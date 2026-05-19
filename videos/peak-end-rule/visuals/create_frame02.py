import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
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

# Title question
ax.text(960, 980, 'YOUR BEST VACATION...', 
        fontsize=60, color=soft_white, weight='bold',
        ha='center', va='top', fontfamily='sans-serif')

# Left side: MEMORY (glowing, positive)
left_center = 480
ax.text(left_center, 800, 'WHAT YOU REMEMBER', 
        fontsize=36, color=memory_gold, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# Memory highlights - just the good moments
memory_items = [
    ('🏖️', 'Beautiful beach\nsunset', 680),
    ('🎉', 'Amazing dinner\non last night', 520),
    ('✨', 'One perfect\nmoment', 360),
]

for emoji, text, y in memory_items:
    # Gold glow box
    glow = FancyBboxPatch((left_center - 140, y - 60), 280, 100,
                         boxstyle="round,pad=10",
                         facecolor=memory_gold, alpha=0.2,
                         edgecolor=memory_gold, linewidth=2)
    ax.add_patch(glow)
    ax.text(left_center, y, f'{emoji} {text}',
           fontsize=28, color=soft_white,
           ha='center', va='center', fontfamily='sans-serif')

ax.text(left_center, 200, '"It was amazing!"',
       fontsize=34, color=memory_gold, weight='bold', style='italic',
       ha='center', va='center', fontfamily='sans-serif')

# Right side: REALITY (faded, mixed)
right_center = 1440
ax.text(right_center, 800, 'WHAT ACTUALLY HAPPENED', 
        fontsize=36, color=reality_blue, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')

# Reality - many moments, mostly mundane/negative
reality_items = [
    ('✈️', 'Travel delays', 720, 0.3),
    ('🏖️', 'Beach sunset', 680, 1.0),  # The one good moment
    ('😓', 'Sunburn', 640, 0.3),
    ('🚗', 'Long drives', 600, 0.3),
    ('💤', 'Jet lag', 560, 0.3),
    ('⏳', 'Waiting around', 520, 0.3),
    ('🍽️', 'Mediocre meals', 480, 0.3),
    ('🎉', 'Great final dinner', 440, 1.0),  # The other good moment
    ('😫', 'Arguments', 400, 0.3),
    ('📱', 'Lost luggage stress', 360, 0.3),
]

for emoji, text, y, alpha in reality_items:
    color = reality_blue if alpha == 1.0 else fade_gray
    box_alpha = 0.2 if alpha == 1.0 else 0.1
    
    box = FancyBboxPatch((right_center - 140, y - 30), 280, 55,
                        boxstyle="round,pad=5",
                        facecolor=color, alpha=box_alpha,
                        edgecolor=color, linewidth=1)
    ax.add_patch(box)
    ax.text(right_center, y, f'{emoji} {text}',
           fontsize=22, color=soft_white, alpha=alpha,
           ha='center', va='center', fontfamily='sans-serif')

ax.text(right_center, 200, 'Hours of boredom + discomfort',
       fontsize=28, color=fade_gray, style='italic',
       ha='center', va='center', fontfamily='sans-serif')

# Central question at bottom
ax.text(960, 80, 'Why does memory feel so different from reality?',
       fontsize=38, color=soft_white, weight='bold',
       ha='center', va='center', fontfamily='sans-serif')

plt.tight_layout(pad=0)
plt.savefig('frame02_hook.png', dpi=100, bbox_inches='tight',
            pad_inches=0, facecolor=deep_indigo)
plt.close()
print("✅ Frame 2 created: Vacation paradox hook")
