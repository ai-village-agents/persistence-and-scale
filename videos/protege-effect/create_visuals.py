import os
from textwrap import dedent

import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.colors import LinearSegmentedColormap, to_rgba


COLORS = {
    "deep_teal": "#006B7D",
    "knowledge_gold": "#F4A300",
    "understanding_blue": "#3A86FF",
    "connection_purple": "#8338EC",
    "gap_red": "#FF006E",
    "clarity_white": "#FBFEF9",
}


plt.rcParams.update(
    {
        "text.kerning_factor": 6,
        "font.family": "DejaVu Sans",
    }
)


def setup_figure():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_facecolor(COLORS["deep_teal"])
    fig.patch.set_facecolor(COLORS["deep_teal"])
    return fig, ax


def frame_1(path):
    fig, ax = setup_figure()

    ax.text(
        0.5,
        0.6,
        "The Protégé Effect",
        color=COLORS["clarity_white"],
        fontsize=72,
        fontweight="bold",
        ha="center",
        va="center",
    )
    ax.text(
        0.5,
        0.45,
        "Learn By Teaching",
        color=COLORS["knowledge_gold"],
        fontsize=40,
        ha="center",
        va="center",
    )

    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)


def frame_2(path):
    fig, ax = setup_figure()

    levels = [
        ("Lecture: 5%", 0.85, 0.81),
        ("Reading: 10%", 0.81, 0.77),
        ("Demonstration: 30%", 0.77, 0.73),
        ("Discussion: 50%", 0.73, 0.69),
        ("Practice: 75%", 0.69, 0.65),
        ("Teaching Others: 90%", 0.75, 0.71),
    ]

    cmap = LinearSegmentedColormap.from_list(
        "blue_purple", [COLORS["understanding_blue"], COLORS["connection_purple"]]
    )

    start_y = 0.78
    height = 0.08
    for idx, (label, top_width, bottom_width) in enumerate(levels):
        y_top = start_y - idx * height
        y_bottom = y_top - height + (0.02 if idx == len(levels) - 1 else 0)
        left_top = 0.5 - top_width / 2
        right_top = 0.5 + top_width / 2
        left_bottom = 0.5 - bottom_width / 2
        right_bottom = 0.5 + bottom_width / 2

        if idx == len(levels) - 1:
            face_color = COLORS["knowledge_gold"]
            edge_color = COLORS["clarity_white"]
            lw = 4
        else:
            face_color = cmap(idx / (len(levels) - 1))
            edge_color = to_rgba(COLORS["clarity_white"], 0.6)
            lw = 2

        trapezoid = patches.Polygon(
            [
                (left_top, y_top),
                (right_top, y_top),
                (right_bottom, y_bottom),
                (left_bottom, y_bottom),
            ],
            closed=True,
            linewidth=lw,
            edgecolor=edge_color,
            facecolor=face_color,
        )
        ax.add_patch(trapezoid)

        label_x = min(left_top, left_bottom) - 0.06
        label_x = max(label_x, 0.05)
        text_color = COLORS["knowledge_gold"] if idx == len(levels) - 1 else COLORS["clarity_white"]
        font_weight = "bold" if idx == len(levels) - 1 else "normal"

        ax.text(
            label_x,
            (y_top + y_bottom) / 2,
            label,
            color=text_color,
            fontsize=28,
            ha="right",
            va="center",
            fontweight=font_weight,
        )

    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)


def frame_3(path):
    fig, ax = setup_figure()

    centers = [
        (0.5, 0.75, "Learn", COLORS["understanding_blue"]),
        (0.75, 0.5, "Teach", COLORS["knowledge_gold"]),
        (0.5, 0.25, "Understand\nDeeply", COLORS["connection_purple"]),
        (0.25, 0.5, "Learn More", COLORS["understanding_blue"]),
    ]

    for x, y, label, color in centers:
        box = patches.FancyBboxPatch(
            (x - 0.12, y - 0.065),
            0.24,
            0.13,
            boxstyle="round,pad=0.02",
            linewidth=0,
            facecolor=color,
        )
        ax.add_patch(box)
        ax.text(
            x,
            y,
            label,
            color=COLORS["clarity_white"],
            fontsize=28,
            ha="center",
            va="center",
        )

    arrow_pairs = [
        (centers[0], centers[1]),
        (centers[1], centers[2]),
        (centers[2], centers[3]),
        (centers[3], centers[0]),
    ]

    for (x0, y0, *_), (x1, y1, *_) in arrow_pairs:
        arrow = patches.FancyArrowPatch(
            (x0, y0),
            (x1, y1),
            connectionstyle="arc3,rad=-0.3",
            arrowstyle="-|>",
            mutation_scale=30,
            linewidth=6,
            color=COLORS["clarity_white"],
        )
        ax.add_patch(arrow)

    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)


def frame_4(path):
    fig, ax = setup_figure()

    brain_path = patches.Path(
        [
            (0.5, 0.78),
            (0.66, 0.73),
            (0.75, 0.62),
            (0.74, 0.47),
            (0.68, 0.35),
            (0.54, 0.32),
            (0.46, 0.33),
            (0.32, 0.35),
            (0.26, 0.47),
            (0.25, 0.62),
            (0.34, 0.73),
            (0.5, 0.78),
        ],
        [
            patches.Path.MOVETO,
            patches.Path.CURVE3,
            patches.Path.CURVE3,
            patches.Path.CURVE3,
            patches.Path.CURVE3,
            patches.Path.CURVE3,
            patches.Path.CURVE3,
            patches.Path.CURVE3,
            patches.Path.CURVE3,
            patches.Path.CURVE3,
            patches.Path.CURVE3,
            patches.Path.CLOSEPOLY,
        ],
    )
    brain_outline = patches.PathPatch(
        brain_path,
        edgecolor=COLORS["clarity_white"],
        facecolor="none",
        linewidth=6,
    )
    ax.add_patch(brain_outline)

    ax.plot(
        [0.43, 0.57],
        [0.74, 0.74],
        color=COLORS["clarity_white"],
        linewidth=3,
    )
    ax.plot(
        [0.41, 0.59],
        [0.62, 0.62],
        color=COLORS["clarity_white"],
        linewidth=3,
    )

    nodes = [
        (0.45, 0.69),
        (0.55, 0.68),
        (0.6, 0.57),
        (0.48, 0.56),
        (0.36, 0.52),
        (0.42, 0.44),
        (0.58, 0.45),
        (0.64, 0.5),
    ]
    connections = [
        (0, 1),
        (1, 2),
        (1, 3),
        (3, 4),
        (3, 5),
        (2, 6),
        (6, 7),
        (4, 5),
        (2, 7),
    ]

    for i, j in connections:
        x0, y0 = nodes[i]
        x1, y1 = nodes[j]
        ax.plot(
            [x0, x1],
            [y0, y1],
            color=COLORS["connection_purple"],
            linewidth=3,
            alpha=0.8,
        )

    for idx, (x, y) in enumerate(nodes):
        color = COLORS["knowledge_gold"] if idx % 2 == 0 else COLORS["connection_purple"]
        node = patches.Circle((x, y), radius=0.017, facecolor=color, edgecolor=COLORS["clarity_white"], linewidth=1.5)
        ax.add_patch(node)

    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)


def frame_5(path):
    fig, ax = setup_figure()

    # Teacher figure
    ax.add_patch(patches.Circle((0.3, 0.65), 0.05, facecolor=COLORS["knowledge_gold"], edgecolor="none"))
    ax.plot([0.3, 0.3], [0.6, 0.45], color=COLORS["knowledge_gold"], linewidth=6)
    ax.plot([0.3, 0.24], [0.57, 0.5], color=COLORS["knowledge_gold"], linewidth=6)
    ax.plot([0.3, 0.36], [0.57, 0.5], color=COLORS["knowledge_gold"], linewidth=6)
    ax.plot([0.3, 0.26], [0.45, 0.35], color=COLORS["knowledge_gold"], linewidth=6)
    ax.plot([0.3, 0.34], [0.45, 0.35], color=COLORS["knowledge_gold"], linewidth=6)
    ax.text(0.3, 0.32, "", color=COLORS["clarity_white"])

    # Listener figure
    ax.add_patch(patches.Circle((0.7, 0.65), 0.05, facecolor=COLORS["clarity_white"], edgecolor="none"))
    ax.plot([0.7, 0.7], [0.6, 0.45], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.7, 0.64], [0.57, 0.5], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.7, 0.76], [0.57, 0.5], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.7, 0.66], [0.45, 0.35], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.7, 0.74], [0.45, 0.35], color=COLORS["clarity_white"], linewidth=6)

    # Speech lines
    ax.plot([0.38, 0.62], [0.6, 0.7], color=COLORS["clarity_white"], linewidth=2, alpha=0.6)
    ax.plot([0.38, 0.62], [0.55, 0.65], color=COLORS["clarity_white"], linewidth=2, alpha=0.6)

    # Lightbulb
    bulb = patches.Circle((0.3, 0.78), 0.04, facecolor=COLORS["understanding_blue"], edgecolor=COLORS["clarity_white"], linewidth=2)
    ax.add_patch(bulb)
    ax.plot([0.3, 0.3], [0.74, 0.71], color=COLORS["understanding_blue"], linewidth=4)
    ax.plot([0.28, 0.32], [0.71, 0.71], color=COLORS["clarity_white"], linewidth=2)
    ax.plot([0.28, 0.32], [0.7, 0.7], color=COLORS["clarity_white"], linewidth=2)

    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)


def frame_6(path):
    fig, ax = setup_figure()

    # Desk and paper
    ax.plot([0.2, 0.8], [0.35, 0.35], color=COLORS["clarity_white"], linewidth=6)
    ax.add_patch(patches.Rectangle((0.45, 0.35), 0.12, 0.18, facecolor=COLORS["clarity_white"], edgecolor="none", alpha=0.2))

    # Stick figure
    ax.add_patch(patches.Circle((0.35, 0.62), 0.05, facecolor=COLORS["clarity_white"], edgecolor="none"))
    ax.plot([0.35, 0.35], [0.57, 0.4], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.35, 0.3], [0.52, 0.45], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.35, 0.4], [0.52, 0.45], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.35, 0.32], [0.4, 0.3], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.35, 0.38], [0.4, 0.3], color=COLORS["clarity_white"], linewidth=6)

    # Thought bubbles
    left_bubble = patches.Ellipse((0.55, 0.7), 0.18, 0.12, facecolor=to_rgba(COLORS["gap_red"], 0.8), edgecolor=COLORS["clarity_white"], linewidth=3)
    right_bubble = patches.Ellipse((0.78, 0.7), 0.2, 0.14, facecolor=to_rgba(COLORS["knowledge_gold"], 0.85), edgecolor=COLORS["clarity_white"], linewidth=3)
    ax.add_patch(left_bubble)
    ax.add_patch(right_bubble)

    ax.text(
        0.55,
        0.7,
        "???",
        color=COLORS["clarity_white"],
        fontsize=36,
        ha="center",
        va="center",
    )
    ax.text(
        0.78,
        0.7,
        "Aha!",
        color=COLORS["deep_teal"],
        fontsize=34,
        ha="center",
        va="center",
        fontweight="bold",
    )

    # Bubble connectors
    ax.plot([0.5, 0.45], [0.62, 0.58], color=COLORS["clarity_white"], linewidth=3)
    ax.plot([0.7, 0.45], [0.62, 0.58], color=COLORS["clarity_white"], linewidth=3)

    ax.text(
        0.66,
        0.56,
        "clarify",
        color=COLORS["knowledge_gold"],
        fontsize=24,
        ha="center",
        va="center",
    )

    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)


def frame_7(path):
    fig, ax = setup_figure()

    # Desk
    ax.plot([0.2, 0.8], [0.35, 0.35], color=COLORS["clarity_white"], linewidth=6)

    # Person
    ax.add_patch(patches.Circle((0.3, 0.65), 0.05, facecolor=COLORS["clarity_white"], edgecolor="none"))
    ax.plot([0.3, 0.3], [0.6, 0.45], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.3, 0.26], [0.55, 0.48], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.3, 0.34], [0.55, 0.48], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.3, 0.27], [0.45, 0.35], color=COLORS["clarity_white"], linewidth=6)
    ax.plot([0.3, 0.33], [0.45, 0.35], color=COLORS["clarity_white"], linewidth=6)

    # Computer
    ax.add_patch(patches.Rectangle((0.42, 0.45), 0.08, 0.11, facecolor=COLORS["clarity_white"], edgecolor="none"))
    ax.add_patch(patches.Rectangle((0.44, 0.35), 0.04, 0.1, facecolor=COLORS["clarity_white"], edgecolor="none"))

    # Rubber duck
    duck_body = patches.Ellipse((0.55, 0.42), 0.08, 0.05, facecolor=COLORS["knowledge_gold"], edgecolor=COLORS["clarity_white"], linewidth=2)
    duck_head = patches.Circle((0.59, 0.46), 0.025, facecolor=COLORS["knowledge_gold"], edgecolor=COLORS["clarity_white"], linewidth=2)
    ax.add_patch(duck_body)
    ax.add_patch(duck_head)
    ax.add_patch(patches.Polygon([(0.61, 0.45), (0.64, 0.45), (0.61, 0.43)], facecolor=COLORS["gap_red"], edgecolor=COLORS["clarity_white"], linewidth=1))

    # Lightbulb
    bulb = patches.Circle((0.7, 0.72), 0.05, facecolor=COLORS["understanding_blue"], edgecolor=COLORS["clarity_white"], linewidth=3)
    ax.add_patch(bulb)
    ax.plot([0.7, 0.7], [0.67, 0.62], color=COLORS["knowledge_gold"], linewidth=5)
    ax.plot([0.67, 0.73], [0.62, 0.62], color=COLORS["clarity_white"], linewidth=3)

    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)


def frame_8(path):
    fig, ax = setup_figure()

    # Water line
    ax.plot([0.1, 0.9], [0.55, 0.55], color=to_rgba(COLORS["clarity_white"], 0.6), linewidth=3)

    iceberg_top = patches.Polygon(
        [(0.45, 0.55), (0.5, 0.7), (0.55, 0.55)],
        closed=True,
        facecolor=to_rgba(COLORS["clarity_white"], 0.2),
        edgecolor=COLORS["clarity_white"],
        linewidth=3,
    )
    iceberg_bottom = patches.Polygon(
        [(0.45, 0.55), (0.3, 0.25), (0.5, 0.1), (0.7, 0.25), (0.55, 0.55)],
        closed=True,
        facecolor=to_rgba(COLORS["connection_purple"], 0.35),
        edgecolor=COLORS["clarity_white"],
        linewidth=3,
    )
    ax.add_patch(iceberg_top)
    ax.add_patch(iceberg_bottom)

    ax.text(
        0.5,
        0.62,
        "Teaching Others",
        color=COLORS["knowledge_gold"],
        fontsize=32,
        ha="center",
        va="center",
        fontweight="bold",
    )
    ax.text(
        0.5,
        0.28,
        "Your Understanding Deepens",
        color=COLORS["clarity_white"],
        fontsize=30,
        ha="center",
        va="center",
    )

    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)


def frame_9(path):
    fig, ax = setup_figure()

    panel_height = 0.22
    start_y = 0.78
    instructions = dedent(
        """1. Notice: What can't you explain simply?
2. Create: Find teaching opportunities
3. Teach to learn: Make teaching your learning method"""
    ).splitlines()

    for idx, text in enumerate(instructions):
        y = start_y - idx * (panel_height + 0.04)
        panel = patches.FancyBboxPatch(
            (0.2, y - panel_height),
            0.6,
            panel_height,
            boxstyle="round,pad=0.025",
            linewidth=2,
            edgecolor=to_rgba(COLORS["clarity_white"], 0.9),
            facecolor=to_rgba(COLORS["clarity_white"], 0.08),
        )
        ax.add_patch(panel)

        number, message = text.split(" ", 1)
        ax.text(
            0.24,
            y - panel_height / 2,
            number,
            color=COLORS["knowledge_gold"],
            fontsize=36,
            fontweight="bold",
            ha="left",
            va="center",
        )
        ax.text(
            0.3,
            y - panel_height / 2,
            message,
            color=COLORS["clarity_white"],
            fontsize=26,
            ha="left",
            va="center",
        )

    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)


def frame_10(path):
    fig, ax = setup_figure()

    loop_arrow = patches.FancyArrowPatch(
        (0.65, 0.5),
        (0.35, 0.5),
        connectionstyle="arc3,rad=0.7",
        arrowstyle="-|>",
        mutation_scale=60,
        linewidth=10,
        color=COLORS["knowledge_gold"],
    )
    ax.add_patch(loop_arrow)
    loop_arrow_back = patches.FancyArrowPatch(
        (0.35, 0.5),
        (0.65, 0.5),
        connectionstyle="arc3,rad=0.7",
        arrowstyle="-|>",
        mutation_scale=60,
        linewidth=10,
        color=COLORS["knowledge_gold"],
    )
    ax.add_patch(loop_arrow_back)

    ax.text(
        0.5,
        0.5,
        "Keep the cycle going",
        color=COLORS["clarity_white"],
        fontsize=40,
        ha="center",
        va="center",
        fontweight="bold",
    )

    ax.text(
        0.5,
        0.22,
        "PERSISTENCE & SCALE",
        color=COLORS["understanding_blue"],
        fontsize=36,
        ha="center",
        va="center",
        fontweight="bold",
    )

    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)


def main():
    os.makedirs("visuals", exist_ok=True)
    generators = [
        frame_1,
        frame_2,
        frame_3,
        frame_4,
        frame_5,
        frame_6,
        frame_7,
        frame_8,
        frame_9,
        frame_10,
    ]

    for idx, generator in enumerate(generators, start=1):
        filename = f"visuals/frame{idx:02d}.png"
        generator(filename)
        print(f"Saved {filename}")


if __name__ == "__main__":
    main()
