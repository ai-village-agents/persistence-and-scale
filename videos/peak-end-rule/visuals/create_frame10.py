import matplotlib.pyplot as plt
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

# Central visual: Simple peak-end graph
center_x, center_y = 960, 620

# Draw timeline
timeline_left = 500
timeline_right = 1420
timeline_y = center_y

ax.plot([timeline_left, timeline_right], [timeline_y, timeline_y],
       color=fade_gray, linewidth=3, alpha=0.5)

# Draw experience curve (ups and downs)
x_points = np.linspace(timeline_left, timeline_right, 100)
# Create a wavy experience with a clear peak
experience_curve = (
    100 * np.sin(3 * (x_points - timeline_left) / (timeline_right - timeline_left)) +
    80 * np.sin(7 * (x_points - timeline_left) / (timeline_right - timeline_left)) +
    50
)
ax.plot(x_points, timeline_y + experience_curve, 
       color=fade_gray, linewidth=4, alpha=0.4)

# Mark the peak
peak_idx = np.argmax(experience_curve)
peak_x = x_points[peak_idx]
peak_y = timeline_y + experience_curve[peak_idx]
peak_circle = plt.Circle((peak_x, peak_y), 40, color=memory_gold, zorder=10)
ax.add_patch(peak_circle)
ax.text(peak_x, peak_y - 100, 'PEAK',
       fontsize=28, color=memory_gold, weight='bold',
       ha='center', va='bottom', fontfamily='sans-serif')

# Mark the end
end_x = timeline_right
end_y = timeline_y + experience_curve[-1]
end_circle = plt.Circle((end_x, end_y), 40, color=ending_purple, zorder=10)
ax.add_patch(end_circle)
ax.text(end_x, end_y - 100, 'END',
       fontsize=28, color=ending_purple, weight='bold',
       ha='center', va='bottom', fontfamily='sans-serif')

# Main closing message
ax.text(960, 340, 'Memory is not a recording.', 
        fontsize=58, color=soft_white, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

ax.text(960, 250, 'It\'s a story.', 
        fontsize=58, color=memory_gold, weight='bold',
        ha='center', va='center', fontfamily='sans-serif',
        style='italic')

# Channel name at bottom
ax.text(960, 120, 'PERSISTENCE & SCALE', 
        fontsize=40, color=soft_white, alpha=0.6,
        ha='center', va='center', fontfamily='sans-serif', weight='bold')

# Subtle subtitle
ax.text(960, 60, 'Subscribe for more cognitive insights', 
        fontsize=24, color=fade_gray, alpha=0.7,
        ha='center', va='center', fontfamily='sans-serif')

plt.tight_layout(pad=0)
plt.savefig('frame10_closing.png', dpi=100, bbox_inches='tight',
            pad_inches=0, facecolor=deep_indigo)
plt.close()
print("✅ Frame 10 created: Closing card")
