#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from moviepy import AudioFileClip, ImageClip, concatenate_videoclips


SEGMENTS = [
    ("01", 21.34),
    ("02", 29.86),
    ("03", 33.62),
    ("04", 29.11),
    ("05", 31.56),
    ("06", 25.15),
    ("07", 16.80),
]


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    visuals_dir = base_dir / "visuals"
    audio_dir = base_dir / "audio"

    clips = []
    audio_clips = []

    try:
        for suffix, duration in SEGMENTS:
            image_path = visuals_dir / f"slide_{suffix}.png"
            audio_path = audio_dir / f"segment_{suffix}.wav"

            if not image_path.is_file():
                raise FileNotFoundError(f"Missing image: {image_path}")
            if not audio_path.is_file():
                raise FileNotFoundError(f"Missing audio: {audio_path}")

            image_clip = ImageClip(str(image_path), duration=duration).resized((1920, 1080))
            audio_clip = AudioFileClip(str(audio_path))

            segment_clip = image_clip.with_audio(audio_clip)

            clips.append(segment_clip)
            audio_clips.append(audio_clip)

        final_clip = concatenate_videoclips(clips)
        try:
            final_clip.write_videofile(
                "rest_collaboration_v1.mp4",
                fps=1,
                codec="libx264",
                audio_codec="aac",
                preset="ultrafast",
            )
        finally:
            final_clip.close()
    finally:
        for clip in clips:
            clip.close()
        for audio_clip in audio_clips:
            audio_clip.close()


if __name__ == "__main__":
    main()
