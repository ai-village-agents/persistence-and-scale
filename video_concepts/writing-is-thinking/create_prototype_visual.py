import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Create figure with better aesthetics
fig, ax = plt.subplots(1, 1, figsize=(19.2, 10.8), facecolor='#1a1a1a')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Create a "paper" effect - slightly off-white rectangle with shadow
shadow = patches.Rectangle((12, 18), 76, 60, linewidth=0, 
                          edgecolor='none', facecolor='#0a0a0a', alpha=0.3)
ax.add_patch(shadow)

paper = patches.Rectangle((10, 20), 76, 60, linewidth=2, 
                         edgecolor='#666666', facecolor='#f5f5f5')
ax.add_patch(paper)

# Add subtle lines like ruled paper
for i in range(25, 75, 3):
    ax.plot([15, 81], [i, i], color='#e0e0e0', linewidth=0.5, alpha=0.6)

# Add title text at bottom (outside the paper)
ax.text(50, 10, 'Why Writing is Thinking: The Blank Page Test', 
        ha='center', va='center', fontsize=28, color='#ffffff',
        fontfamily='sans-serif', weight='normal')

plt.tight_layout()
plt.savefig('/tmp/prototype_blank_page.png', dpi=100, facecolor='#1a1a1a',
            bbox_inches='tight', pad_inches=0.1)
plt.close()

print("✓ Prototype visual created: /tmp/prototype_blank_page.png")

# Now create a comparison visual using Pillow for more control
img = Image.new('RGB', (1920, 1080), color='#1a1a1a')
draw = ImageDraw.Draw(img)

# Draw paper with shadow
draw.rectangle([210, 210, 1710, 870], fill='#0a0a0a')  # shadow
draw.rectangle([200, 200, 1700, 860], fill='#f5f5f5', outline='#666666', width=3)  # paper

# Draw ruled lines
for y in range(250, 850, 40):
    draw.line([250, y, 1650, y], fill='#e0e0e0', width=2)

# Add text at bottom (using default font since we may not have custom fonts)
draw.text((960, 950), 'Why Writing is Thinking: The Blank Page Test',
          fill='#ffffff', anchor='mm')

img.save('/tmp/prototype_blank_page_pillow.png')
print("✓ Pillow version created: /tmp/prototype_blank_page_pillow.png")

# Create a second prototype - side-by-side comparison visual
img2 = Image.new('RGB', (1920, 1080), color='#1a1a1a')
draw2 = ImageDraw.Draw(img2)

# Left side - "Reading" (with checkmarks)
draw2.rectangle([50, 150, 900, 900], fill='#2a4a2a', outline='#4a8a4a', width=3)
draw2.text((475, 200), 'READING', fill='#ffffff', anchor='mm')
draw2.text((475, 300), '✓ Makes sense', fill='#8fbc8f', anchor='mm')
draw2.text((475, 400), '✓ Following along', fill='#8fbc8f', anchor='mm')
draw2.text((475, 500), '✓ Ideas are clear', fill='#8fbc8f', anchor='mm')
draw2.text((475, 700), 'Recognition', fill='#ffffff', anchor='mm')

# Right side - "Writing" (with question marks)
draw2.rectangle([1020, 150, 1870, 900], fill='#4a2a2a', outline='#8a4a4a', width=3)
draw2.text((1445, 200), 'WRITING', fill='#ffffff', anchor='mm')
draw2.text((1445, 300), '? Wait, what comes first?', fill='#bc8f8f', anchor='mm')
draw2.text((1445, 400), '? How does this connect?', fill='#bc8f8f', anchor='mm')
draw2.text((1445, 500), '? What was that part again?', fill='#bc8f8f', anchor='mm')
draw2.text((1445, 700), 'Understanding', fill='#ffffff', anchor='mm')

# Title at top
draw2.text((960, 50), 'The Illusion of Understanding', fill='#ffffff', anchor='mm')

img2.save('/tmp/prototype_comparison.png')
print("✓ Comparison visual created: /tmp/prototype_comparison.png")

print("\nPrototype visuals complete. These demonstrate:")
print("1. Better aesthetic design (not just matplotlib defaults)")
print("2. Visual variety (blank page, comparison layout)")
print("3. Meaningful graphics that support the narrative")
print("\nThis is a significant quality improvement over yesterday's work.")
