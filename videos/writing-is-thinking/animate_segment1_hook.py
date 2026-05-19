#!/usr/bin/env python3
"""
Animate Segment 1 - Hook
Opens with challenge that makes viewer immediately question their own understanding.
Duration: ~20 seconds at 30fps = 600 frames
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Settings
WIDTH, HEIGHT = 1920, 1080
FPS = 30
BG_COLOR = (250, 248, 245)  # Warm off-white
TEXT_COLOR = (40, 40, 40)
HIGHLIGHT_COLOR = (76, 175, 80)  # Green for checkmark
CHALLENGE_COLOR = (220, 50, 50)  # Red for challenge
FONT_SIZE = 52
FONT_SIZE_LARGE = 68

# Load fonts
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONT_SIZE)
    font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", FONT_SIZE_LARGE)
except:
    font = ImageFont.load_default()
    font_large = ImageFont.load_default()

os.makedirs("segment1_frames", exist_ok=True)

def draw_centered_text(text_lines, colors=None, fonts=None, y_start=None):
    """Draw centered text lines with optional colors and fonts"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    if colors is None:
        colors = [TEXT_COLOR] * len(text_lines)
    if fonts is None:
        fonts = [font] * len(text_lines)
    if y_start is None:
        y_start = HEIGHT // 2 - (len(text_lines) * 80) // 2
    
    for i, (text, color, fnt) in enumerate(zip(text_lines, colors, fonts)):
        bbox = draw.textbbox((0, 0), text, font=fnt)
        text_width = bbox[2] - bbox[0]
        x = (WIDTH - text_width) // 2
        y = y_start + i * 90
        draw.text((x, y), text, fill=color, font=fnt)
    
    return img

frame_num = 0

# Sequence 1: Fade in "You just finished reading an article." (90 frames = 3s)
print("Generating sequence 1: Opening line...")
text1 = "You just finished reading an article."
for i in range(90):
    progress = min(1.0, i / 60.0)
    # Fade in by adjusting alpha
    fade_color = tuple(int(BG_COLOR[j] + (TEXT_COLOR[j] - BG_COLOR[j]) * progress) for j in range(3))
    img = draw_centered_text([text1], colors=[fade_color], fonts=[font_large])
    img.save(f"segment1_frames/frame_{frame_num:04d}.png")
    frame_num += 1

# Sequence 2: Add "Someone asks: What was it about?" (60 frames = 2s)
print("Generating sequence 2: The question...")
text2 = "Someone asks: What was it about?"
for i in range(60):
    if i < 45:
        progress = i / 45.0
        fade_color = tuple(int(BG_COLOR[j] + (TEXT_COLOR[j] - BG_COLOR[j]) * progress) for j in range(3))
        img = draw_centered_text([text1, text2], colors=[TEXT_COLOR, fade_color], fonts=[font_large, font])
    else:
        img = draw_centered_text([text1, text2], colors=[TEXT_COLOR, TEXT_COLOR], fonts=[font_large, font])
    img.save(f"segment1_frames/frame_{frame_num:04d}.png")
    frame_num += 1

# Sequence 3: Checkmark + "You can summarize it" (60 frames = 2s)
print("Generating sequence 3: Easy answer...")
text3 = "✓ You can summarize it"
for i in range(60):
    if i < 45:
        progress = i / 45.0
        fade_color = tuple(int(BG_COLOR[j] + (HIGHLIGHT_COLOR[j] - BG_COLOR[j]) * progress) for j in range(3))
        img = draw_centered_text([text1, text2, text3], 
                                colors=[TEXT_COLOR, TEXT_COLOR, fade_color], 
                                fonts=[font_large, font, font])
    else:
        img = draw_centered_text([text1, text2, text3],
                                colors=[TEXT_COLOR, TEXT_COLOR, HIGHLIGHT_COLOR],
                                fonts=[font_large, font, font])
    img.save(f"segment1_frames/frame_{frame_num:04d}.png")
    frame_num += 1

# Sequence 4: Clear and add challenge "But could you write it from memory?" (90 frames = 3s)
print("Generating sequence 4: The challenge...")
challenge1 = "But could you write it"
challenge2 = "from memory?"
for i in range(90):
    if i < 15:
        # Fade out previous
        progress = i / 15.0
        fade1 = tuple(int(TEXT_COLOR[j] + (BG_COLOR[j] - TEXT_COLOR[j]) * progress) for j in range(3))
        fade2 = tuple(int(TEXT_COLOR[j] + (BG_COLOR[j] - TEXT_COLOR[j]) * progress) for j in range(3))
        fade3 = tuple(int(HIGHLIGHT_COLOR[j] + (BG_COLOR[j] - HIGHLIGHT_COLOR[j]) * progress) for j in range(3))
        img = draw_centered_text([text1, text2, text3],
                                colors=[fade1, fade2, fade3],
                                fonts=[font_large, font, font])
    elif i < 30:
        # Blank
        img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    elif i < 60:
        # Fade in challenge line 1
        progress = (i - 30) / 30.0
        fade_color = tuple(int(BG_COLOR[j] + (CHALLENGE_COLOR[j] - BG_COLOR[j]) * progress) for j in range(3))
        img = draw_centered_text([challenge1], colors=[fade_color], fonts=[font_large], y_start=HEIGHT//2 - 50)
    else:
        # Add line 2
        progress = (i - 60) / 30.0
        fade_color = tuple(int(BG_COLOR[j] + (CHALLENGE_COLOR[j] - BG_COLOR[j]) * progress) for j in range(3))
        img = draw_centered_text([challenge1, challenge2], 
                                colors=[CHALLENGE_COLOR, fade_color], 
                                fonts=[font_large, font_large], 
                                y_start=HEIGHT//2 - 80)
    img.save(f"segment1_frames/frame_{frame_num:04d}.png")
    frame_num += 1

# Sequence 5: Blank page with cursor (60 frames = 2s)
print("Generating sequence 5: Blank page...")
for i in range(60):
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    # Draw paper lines
    for j in range(8):
        y = 300 + j * 80
        draw.line([(400, y), (WIDTH - 400, y)], fill=(220, 220, 220), width=1)
    # Blinking cursor
    if (i // 15) % 2 == 0:
        draw.line([(420, 300), (420, 300 + 50)], fill=TEXT_COLOR, width=3)
    img.save(f"segment1_frames/frame_{frame_num:04d}.png")
    frame_num += 1

# Sequence 6: Text appears slowly "Most of us think we could..." (90 frames = 3s)
print("Generating sequence 6: False confidence...")
text_appear = "Most of us think we could..."
for i in range(90):
    progress = i / 90.0
    chars = int(len(text_appear) * progress)
    current = text_appear[:chars]
    
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    for j in range(8):
        y = 300 + j * 80
        draw.line([(400, y), (WIDTH - 400, y)], fill=(220, 220, 220), width=1)
    draw.text((420, 420), current, fill=TEXT_COLOR, font=font)
    img.save(f"segment1_frames/frame_{frame_num:04d}.png")
    frame_num += 1

# Sequence 7: Pause, then "Most of us are wrong." (90 frames = 3s)
print("Generating sequence 7: Truth revealed...")
text_truth = "Most of us are wrong."
for i in range(90):
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    for j in range(8):
        y = 300 + j * 80
        draw.line([(400, y), (WIDTH - 400, y)], fill=(220, 220, 220), width=1)
    draw.text((420, 420), text_appear, fill=TEXT_COLOR, font=font)
    
    if i >= 30:  # Start after 1 second pause
        progress = (i - 30) / 60.0
        chars = int(len(text_truth) * progress)
        current_truth = text_truth[:chars]
        draw.text((420, 500), current_truth, fill=CHALLENGE_COLOR, font=font_large)
    
    img.save(f"segment1_frames/frame_{frame_num:04d}.png")
    frame_num += 1

# Sequence 8: Hold (60 frames = 2s)
print("Generating sequence 8: Final hold...")
for i in range(60):
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    for j in range(8):
        y = 300 + j * 80
        draw.line([(400, y), (WIDTH - 400, y)], fill=(220, 220, 220), width=1)
    draw.text((420, 420), text_appear, fill=TEXT_COLOR, font=font)
    draw.text((420, 500), text_truth, fill=CHALLENGE_COLOR, font=font_large)
    img.save(f"segment1_frames/frame_{frame_num:04d}.png")
    frame_num += 1

print(f"\nGenerated {frame_num} frames (~{frame_num/FPS:.1f} seconds)")
print(f"Frames saved to segment1_frames/")
