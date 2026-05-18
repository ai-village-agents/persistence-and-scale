from pathlib import Path

from moviepy import AudioFileClip, ImageClip, concatenate_videoclips


def main() -> None:
    visuals_dir = Path("visuals")
    audio_path = Path("full_narration.wav")
    output_path = Path("beyond_prompt_response_v1.mp4")

    if not audio_path.is_file():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    slide_paths = [
        visuals_dir / f"slide_{index:02d}.png" for index in range(1, 9)
    ]

    missing_slides = [path for path in slide_paths if not path.is_file()]
    if missing_slides:
        missing_list = ", ".join(str(path) for path in missing_slides)
        raise FileNotFoundError(f"Missing slide images: {missing_list}")

    full_audio = AudioFileClip(str(audio_path))
    audio_duration = full_audio.duration
    if audio_duration is None or audio_duration == 0:
        raise ValueError("Audio duration could not be determined or is zero.")

    duration_per_slide = audio_duration / len(slide_paths)

    slide_clips = []
    for slide_path in slide_paths:
        clip = ImageClip(str(slide_path)).resized((1920, 1080)).with_duration(duration_per_slide)
        slide_clips.append(clip)

    video = concatenate_videoclips(slide_clips).with_audio(full_audio)

    video.write_videofile(
        str(output_path),
        fps=1,
        codec="libx264",
        audio_codec="aac",
        preset="ultrafast",
    )


if __name__ == "__main__":
    main()
