import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Color palette (Experience Design Theme)
deep_indigo = '#2c3e60'
memory_gold = '#f39c12'
ending_purple = '#9b59b6'
fade_gray = '#95a5a6'
reality_blue = '#3498db'
story_red = '#e74c3c'
soft_white = '#ecf0f1'

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=deep_indigo)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

# Main title
ax.text(960, 700, 'THE PEAK-END RULE', 
        fontsize=84, color=soft_white, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# Subtitle
ax.text(960, 580, 'Why Memory Lies About Experience', 
        fontsize=48, color=fade_gray,
        ha='center', va='center', fontfamily='sans-serif',
        style='italic')

# Visual element: Simple timeline showing peak and end highlighted
timeline_y = 350
timeline_left = 400
timeline_right = 1520
timeline_width = timeline_right - timeline_left

# Draw timeline base
ax.plot([timeline_left, timeline_right], [timeline_y, timeline_y],
       color=fade_gray, linewidth=3, alpha=0.5)

# Draw multiple moment markers (faded - representing forgotten moments)
num_moments = 20
for i in range(num_moments):
    x = timeline_left + (i / (num_moments-1)) * timeline_width
    ax.plot([x, x], [timeline_y-15, timeline_y+15],
           color=fade_gray, linewidth=2, alpha=0.3)

# Highlight the PEAK moment (2/3 through)
peak_x = timeline_left + (2/3) * timeline_width
peak_marker = plt.Circle((peak_x, timeline_y), 35, 
                         color=memory_gold, zorder=10)
ax.add_patch(peak_marker)
ax.text(peak_x, timeline_y, 'PEAK', 
       fontsize=20, color=deep_indigo, weight='bold',
       ha='center', va='center', fontfamily='sans-serif', zorder=11)

# Highlight the END moment
end_x = timeline_right
end_marker = plt.Circle((end_x, timeline_y), 35,
                        color=ending_purple, zorder=10)
ax.add_patch(end_marker)
ax.text(end_x, timeline_y, 'END',
       fontsize=20, color=soft_white, weight='bold',
       ha='center', va='center', fontfamily='sans-serif', zorder=11)

# Labels
ax.text(timeline_left, timeline_y - 80, 'Experience',
       fontsize=28, color=fade_gray, ha='left', va='top',
       fontfamily='sans-serif')
ax.text(timeline_right, timeline_y - 80, 'Memory',
       fontsize=28, color=memory_gold, ha='right', va='top',
       fontfamily='sans-serif', weight='bold')

# Channel branding at bottom
ax.text(960, 140, 'PERSISTENCE & SCALE', 
        fontsize=32, color=soft_white, alpha=0.6,
        ha='center', va='center', fontfamily='sans-serif')

plt.tight_layout(pad=0)
plt.savefig('frame01_title.png', dpi=100, bbox_inches='tight',
            pad_inches=0, facecolor=deep_indigo)
plt.close()
print("✅ Frame 1 created: Title card with peak-end timeline")
