import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
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
ax.text(960, 1000, 'DESIGN BETTER EXPERIENCES', 
        fontsize=56, color=soft_white, weight='bold',
        ha='center', va='top', fontfamily='sans-serif')

# Two comparisons: BEFORE vs AFTER
left_center = 480
right_center = 1440
timeline_y = 650

# BEFORE: Flat/mediocre experience
ax.text(left_center, 900, 'BEFORE', 
        fontsize=44, color=fade_gray, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

ax.text(left_center, 840, 'Consistent Mediocrity', 
        fontsize=28, color=fade_gray, style='italic',
        ha='center', va='center', fontfamily='sans-serif')

# Draw flat timeline
before_x = np.linspace(left_center - 250, left_center + 250, 100)
before_quality = 80 + 15 * np.sin(10 * (before_x - (left_center - 250)) / 500)

ax.fill_between(before_x, timeline_y, timeline_y + before_quality,
                color=fade_gray, alpha=0.3)
ax.plot(before_x, timeline_y + before_quality, 
       color=fade_gray, linewidth=4)

# No memorable moments
ax.text(left_center, 520, 'No memorable peaks', 
        fontsize=26, color=fade_gray,
        ha='center', va='center', fontfamily='sans-serif')
ax.text(left_center, 470, 'Weak ending', 
        fontsize=26, color=fade_gray,
        ha='center', va='center', fontfamily='sans-serif')

# Memory result
memory_box_before = FancyBboxPatch((left_center - 160, 300), 320, 100,
                                   boxstyle="round,pad=10",
                                   facecolor=fade_gray, alpha=0.2,
                                   edgecolor=fade_gray, linewidth=3)
ax.add_patch(memory_box_before)
ax.text(left_center, 350, 'Forgettable', 
        fontsize=36, color=fade_gray, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# AFTER: Designed with peaks and strong ending
ax.text(right_center, 900, 'AFTER', 
        fontsize=44, color=memory_gold, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

ax.text(right_center, 840, 'Peaks + Strong Ending', 
        fontsize=28, color=memory_gold, style='italic',
        ha='center', va='center', fontfamily='sans-serif')

# Draw experience with clear peak and strong ending
after_x = np.linspace(right_center - 250, right_center + 250, 100)
# Create a curve with a dramatic peak and strong ending
after_quality = 60 + 100 * np.exp(-((after_x - (right_center - 50))**2) / 8000) + \
                80 * np.exp(-((after_x - (right_center + 230))**2) / 3000)

ax.fill_between(after_x, timeline_y, timeline_y + after_quality,
                color=memory_gold, alpha=0.3)
ax.plot(after_x, timeline_y + after_quality,
       color=memory_gold, linewidth=4)

# Mark the peak
peak_idx = np.argmax(after_quality)
peak_x = after_x[peak_idx]
peak_y = timeline_y + after_quality[peak_idx]
ax.plot([peak_x], [peak_y], 'o', color=memory_gold, markersize=25, zorder=10)
ax.text(peak_x, peak_y + 60, 'PEAK',
       fontsize=24, color=memory_gold, weight='bold',
       ha='center', va='bottom', fontfamily='sans-serif')

# Mark strong ending
end_x = after_x[-1]
end_y = timeline_y + after_quality[-1]
ax.plot([end_x], [end_y], 'o', color=ending_purple, markersize=25, zorder=10)
ax.text(end_x - 40, end_y + 60, 'Strong\nEND',
       fontsize=24, color=ending_purple, weight='bold',
       ha='center', va='bottom', fontfamily='sans-serif')

# Design notes
ax.text(right_center, 520, 'Memorable peak moments', 
        fontsize=26, color=memory_gold, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')
ax.text(right_center, 470, 'Strong closing impression', 
        fontsize=26, color=ending_purple, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# Memory result
memory_box_after = FancyBboxPatch((right_center - 160, 300), 320, 100,
                                  boxstyle="round,pad=10",
                                  facecolor=memory_gold, alpha=0.2,
                                  edgecolor=memory_gold, linewidth=3)
ax.add_patch(memory_box_after)
ax.text(right_center, 350, 'Memorable', 
        fontsize=36, color=memory_gold, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# Bottom insight
ax.text(960, 150, 'The last 5 minutes shape memory more than the first 55',
       fontsize=34, color=soft_white, style='italic',
       ha='center', va='center', fontfamily='sans-serif')

plt.tight_layout(pad=0)
plt.savefig('frame08_design_implication.png', dpi=100, bbox_inches='tight',
            pad_inches=0, facecolor=deep_indigo)
plt.close()
print("✅ Frame 8 created: Design implication visualization")
