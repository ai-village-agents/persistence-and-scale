import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Color palette
deep_navy = '#1a2332'
mechanical_silver = '#c0c8d1'
forward_green = '#4CAF50'
lock_red = '#e74c3c'
neural_gold = '#f9a825'
soft_white = '#f5f5f5'
understanding_blue = '#5D9CEC'

fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor=deep_navy)
ax.set_xlim(0, 1920)
ax.set_ylim(0, 1080)
ax.axis('off')

# Title at top
ax.text(960, 980, 'THREE STEPS TO USE THE RATCHET EFFECT', 
        fontsize=48, color=soft_white, weight='bold', ha='center', va='top',
        fontfamily='sans-serif')

# Three vertical panels
panel_width = 500
panel_height = 650
panel_y_bottom = 150
spacing = 100

colors = [forward_green, neural_gold, understanding_blue]
steps = [
    ('1', 'Notice:', 'What can\'t you\nunsee?'),
    ('2', 'Choose:', 'What\'s worth\nmaking permanent?'),
    ('3', 'Trust:', 'Small clicks\ncompound')
]

x_positions = [
    960 - panel_width - spacing,  # Left panel
    960 - panel_width // 2,       # Center panel
    960 + spacing                  # Right panel
]

for i, (x_center, color, (number, title, subtitle)) in enumerate(zip(x_positions, colors, steps)):
    # Panel background
    panel = FancyBboxPatch(
        (x_center - panel_width//2, panel_y_bottom),
        panel_width, panel_height,
        boxstyle="round,pad=20",
        facecolor=deep_navy,
        edgecolor=color,
        linewidth=4,
        alpha=0.9
    )
    ax.add_patch(panel)
    
    # Number circle
    circle = plt.Circle((x_center, panel_y_bottom + panel_height - 100),
                       60, color=color, zorder=10)
    ax.add_patch(circle)
    ax.text(x_center, panel_y_bottom + panel_height - 100,
           number, fontsize=72, color=deep_navy, weight='bold',
           ha='center', va='center', fontfamily='sans-serif', zorder=11)
    
    # Title
    ax.text(x_center, panel_y_bottom + panel_height - 250,
           title, fontsize=44, color=color, weight='bold',
           ha='center', va='center', fontfamily='sans-serif')
    
    # Subtitle
    ax.text(x_center, panel_y_bottom + panel_height - 450,
           subtitle, fontsize=32, color=soft_white,
           ha='center', va='center', fontfamily='sans-serif',
           linespacing=1.6)

plt.tight_layout(pad=0)
plt.savefig('frame09_three_step_takeaway.png', dpi=100, bbox_inches='tight', 
            pad_inches=0, facecolor=deep_navy)
plt.close()
print("✅ Frame 9 created: 3-step takeaway")
