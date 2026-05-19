"""
Test creating animated segment 7 with text appearing line by line
Generate a sequence of frames showing progressive text reveal
"""

from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1920, 1080
BG_COLOR = "#1a1a1a"
PAPER_COLOR = "#f5f5f5"
TEXT_DARK = "#2c2c2c"

# Create frames directory
os.makedirs('animation_test_frames', exist_ok=True)

try:
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 56)
except:
    font_text = font_title = ImageFont.load_default()

# Text lines to appear
lines = [
    "The blank page doesn't lie.",
    "",
    "It shows you what you really know",
    "versus what you only recognized.",
    "",
    "You can't build on a foundation",
    "that isn't really there.",
    "",
    "So write. Find the gaps.",
    "That's where learning begins."
]

# Paper dimensions
paper_left = 300
paper_top = 200
paper_width = 1320
paper_height = 700

def create_frame(lines_visible):
    """Create a frame with specified number of lines visible"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Shadow
    draw.rectangle([paper_left + 8, paper_top + 8,
                   paper_left + paper_width + 8, paper_top + paper_height + 8],
                  fill="#000000")
    
    # Paper
    draw.rectangle([paper_left, paper_top,
                   paper_left + paper_width, paper_top + paper_height],
                  fill=PAPER_COLOR, outline="#cccccc", width=2)
    
    # Ruled lines
    for i in range(15):
        y = paper_top + 60 + i * 42
        draw.line([paper_left + 50, y, paper_left + paper_width - 50, y],
                 fill="#d0d0d0", width=1)
    
    # Draw visible lines
    y_pos = paper_top + 60
    for i in range(min(lines_visible, len(lines))):
        draw.text((paper_left + 60, y_pos), lines[i],
                 fill=TEXT_DARK, font=font_text, anchor="lt")
        y_pos += 42
    
    # Cursor at end of last visible line if not all shown
    if lines_visible < len(lines):
        cursor_x = paper_left + 60 + len(lines[lines_visible-1]) * 15
        cursor_y = y_pos - 42
        draw.rectangle([cursor_x + 10, cursor_y, cursor_x + 15, cursor_y + 32],
                      fill="#2a4a2a")
    
    # Bottom text
    draw.text((WIDTH // 2, paper_top + paper_height + 80),
             "Start with the blank page test today",
             fill=PAPER_COLOR, font=font_title, anchor="mm")
    
    return img

# Create frames: start with blank page, add one line at a time
# Hold each line for a few frames (~0.5 seconds at 30fps = 15 frames)
frame_num = 0

# Initial blank page (hold for 1 second = 30 frames)
print("Creating initial blank frames...")
for i in range(30):
    img = create_frame(0)
    img.save(f'animation_test_frames/frame_{frame_num:04d}.png')
    frame_num += 1

# Add lines progressively
print("Creating progressive reveal frames...")
for line_count in range(1, len(lines) + 1):
    # Hold each line for 0.5 seconds = 15 frames
    for i in range(15):
        img = create_frame(line_count)
        img.save(f'animation_test_frames/frame_{frame_num:04d}.png')
        frame_num += 1

# Final hold (2 seconds = 60 frames)
print("Creating final hold frames...")
for i in range(60):
    img = create_frame(len(lines))
    img.save(f'animation_test_frames/frame_{frame_num:04d}.png')
    frame_num += 1

print(f"\n✓ Created {frame_num} frames")
print(f"Duration: {frame_num / 30:.1f} seconds at 30fps")
