#!/usr/bin/env python3
"""
Assemble Video 9: The Inverted U of Trying
Frame timing synchronized with 179-second audio narration
"""

from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
import os

# Paths
visuals_dir = "visuals"
audio_path = "audio/narration_full.mp3"
output_path = "inverted_u_trying_v1.mp4"

# Frame timing (total 179 seconds to match audio)
frames = [
    ("frame_01_title_simple.png", 5),
    ("frame_02_hook.png", 10),
    ("inverted_u_curve_simple.png", 15),
    ("frame_04_comparison.png", 20),
    ("frame_05_remembering.png", 20),
    ("frame_06_sleep.png", 20),
    ("frame_07_brain_body_minimal.png", 20),
    ("frame_08_recognition_minimal.png", 20),
    ("frame_09_grip_transformation.png", 24),  # 25 -> 24 to match 179s total
    ("frame_10_takeaway_minimal.png", 20),
    ("frame_11_closing.png", 5)
]

print(f"Total frame duration: {sum(f[1] for f in frames)} seconds")

# Create video clips
clips = []
for filename, duration in frames:
    path = os.path.join(visuals_dir, filename)
    print(f"Loading {filename} ({duration}s)...")
    clip = ImageClip(path, duration=duration).resized((1920, 1080))
    clips.append(clip)

# Concatenate video clips
print("\nConcatenating clips...")
video = concatenate_videoclips(clips, method="compose")

# Load audio
print("Loading audio...")
audio = AudioFileClip(audio_path)
print(f"Audio duration: {audio.duration:.1f}s")

# Combine video and audio
print("Combining video and audio...")
final_video = video.with_audio(audio)

# Export
print(f"\nExporting to {output_path}...")
final_video.write_videofile(
    output_path,
    fps=30,
    codec='libx264',
    audio_codec='aac',
    preset='medium',
    ffmpeg_params=['-pix_fmt', 'yuv420p', '-movflags', '+faststart']
)

print(f"\n✅ Video exported successfully: {output_path}")
print(f"Duration: {final_video.duration:.1f}s")
