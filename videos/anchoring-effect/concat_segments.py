from pathlib import Path
import subprocess


def main() -> None:
    segments_dir = Path("segments")
    output_list = Path("concat_list.txt")
    output_video = Path("anchoring_effect_final.mp4")

    segments = sorted(segments_dir.glob("segment*.mp4"))
    if not segments:
        raise SystemExit(f"No MP4 segments found in {segments_dir}")

    with output_list.open("w", encoding="utf-8") as concat_file:
        for segment in segments:
            concat_file.write(f"file '{segment.as_posix()}'\n")

    if output_video.exists():
        output_video.unlink()

    command = [
        "ffmpeg",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(output_list),
        "-c",
        "copy",
        str(output_video),
    ]

    subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
