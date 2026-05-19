#!/usr/bin/env python3
"""
Animate Segment 3 - The Test
Shows the visceral experience of trying to write from memory and hitting gaps.
Duration: ~35 seconds at 30fps = 1050 frames
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Settings
WIDTH, HEIGHT = 1920, 1080
FPS = 30
BG_COLOR = (250, 248, 245)  # Warm off-white paper
TEXT_COLOR = (40, 40, 40)   # Near black
CURSOR_COLOR = (40, 40, 40)
FONT_SIZE = 48
LINE_HEIGHT = 70

# Load font
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONT_SIZE)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
except:
    font = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Create output directory
os.makedirs("segment3_frames", exist_ok=True)

def draw_cursor(draw, x, y, show=True):
    """Draw blinking cursor"""
    if show:
        draw.line([(x, y), (x, y + FONT_SIZE)], fill=CURSOR_COLOR, width=3)

def draw_text_on_page(text_lines, cursor_pos=None, cursor_visible=True):
    """Draw text on a page with optional cursor"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Add subtle paper lines
    line_y = 250
    for i in range(12):
        y = line_y + i * LINE_HEIGHT
        draw.line([(300, y), (WIDTH - 300, y)], fill=(220, 220, 220), width=1)
    
    # Draw text
    y_offset = 250
    for i, line_text in enumerate(text_lines):
        x_offset = 320
        draw.text((x_offset, y_offset + i * LINE_HEIGHT), line_text, fill=TEXT_COLOR, font=font)
    
    # Draw cursor if specified
    if cursor_pos is not None:
        line_idx, char_idx = cursor_pos
        x_base = 320
        if line_idx < len(text_lines) and char_idx <= len(text_lines[line_idx]):
            text_before = text_lines[line_idx][:char_idx]
            bbox = draw.textbbox((0, 0), text_before, font=font)
            cursor_x = x_base + (bbox[2] - bbox[0])
            cursor_y = 250 + line_idx * LINE_HEIGHT
            draw_cursor(draw, cursor_x, cursor_y, cursor_visible)
    
    return img

# Animation sequence
frame_num = 0
sequences = []

# Sequence 1: Book closing / article ending (60 frames = 2s)
print("Generating sequence 1: Article closing...")
for i in range(60):
    img = Image.new('RGB', (WIDTH, HEIGHT), (230, 230, 230))
    draw = ImageDraw.Draw(img)
    draw.text((WIDTH//2 - 200, HEIGHT//2 - 50), "Article about photosynthesis", 
              fill=TEXT_COLOR, font=font_small)
    alpha = i / 60.0
    overlay = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    img = Image.blend(img, overlay, alpha)
    img.save(f"segment3_frames/frame_{frame_num:04d}.png")
    frame_num += 1
    sequences.append("article_closing")

# Sequence 2: Blank page with cursor appears (30 frames = 1s)
print("Generating sequence 2: Blank page appears...")
for i in range(30):
    cursor_visible = (i // 15) % 2 == 0  # Blink every 0.5s
    img = draw_text_on_page([], cursor_pos=(0, 0), cursor_visible=cursor_visible)
    img.save(f"segment3_frames/frame_{frame_num:04d}.png")
    frame_num += 1
    sequences.append("blank_page")

# Sequence 3: Strong start - "Photosynthesis is..." (90 frames = 3s)
print("Generating sequence 3: Strong start...")
text = "Photosynthesis is"
for i in range(90):
    progress = min(1.0, i / 60.0)  # Type over first 2s
    chars_shown = int(len(text) * progress)
    current_text = text[:chars_shown]
    cursor_visible = (i // 15) % 2 == 0
    img = draw_text_on_page([current_text], cursor_pos=(0, len(current_text)), 
                           cursor_visible=cursor_visible and progress >= 1.0)
    img.save(f"segment3_frames/frame_{frame_num:04d}.png")
    frame_num += 1
    sequences.append("strong_start")

# Sequence 4: Pause... thinking (60 frames = 2s)
print("Generating sequence 4: Pause...")
for i in range(60):
    cursor_visible = (i // 15) % 2 == 0
    img = draw_text_on_page(["Photosynthesis is"], cursor_pos=(0, 17), cursor_visible=cursor_visible)
    img.save(f"segment3_frames/frame_{frame_num:04d}.png")
    frame_num += 1
    sequences.append("pause_1")

# Sequence 5: Hesitant continuation - "...the process where..." (90 frames = 3s)
print("Generating sequence 5: Hesitant text...")
line1 = "Photosynthesis is"
text2 = "...the process where"
for i in range(90):
    progress = min(1.0, i / 60.0)
    chars_shown = int(len(text2) * progress)
    current_text2 = text2[:chars_shown]
    cursor_visible = (i // 15) % 2 == 0
    img = draw_text_on_page([line1, current_text2], cursor_pos=(1, len(current_text2)),
                           cursor_visible=cursor_visible and progress >= 1.0)
    img.save(f"segment3_frames/frame_{frame_num:04d}.png")
    frame_num += 1
    sequences.append("hesitant")

# Sequence 6: Longer pause (90 frames = 3s)
print("Generating sequence 6: Long pause...")
for i in range(90):
    cursor_visible = (i // 15) % 2 == 0
    img = draw_text_on_page(["Photosynthesis is", "...the process where"], 
                           cursor_pos=(1, 20), cursor_visible=cursor_visible)
    img.save(f"segment3_frames/frame_{frame_num:04d}.png")
    frame_num += 1
    sequences.append("pause_2")

# Sequence 7: Struggle - text appears then gets deleted (120 frames = 4s)
print("Generating sequence 7: Struggle - type and delete...")
line1 = "Photosynthesis is"
line2 = "...the process where"
struggle_text = "Wait, does the light"

# Type struggle text (2s = 60 frames)
for i in range(60):
    progress = i / 60.0
    chars_shown = int(len(struggle_text) * progress)
    current_struggle = struggle_text[:chars_shown]
    cursor_visible = (i // 15) % 2 == 0
    img = draw_text_on_page([line1, line2, current_struggle], 
                           cursor_pos=(2, len(current_struggle)), cursor_visible=cursor_visible)
    img.save(f"segment3_frames/frame_{frame_num:04d}.png")
    frame_num += 1
    sequences.append("struggle_type")

# Delete struggle text (2s = 60 frames)
for i in range(60):
    progress = i / 60.0
    chars_remaining = len(struggle_text) - int(len(struggle_text) * progress)
    current_struggle = struggle_text[:chars_remaining]
    cursor_visible = (i // 15) % 2 == 0
    img = draw_text_on_page([line1, line2, current_struggle], 
                           cursor_pos=(2, len(current_struggle)), cursor_visible=cursor_visible)
    img.save(f"segment3_frames/frame_{frame_num:04d}.png")
    frame_num += 1
    sequences.append("struggle_delete")

# Sequence 8: Gap becomes visible - confused fragments (90 frames = 3s)
print("Generating sequence 8: Gap visible...")
line1 = "Photosynthesis is"
line2 = "...the process where"
gap_text = "chlorophyll? split first?"
for i in range(90):
    if i < 45:
        progress = i / 45.0
        chars_shown = int(len(gap_text) * progress)
        current_gap = gap_text[:chars_shown]
    else:
        current_gap = gap_text
    cursor_visible = (i // 15) % 2 == 0
    img = draw_text_on_page([line1, line2, current_gap], 
                           cursor_pos=(2, len(current_gap)), cursor_visible=cursor_visible)
    img.save(f"segment3_frames/frame_{frame_num:04d}.png")
    frame_num += 1
    sequences.append("gap_visible")

# Sequence 9: Realization - cursor stops, incomplete fragments visible (90 frames = 3s)
print("Generating sequence 9: Realization...")
for i in range(90):
    img = draw_text_on_page(["Photosynthesis is", "...the process where", "chlorophyll? split first?"],
                           cursor_pos=None)  # No cursor - giving up
    img.save(f"segment3_frames/frame_{frame_num:04d}.png")
    frame_num += 1
    sequences.append("realization")

# Sequence 10: Final hold (90 frames = 3s)
print("Generating sequence 10: Final hold...")
for i in range(90):
    img = draw_text_on_page(["Photosynthesis is", "...the process where", "chlorophyll? split first?", "", "...I thought I knew this."],
                           cursor_pos=None)
    img.save(f"segment3_frames/frame_{frame_num:04d}.png")
    frame_num += 1
    sequences.append("final_hold")

print(f"\nGenerated {frame_num} frames (~{frame_num/FPS:.1f} seconds)")
print(f"Frames saved to segment3_frames/")
