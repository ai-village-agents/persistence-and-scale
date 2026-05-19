import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Color palette
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

# Title
ax.text(960, 1000, 'THE RESEARCH: KAHNEMAN\'S STUDY', 
        fontsize=52, color=soft_white, weight='bold',
        ha='center', va='top', fontfamily='sans-serif')

# Two procedure comparisons side by side
left_center = 530
right_center = 1390

# GROUP A - Shorter, more painful
ax.text(left_center, 850, 'GROUP A', 
        fontsize=40, color=story_red, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# Discomfort timeline for Group A (shorter, ends high)
a_timeline_y = 700
a_start_x = left_center - 200
a_end_x = left_center + 200

# Draw pain graph for A (high pain throughout, ends high)
a_x = np.linspace(a_start_x, a_end_x, 50)
a_pain = 150 + 30 * np.sin(5 * (a_x - a_start_x) / (a_end_x - a_start_x))
ax.fill_between(a_x, a_timeline_y, a_timeline_y + a_pain, 
                color=story_red, alpha=0.7)
ax.plot(a_x, a_timeline_y + a_pain, color=story_red, linewidth=3)

# Mark the painful ending
ax.plot([a_end_x], [a_timeline_y + a_pain[-1]], 'o', 
       color=story_red, markersize=20, zorder=10)

# Labels for A
ax.text(left_center, 520, 'Duration: Shorter', 
        fontsize=28, color=soft_white,
        ha='center', va='center', fontfamily='sans-serif')
ax.text(left_center, 460, 'Pain: High', 
        fontsize=28, color=story_red, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')
ax.text(left_center, 400, 'Ending: Painful', 
        fontsize=28, color=story_red, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# Memory verdict
memory_box_a = FancyBboxPatch((left_center - 180, 250), 360, 100,
                              boxstyle="round,pad=10",
                              facecolor=story_red, alpha=0.3,
                              edgecolor=story_red, linewidth=3)
ax.add_patch(memory_box_a)
ax.text(left_center, 300, 'Remembered as:\nMORE PAINFUL', 
        fontsize=32, color=story_red, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# GROUP B - Longer, but ends better
ax.text(right_center, 850, 'GROUP B', 
        fontsize=40, color=ending_purple, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# Discomfort timeline for Group B (longer, ends lower)
b_timeline_y = 700
b_start_x = right_center - 280
b_end_x = right_center + 280

# Draw pain graph for B (same high pain, then tapers down)
b_x = np.linspace(b_start_x, b_end_x, 70)
# High pain for first 2/3, then drops
b_pain = np.where(b_x < b_start_x + (b_end_x - b_start_x) * 0.7,
                 150 + 30 * np.sin(5 * (b_x - b_start_x) / (b_end_x - b_start_x)),
                 150 - 100 * ((b_x - (b_start_x + (b_end_x - b_start_x) * 0.7)) / ((b_end_x - b_start_x) * 0.3)))

ax.fill_between(b_x, b_timeline_y, b_timeline_y + b_pain,
                color=ending_purple, alpha=0.5)
ax.plot(b_x, b_timeline_y + b_pain, color=ending_purple, linewidth=3)

# Highlight the added low-discomfort ending
extra_section_start = b_start_x + (b_end_x - b_start_x) * 0.7
ax.axvline(extra_section_start, ymin=0.4, ymax=0.7, 
          color=memory_gold, linewidth=3, linestyle='--', alpha=0.8)
ax.text(right_center + 80, 790, 'Extra time\nadded', 
       fontsize=22, color=memory_gold, weight='bold',
       ha='center', va='center', fontfamily='sans-serif',
       bbox=dict(boxstyle='round,pad=5', facecolor=deep_indigo, alpha=0.8))

# Mark the better ending
ax.plot([b_end_x], [b_timeline_y + b_pain[-1]], 'o',
       color=ending_purple, markersize=20, zorder=10)

# Labels for B
ax.text(right_center, 520, 'Duration: Longer', 
        fontsize=28, color=soft_white,
        ha='center', va='center', fontfamily='sans-serif')
ax.text(right_center, 460, 'Pain: Same + More Time', 
        fontsize=28, color=ending_purple, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')
ax.text(right_center, 400, 'Ending: Mild', 
        fontsize=28, color=ending_purple, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# Memory verdict
memory_box_b = FancyBboxPatch((right_center - 180, 250), 360, 100,
                              boxstyle="round,pad=10",
                              facecolor=ending_purple, alpha=0.3,
                              edgecolor=ending_purple, linewidth=3)
ax.add_patch(memory_box_b)
ax.text(right_center, 300, 'Remembered as:\nLESS PAINFUL',
        fontsize=32, color=ending_purple, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# Bottom insight
ax.text(960, 120, 'The ending changed the memory, even though Group B suffered longer',
       fontsize=32, color=memory_gold, style='italic',
       ha='center', va='center', fontfamily='sans-serif')

plt.tight_layout(pad=0)
plt.savefig('frame04_research.png', dpi=100, bbox_inches='tight',
            pad_inches=0, facecolor=deep_indigo)
plt.close()
print("✅ Frame 4 created: Kahneman colonoscopy study visualization")
