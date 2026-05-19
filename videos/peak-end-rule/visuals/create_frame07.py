import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

# Color palette
deep_indigo = '#2c3e60'
memory_gold = '#f39c12'
ending_purple = '#9b59b6'
fade_gray = '#95a5a6'
story_red = '#e74c3c'
soft_white = '#ecf0f1'

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=deep_indigo)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

# Title
ax.text(960, 1000, 'EXAMPLE: RELATIONSHIPS', 
        fontsize=56, color=soft_white, weight='bold',
        ha='center', va='top', fontfamily='sans-serif')

# Relationship timeline
timeline_y = 600
timeline_start = 250
timeline_end = 1670
timeline_length = timeline_end - timeline_start

# Draw timeline bar (representing years)
ax.plot([timeline_start, timeline_end], [timeline_y, timeline_y],
       color=fade_gray, linewidth=6, alpha=0.4)

# Everyday mundane moments (many faded dots)
num_days = 80
for i in range(num_days):
    x = timeline_start + (i / num_days) * timeline_length
    y_jitter = timeline_y + np.random.randint(-30, 30)
    ax.plot([x], [y_jitter], 'o', color=fade_gray, markersize=4, alpha=0.2)

ax.text(960, timeline_y - 120, 'Years of daily mundane moments',
       fontsize=28, color=fade_gray, alpha=0.6, style='italic',
       ha='center', va='top', fontfamily='sans-serif')

# Peak moments (highlighted with gold)
peak_moments = [
    (0.25, 'Amazing\ntrip', 150),
    (0.55, 'Crisis\nhandled\ntogether', 170),
    (0.75, 'Special\nanniversary', 150),
]

for position, label, offset in peak_moments:
    x = timeline_start + position * timeline_length
    # Large gold marker
    peak_circle = Circle((x, timeline_y), 35, color=memory_gold, zorder=10)
    ax.add_patch(peak_circle)
    ax.text(x, timeline_y + offset, label,
           fontsize=24, color=memory_gold, weight='bold',
           ha='center', va='bottom', fontfamily='sans-serif')

# The ending - breakup (red X)
end_x = timeline_end
end_marker = Circle((end_x, timeline_y), 45, color=story_red, zorder=10)
ax.add_patch(end_marker)
ax.text(end_x, timeline_y, '✗',
       fontsize=70, color=soft_white, weight='bold',
       ha='center', va='center', fontfamily='sans-serif', zorder=11)
ax.text(end_x, timeline_y - 100, 'Breakup',
       fontsize=28, color=story_red, weight='bold',
       ha='center', va='top', fontfamily='sans-serif')

# Visual effect: ending colors the whole timeline
# Draw red tint overlay showing ending rewriting history
overlay_start = timeline_start - 50
overlay_end = timeline_end
ax.fill_between([overlay_start, overlay_end], 
               [timeline_y - 200, timeline_y - 200],
               [timeline_y + 200, timeline_y + 200],
               color=story_red, alpha=0.08)

# Arrow showing ending's power
ax.annotate('', xy=(timeline_start + 200, timeline_y + 80),
           xytext=(end_x - 100, timeline_y + 80),
           arrowprops=dict(arrowstyle='<-', lw=4, color=story_red, linestyle='--'))
ax.text(960, timeline_y + 130, 'The ending rewrites the entire history',
       fontsize=30, color=story_red, weight='bold', style='italic',
       ha='center', va='bottom', fontfamily='sans-serif')

# Memory assessment boxes
# Top: What matters to memory
memory_matters = FancyBboxPatch((300, 780), 1320, 90,
                               boxstyle="round,pad=10",
                               facecolor=memory_gold, alpha=0.2,
                               edgecolor=memory_gold, linewidth=2)
ax.add_patch(memory_matters)
ax.text(960, 825, 'What Memory Keeps: A handful of peak experiences + How it ended',
       fontsize=28, color=memory_gold, weight='bold',
       ha='center', va='center', fontfamily='sans-serif')

# Bottom insight
insight_box = FancyBboxPatch((400, 320), 1120, 100,
                            boxstyle="round,pad=15",
                            facecolor=ending_purple, alpha=0.2,
                            edgecolor=ending_purple, linewidth=2)
ax.add_patch(insight_box)
ax.text(960, 370, 'Endings have disproportionate power over memory',
       fontsize=34, color=soft_white, weight='bold',
       ha='center', va='center', fontfamily='sans-serif')

plt.tight_layout(pad=0)
plt.savefig('frame07_relationships_example.png', dpi=100, bbox_inches='tight',
            pad_inches=0, facecolor=deep_indigo)
plt.close()
print("✅ Frame 7 created: Relationships example")
