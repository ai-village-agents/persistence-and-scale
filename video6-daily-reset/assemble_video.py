#!/usr/bin/env python3

from pathlib import Path

from moviepy import AudioFileClip, ImageClip, concatenate_videoclips


def build_segment(index: int):
    """Create a single video segment from corresponding audio and image files."""
    suffix = f"{index:02d}"
    audio_path = Path("audio") / f"segment_{suffix}.wav"
    image_path = Path("visuals") / f"slide_{suffix}.png"

    audio_clip = AudioFileClip(str(audio_path))
    duration = audio_clip.duration

    image_clip = ImageClip(str(image_path), duration=duration).resized(
        (1920, 1080)
    ).with_audio(audio_clip)
    return image_clip


def main():
    segments = [build_segment(i) for i in range(1, 9)]
    final_clip = concatenate_videoclips(segments)
    final_clip.write_videofile(
        "daily_reset_v1.mp4",
        fps=1,
        codec="libx264",
        audio_codec="aac",
        preset="ultrafast",
    )


if __name__ == "__main__":
    main()
