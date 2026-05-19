import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Color palette
deep_indigo = '#2c3e60'
memory_gold = '#f39c12'
ending_purple = '#9b59b6'
fade_gray = '#95a5a6'
soft_white = '#ecf0f1'

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=deep_indigo)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

# Title
ax.text(960, 1000, 'EXAMPLE: MOVIES', 
        fontsize=56, color=soft_white, weight='bold',
        ha='center', va='top', fontfamily='sans-serif')

# Movie timeline visualization
timeline_y = 650
timeline_start = 300
timeline_end = 1620
timeline_length = timeline_end - timeline_start

# Draw movie "screen" backdrop
screen = Rectangle((250, 450), 1420, 350,
                   facecolor='#1a1a1a', edgecolor=soft_white,
                   linewidth=3)
ax.add_patch(screen)

# Timeline bar
ax.plot([timeline_start, timeline_end], [timeline_y, timeline_y],
       color=fade_gray, linewidth=8, alpha=0.5)

# Segment the movie into acts with quality indicators
# Act 1: Boring opening (faded)
act1_end = timeline_start + timeline_length * 0.25
for i in range(8):
    x = timeline_start + i * (act1_end - timeline_start) / 8
    ax.plot([x, x], [timeline_y - 40, timeline_y + 40],
           color=fade_gray, linewidth=4, alpha=0.3)
ax.text((timeline_start + act1_end) / 2, timeline_y - 90,
       'Act 1: Slow start',
       fontsize=24, color=fade_gray, alpha=0.5,
       ha='center', va='top', fontfamily='sans-serif')

# Act 2: Boring middle (faded)
act2_start = act1_end
act2_end = timeline_start + timeline_length * 0.65
for i in range(12):
    x = act2_start + i * (act2_end - act2_start) / 12
    ax.plot([x, x], [timeline_y - 40, timeline_y + 40],
           color=fade_gray, linewidth=4, alpha=0.3)
ax.text((act2_start + act2_end) / 2, timeline_y - 90,
       'Act 2: Drags on...',
       fontsize=24, color=fade_gray, alpha=0.5,
       ha='center', va='top', fontfamily='sans-serif')

# Act 3: Brilliant ending (highlighted)
act3_start = act2_end
for i in range(6):
    x = act3_start + i * (timeline_end - act3_start) / 6
    ax.plot([x, x], [timeline_y - 60, timeline_y + 60],
           color=ending_purple, linewidth=6, alpha=0.8)
ax.text((act3_start + timeline_end) / 2, timeline_y - 90,
       'Act 3: BRILLIANT!',
       fontsize=28, color=ending_purple, weight='bold',
       ha='center', va='top', fontfamily='sans-serif')

# Mark the ending with star burst
ending_marker = plt.Circle((timeline_end, timeline_y), 50,
                          color=ending_purple, zorder=10)
ax.add_patch(ending_marker)
ax.text(timeline_end, timeline_y, '★',
       fontsize=60, color=soft_white, weight='bold',
       ha='center', va='center', fontfamily='sans-serif', zorder=11)

# Arrows showing ending rewrites memory
arrow_curve_x = np.linspace(timeline_end - 100, timeline_start + 300, 50)
arrow_curve_y = timeline_y + 150 - 0.0008 * (arrow_curve_x - timeline_end + 100)**2

ax.plot(arrow_curve_x, arrow_curve_y,
       color=memory_gold, linewidth=4, linestyle='--', alpha=0.7)
ax.annotate('', xy=(timeline_start + 250, timeline_y + 100),
           xytext=(timeline_end - 150, timeline_y + 150),
           arrowprops=dict(arrowstyle='->', lw=4, color=memory_gold))

ax.text(960, timeline_y + 200, 'The ending rewrites everything before it',
       fontsize=30, color=memory_gold, weight='bold', style='italic',
       ha='center', va='center', fontfamily='sans-serif')

# Your reaction leaving the theater
reaction_box = FancyBboxPatch((660, 280), 600, 120,
                             boxstyle="round,pad=15",
                             facecolor=ending_purple, alpha=0.3,
                             edgecolor=ending_purple, linewidth=3)
ax.add_patch(reaction_box)
ax.text(960, 340, '"That movie was GREAT!"',
       fontsize=40, color=soft_white, weight='bold',
       ha='center', va='center', fontfamily='sans-serif')

# Bottom insight
ax.text(960, 150, 'You walk out remembering the ending, not the boring hour before it',
       fontsize=28, color=soft_white,
       ha='center', va='center', fontfamily='sans-serif')

plt.tight_layout(pad=0)
plt.savefig('frame06_movies_example.png', dpi=100, bbox_inches='tight',
            pad_inches=0, facecolor=deep_indigo)
plt.close()
print("✅ Frame 6 created: Movies example")
