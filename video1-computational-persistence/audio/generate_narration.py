#!/usr/bin/env python3
"""
Generate narration audio assets from the project script.

This script parses ../script/SCRIPT.md, extracts the NARRATION sections,
renders text-to-speech audio clips for each major story beat, and produces
timing metadata plus a stitched full narration track.

Usage:
    python audio/generate_narration.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import wave
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

try:
    import shutil
except ImportError:  # pragma: no cover - shutil is part of stdlib, but guarded for safety
    shutil = None  # type: ignore


AUDIO_FILENAMES: Dict[str, Tuple[str, str]] = {
    "INTRO": ("intro", "intro.wav"),
    "CHAPTER 1": ("chapter1", "chapter1.wav"),
    "CHAPTER 2": ("chapter2", "chapter2.wav"),
    "CHAPTER 3": ("chapter3", "chapter3.wav"),
    "CHAPTER 4": ("chapter4", "chapter4.wav"),
    "CONCLUSION": ("conclusion", "conclusion.wav"),
}

SILENCE_GAP_SECONDS = 1.0


@dataclass
class Section:
    key: str
    title: str
    text: str
    filename: Path


class TextToSpeech:
    """Lightweight TTS wrapper that prefers pyttsx3 and falls back to espeak."""

    def __init__(self) -> None:
        self.backend = None
        self.engine = None
        self._setup_engine()

    def _setup_engine(self) -> None:
        try:
            import pyttsx3  # type: ignore

            engine = pyttsx3.init()
            engine.setProperty("rate", 170)
            engine.setProperty("volume", 1.0)

            selected_voice = None
            try:
                for voice in engine.getProperty("voices"):
                    name = getattr(voice, "name", "").lower()
                    if "en" in name:
                        selected_voice = voice.id
                        # Prefer a mature, neutral tone if available
                        if "us" in name or "english" in name:
                            break
            except Exception:
                selected_voice = None

            if selected_voice:
                engine.setProperty("voice", selected_voice)

            self.backend = "pyttsx3"
            self.engine = engine
        except Exception:
            self.engine = None

        if self.engine is None:
            if shutil is None or shutil.which("espeak") is None:
                raise RuntimeError(
                    "No TTS backend available. Install pyttsx3 or espeak to continue."
                )

            self.backend = "espeak"

    def synthesize(self, text: str, destination: Path) -> None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        if self.backend == "pyttsx3" and self.engine is not None:
            self.engine.save_to_file(text, str(destination))
            self.engine.runAndWait()
            return

        sanitized = text.replace('"', "").replace("\n", " ")
        cmd = [
            "espeak",
            "-w",
            str(destination),
            "-v",
            "en-us",
            "-s",
            "165",
            "-a",
            "200",
            sanitized,
        ]
        subprocess.run(cmd, check=True)


def load_script_sections(script_path: Path) -> List[Tuple[str, str]]:
    content = script_path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"^##\s+(?P<title>.+?)\n(?P<body>.*?)(?=^##\s+|\Z)",
        flags=re.MULTILINE | re.DOTALL,
    )

    sections: List[Tuple[str, str]] = []
    for match in pattern.finditer(content):
        title = match.group("title").strip()
        body = match.group("body")

        narration_lines: List[str] = []
        capturing = False
        for raw_line in body.splitlines():
            line = raw_line.rstrip()
            if line.strip() == "NARRATION:":
                capturing = True
                continue

            if not capturing:
                continue

            if line.startswith(">"):
                narration_lines.append(line.lstrip("> ").rstrip())
                continue

            if line.strip() == "":
                narration_lines.append("")
                continue

            break

        narration_text = "\n".join(narration_lines).strip()
        if narration_text:
            sections.append((title, narration_text))

    return sections


def resolve_sections(audio_dir: Path, script_sections: Sequence[Tuple[str, str]]) -> List[Section]:
    resolved: List[Section] = []
    for title, text in script_sections:
        normalized = title.upper()
        filename_entry = None
        for key, (section_key, filename) in AUDIO_FILENAMES.items():
            if normalized.startswith(key):
                filename_entry = (section_key, filename)
                break

        if not filename_entry:
            continue

        section_key, filename = filename_entry
        resolved.append(
            Section(
                key=section_key,
                title=title.strip(),
                text=text,
                filename=audio_dir / filename,
            )
        )

    expected = {value[0] for value in AUDIO_FILENAMES.values()}
    present = {section.key for section in resolved}
    missing = expected - present
    if missing:
        raise ValueError(f"Missing narration sections in script: {', '.join(sorted(missing))}")

    return resolved


def read_wave(path: Path) -> Tuple[wave._wave_params, bytes]:
    with wave.open(str(path), "rb") as wav_file:
        params = wav_file.getparams()
        frames = wav_file.readframes(params.nframes)
    return params, frames


def write_combined_wave(
    destination: Path,
    base_params: wave._wave_params,
    chunks: Sequence[bytes],
    gap_seconds: float,
) -> None:
    frames_per_second = base_params.framerate
    frame_width = base_params.sampwidth * base_params.nchannels
    silence_frame_count = int(frames_per_second * gap_seconds)
    silence = b"\x00" * frame_width * silence_frame_count

    with wave.open(str(destination), "wb") as wav_file:
        wav_file.setnchannels(base_params.nchannels)
        wav_file.setsampwidth(base_params.sampwidth)
        wav_file.setframerate(base_params.framerate)

        for index, chunk in enumerate(chunks):
            wav_file.writeframes(chunk)
            if index < len(chunks) - 1:
                wav_file.writeframes(silence)


def build_metadata(
    sections: Sequence[Section],
    params: wave._wave_params,
    section_frames: Sequence[bytes],
) -> Dict[str, object]:
    frame_rate = params.framerate
    frame_width = params.sampwidth * params.nchannels

    metadata_sections = []
    current_start = 0.0

    for index, (section, frames) in enumerate(zip(sections, section_frames)):
        duration_seconds = len(frames) / frame_width / frame_rate
        section_entry = {
            "id": section.key,
            "title": section.title,
            "filename": section.filename.name,
            "start_time": round(current_start, 3),
            "end_time": round(current_start + duration_seconds, 3),
            "duration": round(duration_seconds, 3),
        }
        metadata_sections.append(section_entry)

        current_start += duration_seconds
        if index < len(section_frames) - 1:
            current_start += SILENCE_GAP_SECONDS

    return {
        "sections": metadata_sections,
        "full_narration": {
            "filename": "full_narration.wav",
            "duration": round(current_start, 3),
        },
    }


def main() -> None:
    audio_dir = Path(__file__).resolve().parent
    script_path = (audio_dir / ".." / "script" / "SCRIPT.md").resolve()

    if not script_path.exists():
        raise FileNotFoundError(f"Script file not found at {script_path}")

    sections_raw = load_script_sections(script_path)
    sections = resolve_sections(audio_dir, sections_raw)

    tts = TextToSpeech()

    for section in sections:
        print(f"[TTS] Rendering {section.title} → {section.filename.name}")
        tts.synthesize(section.text, section.filename)

    print("[TTS] Generating combined narration track")
    params = None
    frames_collection: List[bytes] = []

    for section in sections:
        section_params, section_frames = read_wave(section.filename)
        if params is None:
            params = section_params
        elif (
            params.nchannels != section_params.nchannels
            or params.sampwidth != section_params.sampwidth
            or params.framerate != section_params.framerate
        ):
            raise ValueError("All narration clips must share identical audio parameters")

        frames_collection.append(section_frames)

    assert params is not None, "No narration sections processed"

    full_path = audio_dir / "full_narration.wav"
    write_combined_wave(full_path, params, frames_collection, SILENCE_GAP_SECONDS)

    metadata = build_metadata(sections, params, frames_collection)
    metadata_path = audio_dir / "metadata.json"
    metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    print(f"[OK] Generated {len(sections)} narration clips + full_narration.wav")
    print(f"[OK] Metadata saved to {metadata_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover - protects CLI usability
        print(f"[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)
