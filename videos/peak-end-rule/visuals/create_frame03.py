import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Color palette
deep_indigo = '#2c3e60'
memory_gold = '#f39c12'
ending_purple = '#9b59b6'
fade_gray = '#95a5a6'
reality_blue = '#3498db'
soft_white = '#ecf0f1'

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=deep_indigo)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

# Title
ax.text(960, 1000, 'HOW MEMORY SHORTCUTS', 
        fontsize=56, color=soft_white, weight='bold',
        ha='center', va='top', fontfamily='sans-serif')

# TOP SECTION: Full experience timeline
top_y = 800
ax.text(300, top_y + 60, 'ALL MOMENTS (Reality)', 
        fontsize=36, color=reality_blue, weight='bold',
        ha='left', va='center', fontfamily='sans-serif')

# Draw many small moment boxes (representing all experiences)
box_width = 60
box_height = 80
num_boxes = 20
start_x = 300
spacing = 70

for i in range(num_boxes):
    x = start_x + i * spacing
    # Random heights to show varying intensity
    height = box_height * (0.4 + 0.6 * np.random.random())
    y_bottom = top_y - height
    
    # Most boxes are faded blue
    if i == 13:  # Peak moment
        color = memory_gold
        alpha = 1.0
    elif i == num_boxes - 1:  # End moment
        color = ending_purple
        alpha = 1.0
    else:
        color = reality_blue
        alpha = 0.3
    
    box = FancyBboxPatch((x, y_bottom), box_width, height,
                         boxstyle="round,pad=3",
                         facecolor=color, edgecolor=color,
                         alpha=alpha, linewidth=2)
    ax.add_patch(box)

# Arrow pointing down
arrow = FancyArrowPatch((960, top_y - 150), (960, 520),
                       arrowstyle='->', mutation_scale=40,
                       linewidth=4, color=soft_white, alpha=0.6)
ax.add_patch(arrow)

ax.text(1100, 620, 'Memory\nshortcuts', 
        fontsize=32, color=soft_white, alpha=0.6,
        ha='left', va='center', fontfamily='sans-serif',
        style='italic')

# BOTTOM SECTION: Memory only captures 2 moments
bottom_y = 380
ax.text(300, bottom_y + 60, 'WHAT MEMORY KEEPS', 
        fontsize=36, color=memory_gold, weight='bold',
        ha='left', va='center', fontfamily='sans-serif')

# Only 2 boxes: peak and end
peak_x = 600
end_x = 1200

# Peak box
peak_box = FancyBboxPatch((peak_x, bottom_y - 100), 140, 120,
                         boxstyle="round,pad=5",
                         facecolor=memory_gold, edgecolor=memory_gold,
                         linewidth=3)
ax.add_patch(peak_box)
ax.text(peak_x + 70, bottom_y - 40, 'PEAK', 
       fontsize=32, color=deep_indigo, weight='bold',
       ha='center', va='center', fontfamily='sans-serif')
ax.text(peak_x + 70, bottom_y - 180, 'Most intense\nmoment', 
       fontsize=24, color=soft_white, alpha=0.8,
       ha='center', va='top', fontfamily='sans-serif')

# End box
end_box = FancyBboxPatch((end_x, bottom_y - 100), 140, 120,
                        boxstyle="round,pad=5",
                        facecolor=ending_purple, edgecolor=ending_purple,
                        linewidth=3)
ax.add_patch(end_box)
ax.text(end_x + 70, bottom_y - 40, 'END',
       fontsize=32, color=soft_white, weight='bold',
       ha='center', va='center', fontfamily='sans-serif')
ax.text(end_x + 70, bottom_y - 180, 'Final\nmoment',
       fontsize=24, color=soft_white, alpha=0.8,
       ha='center', va='top', fontfamily='sans-serif')

# Bottom note
ax.text(960, 100, 'Everything else fades from memory',
       fontsize=32, color=fade_gray, style='italic',
       ha='center', va='center', fontfamily='sans-serif')

plt.tight_layout(pad=0)
plt.savefig('frame03_the_rule.png', dpi=100, bbox_inches='tight',
            pad_inches=0, facecolor=deep_indigo)
plt.close()
print("✅ Frame 3 created: Memory shortcut visualization")
