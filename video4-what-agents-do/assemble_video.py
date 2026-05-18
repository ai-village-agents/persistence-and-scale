from __future__ import annotations

from pathlib import Path

from moviepy import AudioFileClip, ImageClip, concatenate_videoclips


def main() -> None:
    audio_dir = Path("audio")
    visuals_dir = Path("visuals")

    audio_clips: list[AudioFileClip] = []
    video_clips: list[ImageClip] = []

    try:
        for index in range(1, 8):
            suffix = f"{index:02d}"
            audio_path = audio_dir / f"segment_{suffix}.wav"
            slide_path = visuals_dir / f"slide_{suffix}.png"

            audio_clip = AudioFileClip(str(audio_path))
            audio_clips.append(audio_clip)

            image_clip = (
                ImageClip(str(slide_path), duration=audio_clip.duration)
                .resized((1920, 1080))
                .with_audio(audio_clip)
            )
            video_clips.append(image_clip)

        final_clip = concatenate_videoclips(video_clips)
        final_clip.write_videofile(
            "what_agents_do_v1.mp4",
            fps=1,
            codec="libx264",
            audio_codec="aac",
            preset="ultrafast",
        )
        final_clip.close()
    finally:
        for clip in video_clips:
            clip.close()
        for audio_clip in audio_clips:
            audio_clip.close()


if __name__ == "__main__":
    main()
