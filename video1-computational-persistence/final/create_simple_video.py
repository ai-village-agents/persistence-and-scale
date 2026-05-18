import json
from moviepy import *

# Load timing metadata
with open('../audio/metadata.json', 'r') as f:
    metadata = json.load(f)

# Define which image to show for each section
section_images = {
    'intro': '../assets/GROWTH_CHART.png',
    'chapter1': '../assets/GROWTH_CHART.png',
    'chapter2': '../assets/ARCHITECTURE_DIAGRAM.png',
    'chapter3': '../assets/TIMELINE.png',
    'chapter4': '../assets/PERFORMANCE_CHART.png',
    'conclusion': '../assets/MILESTONES_CELEBRATION.png'
}

# Load audio
audio = AudioFileClip('../audio/full_narration.wav')

# Create video clips for each section
clips = []
for section in metadata['sections']:
    img_path = section_images.get(section['id'], '../assets/GROWTH_CHART.png')
    duration = section['duration']
    
    img_clip = ImageClip(img_path, duration=duration)
    clips.append(img_clip)

# Concatenate all clips
video = concatenate_videoclips(clips)
video = video.with_audio(audio)

# Write output
print("Writing video...")
video.write_videofile('computational_persistence_v1.mp4', fps=1, codec='libx264', audio_codec='aac', preset='ultrafast', logger=None)
print("Done!")
