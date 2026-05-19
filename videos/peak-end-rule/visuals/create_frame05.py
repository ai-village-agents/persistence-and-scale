import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
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
ax.text(960, 1000, 'WHY YOUR BRAIN DOES THIS', 
        fontsize=56, color=soft_white, weight='bold',
        ha='center', va='top', fontfamily='sans-serif')

# Central brain visualization
brain_center_x = 960
brain_center_y = 600

# Draw simplified brain outline
brain_outline = plt.Circle((brain_center_x, brain_center_y), 220,
                          facecolor=deep_indigo, edgecolor=reality_blue,
                          linewidth=4, fill=False)
ax.add_patch(brain_outline)

# Two systems inside brain
# Left hemisphere: Experiencing Self (faded)
exp_x = brain_center_x - 100
ax.text(exp_x, brain_center_y + 50, 'Experiencing', 
        fontsize=24, color=fade_gray, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')
ax.text(exp_x, brain_center_y + 10, 'Self', 
        fontsize=24, color=fade_gray, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')
ax.text(exp_x, brain_center_y - 50, 'Lives every\nmoment', 
        fontsize=18, color=fade_gray, alpha=0.7,
        ha='center', va='center', fontfamily='sans-serif')

# Right hemisphere: Remembering Self (highlighted)
mem_x = brain_center_x + 100
ax.text(mem_x, brain_center_y + 50, 'Remembering', 
        fontsize=24, color=memory_gold, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')
ax.text(mem_x, brain_center_y + 10, 'Self', 
        fontsize=24, color=memory_gold, weight='bold',
        ha='center', va='center', fontfamily='sans-serif')
ax.text(mem_x, brain_center_y - 50, 'Tells the\nstory', 
        fontsize=18, color=memory_gold,
        ha='center', va='center', fontfamily='sans-serif')

# Three key insights around the brain
# Top: Evolution purpose
insight_top = FancyBboxPatch((brain_center_x - 300, 850), 600, 100,
                            boxstyle="round,pad=15",
                            facecolor=reality_blue, alpha=0.2,
                            edgecolor=reality_blue, linewidth=2)
ax.add_patch(insight_top)
ax.text(brain_center_x, 900, 'Your brain evolved to remember LESSONS, not archives',
       fontsize=30, color=soft_white, weight='bold',
       ha='center', va='center', fontfamily='sans-serif')

# Left: Peak tells you what's important
arrow_left = FancyArrowPatch((500, 600), (brain_center_x - 230, brain_center_y),
                            arrowstyle='->', mutation_scale=30,
                            linewidth=3, color=memory_gold)
ax.add_patch(arrow_left)

peak_box = FancyBboxPatch((180, 550), 300, 100,
                         boxstyle="round,pad=10",
                         facecolor=memory_gold, alpha=0.2,
                         edgecolor=memory_gold, linewidth=2)
ax.add_patch(peak_box)
ax.text(330, 600, 'PEAK tells you\nwhat matters',
       fontsize=26, color=memory_gold, weight='bold',
       ha='center', va='center', fontfamily='sans-serif')

# Right: End tells you the outcome
arrow_right = FancyArrowPatch((1420, 600), (brain_center_x + 230, brain_center_y),
                             arrowstyle='->', mutation_scale=30,
                             linewidth=3, color=ending_purple)
ax.add_patch(arrow_right)

end_box = FancyBboxPatch((1440, 550), 300, 100,
                        boxstyle="round,pad=10",
                        facecolor=ending_purple, alpha=0.2,
                        edgecolor=ending_purple, linewidth=2)
ax.add_patch(end_box)
ax.text(1590, 600, 'END tells you\nthe outcome',
       fontsize=26, color=ending_purple, weight='bold',
       ha='center', va='center', fontfamily='sans-serif')

# Bottom: Middle doesn't help
insight_bottom = FancyBboxPatch((brain_center_x - 320, 280), 640, 100,
                               boxstyle="round,pad=15",
                               facecolor=fade_gray, alpha=0.15,
                               edgecolor=fade_gray, linewidth=2)
ax.add_patch(insight_bottom)
ax.text(brain_center_x, 330, 'The middle doesn\'t help predict "Should I do this again?"',
       fontsize=28, color=fade_gray, style='italic',
       ha='center', va='center', fontfamily='sans-serif')

# Bottom key message
ax.text(960, 150, 'So your brain discards it',
       fontsize=32, color=soft_white, weight='bold',
       ha='center', va='center', fontfamily='sans-serif')

plt.tight_layout(pad=0)
plt.savefig('frame05_why_it_happens.png', dpi=100, bbox_inches='tight',
            pad_inches=0, facecolor=deep_indigo)
plt.close()
print("✅ Frame 5 created: Brain evolution explanation")
