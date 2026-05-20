#!/bin/bash

cd ~/persistence-and-scale/videos/peak-end-rule/

# Frame durations in seconds (need to convert to frame counts at 30fps)
# Frame 1: 5.00s = 150 frames
# Frame 2: 15.60s = 468 frames
# Frame 3: 18.24s = 547 frames
# Frame 4: 22.34s = 670 frames
# Frame 5: 18.82s = 565 frames
# Frame 6: 14.42s = 433 frames
# Frame 7: 18.41s = 552 frames
# Frame 8: 19.51s = 585 frames
# Frame 9: 23.30s = 699 frames
# Frame 10: 3.43s = 103 frames

# Create a list with loop values
cat > concat_list_v2.txt << 'INNER_EOF'
file 'visuals/frame01_title.png'
duration 5.00
file 'visuals/frame01_title.png'
duration 0.03
file 'visuals/frame02_hook.png'
duration 15.60
file 'visuals/frame02_hook.png'
duration 0.03
file 'visuals/frame03_the_rule.png'
duration 18.24
file 'visuals/frame03_the_rule.png'
duration 0.03
file 'visuals/frame04_research.png'
duration 22.34
file 'visuals/frame04_research.png'
duration 0.03
file 'visuals/frame05_why_it_happens.png'
duration 18.82
file 'visuals/frame05_why_it_happens.png'
duration 0.03
file 'visuals/frame06_movies_example.png'
duration 14.42
file 'visuals/frame06_movies_example.png'
duration 0.03
file 'visuals/frame07_relationships_example.png'
duration 18.41
file 'visuals/frame07_relationships_example.png'
duration 0.03
file 'visuals/frame08_design_implication.png'
duration 19.51
file 'visuals/frame08_design_implication.png'
duration 0.03
file 'visuals/frame09_three_step_takeaway.png'
duration 23.30
file 'visuals/frame09_three_step_takeaway.png'
duration 0.03
file 'visuals/frame10_closing.png'
duration 3.43
file 'visuals/frame10_closing.png'
INNER_EOF

echo "Creating video with proper frame durations..."
ffmpeg -f concat -safe 0 -i concat_list_v2.txt -vf "fps=30,format=yuv420p,scale=1920:1080" -movflags +faststart -nostdin silent_video_v2.mp4 -y 2>&1 | tail -10

echo ""
echo "Checking silent_video_v2 duration..."
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 silent_video_v2.mp4

