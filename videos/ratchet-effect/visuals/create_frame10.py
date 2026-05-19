import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Color palette
deep_navy = '#1a2332'
mechanical_silver = '#c0c8d1'
forward_green = '#4CAF50'
soft_white = '#f5f5f5'

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=deep_navy)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

# Central ratchet wheel (simplified, elegant)
center_x, center_y = 960, 600
outer_radius = 200
inner_radius = 100
num_teeth = 12

# Draw ratchet wheel
theta = np.linspace(0, 2*np.pi, num_teeth*2+1)
for i in range(num_teeth):
    angle1 = theta[2*i]
    angle2 = theta[2*i+1]
    
    # Outer tooth
    x_outer1 = center_x + outer_radius * np.cos(angle1)
    y_outer1 = center_y + outer_radius * np.sin(angle1)
    x_outer2 = center_x + outer_radius * np.cos(angle2)
    y_outer2 = center_y + outer_radius * np.sin(angle2)
    
    # Inner base
    x_inner1 = center_x + inner_radius * np.cos(angle1)
    y_inner1 = center_y + inner_radius * np.sin(angle1)
    x_inner2 = center_x + inner_radius * np.cos(angle2)
    y_inner2 = center_y + inner_radius * np.sin(angle2)
    
    # Draw tooth
    tooth = plt.Polygon([
        [x_inner1, y_inner1],
        [x_outer1, y_outer1],
        [x_outer2, y_outer2],
        [x_inner2, y_inner2]
    ], facecolor=mechanical_silver, edgecolor=soft_white, linewidth=2)
    ax.add_patch(tooth)

# Center circle
center_circle = plt.Circle((center_x, center_y), inner_radius-10,
                          facecolor=deep_navy, edgecolor=mechanical_silver, linewidth=3)
ax.add_patch(center_circle)

# Forward arrow
arrow_y = center_y - 50
ax.arrow(center_x + 250, arrow_y, 100, 0,
        head_width=30, head_length=30, fc=forward_green, ec=forward_green,
        linewidth=3)

# Main quote
ax.text(960, 300, 'Progress you can\'t undo.', 
        fontsize=56, color=soft_white, weight='bold',
        ha='center', va='center', fontfamily='sans-serif',
        style='italic')

# Channel name at bottom
ax.text(960, 120, 'PERSISTENCE & SCALE', 
        fontsize=40, color=mechanical_silver, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# Subtle subtitle
ax.text(960, 60, 'Subscribe for more cognitive insights', 
        fontsize=24, color=mechanical_silver, alpha=0.7,
        ha='center', va='center', fontfamily='sans-serif')

plt.tight_layout(pad=0)
plt.savefig('frame10_closing.png', dpi=100, bbox_inches='tight',
            pad_inches=0, facecolor=deep_navy)
plt.close()
print("✅ Frame 10 created: Closing card")
