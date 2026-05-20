import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrow, Polygon, Rectangle


PALETTE = {
    "navy": "#0C1B33",
    "gold": "#FFB627",
    "gray": "#6B7280",
    "blue": "#3B82F6",
    "green": "#10B981",
}

OUTPUT_DIR = "visuals"


def make_canvas():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_facecolor(PALETTE["navy"])
    ax.axis("off")
    return fig, ax


def save_frame(name, draw_fn):
    fig, ax = make_canvas()
    draw_fn(fig, ax)
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, facecolor=PALETTE["navy"])
    plt.close(fig)


def draw_frame1(fig, ax):
    ax.text(
        0.5,
        0.5,
        "THE SPACING EFFECT",
        color=PALETTE["gold"],
        fontsize=120,
        ha="center",
        va="center",
        fontweight="bold",
    )


def draw_frame2(fig, ax):
    ax.text(0.13, 0.78, "CRAMMING", color=PALETTE["gold"], fontsize=42, fontweight="bold")
    ax.text(0.13, 0.42, "SPACING", color=PALETTE["gold"], fontsize=42, fontweight="bold")

    # Cramming timeline
    ax.plot([0.15, 0.85], [0.68, 0.68], color=PALETTE["gray"], linewidth=6, alpha=0.5)
    for i in range(6):
        x = 0.2 + i * 0.08
        ax.add_patch(
            Rectangle(
                (x, 0.62),
                0.05,
                0.12,
                facecolor=PALETTE["gray"],
                edgecolor="none",
                alpha=0.8,
            )
        )

    # Spacing timeline
    ax.plot([0.15, 0.85], [0.32, 0.32], color=PALETTE["blue"], linewidth=6, alpha=0.5)
    spacing_positions = [0.22, 0.4, 0.6, 0.82]
    widths = [0.05, 0.05, 0.05, 0.05]
    for x, w in zip(spacing_positions, widths):
        ax.add_patch(
            Rectangle(
                (x, 0.26),
                w,
                0.12,
                facecolor=PALETTE["blue"],
                edgecolor="none",
            )
        )

    for x in spacing_positions:
        ax.annotate(
            "",
            xy=(x + 0.025, 0.52),
            xytext=(x + 0.025, 0.36),
            arrowprops=dict(arrowstyle="-", color=PALETTE["blue"], linewidth=2),
        )


def draw_frame3(fig, ax):
    # Silhouette
    head = Circle((0.3, 0.6), 0.08, facecolor=PALETTE["gray"], edgecolor="none", alpha=0.9)
    ax.add_patch(head)
    body = Polygon(
        [(0.25, 0.22), (0.35, 0.22), (0.38, 0.5), (0.22, 0.5)],
        closed=True,
        facecolor=PALETTE["gray"],
        edgecolor="none",
        alpha=0.9,
    )
    ax.add_patch(body)

    ax.text(0.3, 0.16, "Hermann Ebbinghaus", color=PALETTE["gold"], fontsize=40, ha="center")
    ax.text(0.3, 0.1, "1885", color=PALETTE["gold"], fontsize=36, ha="center")

    inset = fig.add_axes([0.62, 0.48, 0.28, 0.32])
    inset.set_facecolor(PALETTE["navy"])
    t = np.linspace(0, 1.2, 200)
    inset.plot(t, np.exp(-3 * t), color=PALETTE["gold"], linewidth=4)
    inset.set_title("Forgetting Curve", color=PALETTE["gray"], fontsize=22, pad=12)
    inset.tick_params(colors=PALETTE["gray"], labelsize=14)
    for spine in inset.spines.values():
        spine.set_color(PALETTE["gray"])
    inset.set_xlabel("Time", color=PALETTE["gray"], fontsize=16)
    inset.set_ylabel("Memory", color=PALETTE["gray"], fontsize=16)


def draw_frame4(fig, ax):
    inset = fig.add_axes([0.1, 0.18, 0.8, 0.64])
    inset.set_facecolor(PALETTE["navy"])
    inset.tick_params(colors=PALETTE["gray"], labelsize=16)
    for spine in inset.spines.values():
        spine.set_color(PALETTE["gray"])

    t = np.linspace(0, 1, 200)
    curves = [
        (np.exp(-3 * t), 0.0),
        (0.6 * np.exp(-3 * t) + 0.35, 0.2),
        (0.55 * np.exp(-3 * t) + 0.5, 0.4),
    ]
    colors = [PALETTE["gray"], PALETTE["blue"], PALETTE["gold"]]
    for idx, (base_curve, shift) in enumerate(curves):
        y = base_curve + shift
        inset.plot(t, y, color=colors[idx], linewidth=4)
        retrieval_points = [0.15, 0.4, 0.7]
        for rp in retrieval_points[: idx + 1]:
            inset.scatter(
                [rp],
                [np.interp(rp, t, y)],
                color=PALETTE["green"],
                s=160,
                zorder=5,
            )

    inset.set_xlabel("Time", color=PALETTE["gray"], fontsize=20)
    inset.set_ylabel("Memory Strength", color=PALETTE["gray"], fontsize=20)
    inset.set_ylim(0, 1.2)


def draw_frame5(fig, ax):
    inset = fig.add_axes([0.08, 0.2, 0.84, 0.6])
    inset.set_facecolor(PALETTE["navy"])
    inset.tick_params(colors=PALETTE["gray"], labelsize=18)
    for spine in inset.spines.values():
        spine.set_color(PALETTE["gray"])

    x = np.linspace(0, 1, 200)
    cramming = np.exp(-6 * x) + 0.05
    spacing = 0.6 * np.exp(-4 * x) + 0.35 * (1 - np.exp(-3 * x))
    inset.plot(x, cramming, color=PALETTE["gray"], linewidth=4, label="Cramming")
    inset.plot(x, spacing, color=PALETTE["blue"], linewidth=4, label="Spacing")
    inset.fill_between(x, 0, spacing, color=PALETTE["blue"], alpha=0.12)
    inset.fill_between(x, 0, cramming, color=PALETTE["gray"], alpha=0.12)

    points = [0, 0.3, 0.55, 0.85]
    labels = ["Immediate", "1 week", "1 month", "3 months"]
    for p, label in zip(points, labels):
        inset.axvline(p, color=PALETTE["gray"], linestyle="--", linewidth=1.5, alpha=0.5)
        inset.text(p, -0.05, label, color=PALETTE["gray"], fontsize=18, ha="center", va="top")

    inset.legend(loc="upper right", frameon=False, fontsize=20, labelcolor=PALETTE["gray"])
    inset.set_ylim(0, 1.1)
    inset.set_xlim(0, 0.9)


def draw_frame6(fig, ax):
    # Brain outline using polygon
    brain_outline = [
        (0.5, 0.75),
        (0.62, 0.72),
        (0.72, 0.62),
        (0.76, 0.5),
        (0.72, 0.36),
        (0.6, 0.3),
        (0.52, 0.34),
        (0.45, 0.32),
        (0.38, 0.36),
        (0.32, 0.48),
        (0.35, 0.62),
        (0.44, 0.72),
    ]
    ax.add_patch(
        Polygon(brain_outline, closed=True, edgecolor=PALETTE["green"], linewidth=6, facecolor=PALETTE["navy"])
    )

    np.random.seed(0)
    nodes = np.array(
        [
            [0.44, 0.64],
            [0.56, 0.64],
            [0.48, 0.54],
            [0.62, 0.5],
            [0.52, 0.4],
            [0.4, 0.46],
            [0.66, 0.44],
            [0.46, 0.32],
        ]
    )
    for i, node in enumerate(nodes):
        ax.add_patch(Circle(node, 0.018, facecolor=PALETTE["green"], edgecolor="none"))
        for j in range(i):
            if np.linalg.norm(nodes[j] - node) < 0.22:
                ax.plot(
                    [nodes[j, 0], node[0]],
                    [nodes[j, 1], node[1]],
                    color=PALETTE["green"],
                    linewidth=2.5,
                    alpha=0.7,
                )

    ax.text(0.5, 0.86, "CONSOLIDATION", color=PALETTE["gold"], fontsize=64, ha="center", fontweight="bold")

    sleep_positions = [(0.28, 0.24), (0.72, 0.22)]
    for x, y in sleep_positions:
        ax.text(x, y, "Z Z Z", color=PALETTE["green"], fontsize=32, fontweight="bold")

    clock = Circle((0.82, 0.68), 0.07, facecolor=PALETTE["navy"], edgecolor=PALETTE["green"], linewidth=4)
    ax.add_patch(clock)
    ax.plot([0.82, 0.82], [0.68, 0.75], color=PALETTE["green"], linewidth=4)
    ax.plot([0.82, 0.86], [0.68, 0.64], color=PALETTE["green"], linewidth=4)


def draw_frame7(fig, ax):
    ax.text(0.5, 0.78, "800+ studies", color=PALETTE["gold"], fontsize=96, ha="center", fontweight="bold")
    ax.text(0.5, 0.66, "Meta-Analysis Consensus", color=PALETTE["gray"], fontsize=40, ha="center")

    # Bar chart
    inset = fig.add_axes([0.32, 0.28, 0.36, 0.28])
    inset.set_facecolor(PALETTE["navy"])
    inset.bar(["Effect Size"], [0.85], color=PALETTE["green"], width=0.6)
    inset.text(0, 0.88, "LARGE", color=PALETTE["gold"], fontsize=32, ha="center", va="bottom")
    inset.set_ylim(0, 1)
    inset.tick_params(colors=PALETTE["gray"], labelsize=18)
    for spine in inset.spines.values():
        spine.set_color(PALETTE["gray"])
    inset.set_ylabel("", color=PALETTE["gray"])

    # Diversity icons (simple shapes)
    icon_positions = [(0.2, 0.22), (0.5, 0.18), (0.8, 0.22)]
    for x, y in icon_positions:
        ax.add_patch(Circle((x, y + 0.06), 0.035, facecolor=PALETTE["green"], edgecolor="none"))
        ax.add_patch(Rectangle((x - 0.045, y - 0.04), 0.09, 0.08, facecolor=PALETTE["blue"], edgecolor="none"))

    ax.text(0.5, 0.12, "Across ages • subjects • materials", color=PALETTE["green"], fontsize=34, ha="center")


def draw_frame8(fig, ax):
    ax.text(0.5, 0.82, "Optimal Spacing", color=PALETTE["gold"], fontsize=68, ha="center", fontweight="bold")
    ax.plot([0.12, 0.88], [0.4, 0.4], color=PALETTE["blue"], linewidth=6)
    intervals = [
        ("1 day", 0.18),
        ("3 days", 0.32),
        ("1 week", 0.48),
        ("2 weeks", 0.64),
        ("1 month", 0.82),
    ]
    prev = 0.12
    for label, pos in intervals:
        ax.add_patch(
            FancyArrow(
                prev,
                0.4,
                pos - prev - 0.02,
                0,
                width=0.015,
                length_includes_head=True,
                head_width=0.05,
                head_length=0.02,
                color=PALETTE["blue"],
            )
        )
        ax.text(pos, 0.52, label, color=PALETTE["gold"], fontsize=40, ha="center")
        prev = pos


def draw_frame9(fig, ax):
    ax.text(0.3, 0.84, "Feels Slower", color=PALETTE["gray"], fontsize=60, ha="center", fontweight="bold")
    ax.text(0.7, 0.84, "Works Better", color=PALETTE["gold"], fontsize=60, ha="center", fontweight="bold")

    # Calendar grid
    left = 0.18
    width = 0.64
    bottom = 0.18
    height = 0.52
    rows = 4
    cols = 7
    cell_w = width / cols
    cell_h = height / rows
    for r in range(rows):
        for c in range(cols):
            x = left + c * cell_w
            y = bottom + r * cell_h
            edge_color = PALETTE["gray"] if c < cols / 2 else PALETTE["gold"]
            ax.add_patch(Rectangle((x, y), cell_w, cell_h, edgecolor=edge_color, linewidth=1.5, facecolor="none"))

    spacing_days = [(0, 0), (1, 1), (2, 1), (4, 2), (5, 2)]
    for c, r in spacing_days:
        x = left + c * cell_w + cell_w / 2
        y = bottom + (rows - r - 1) * cell_h + cell_h / 2
        color = PALETTE["blue"] if c < cols / 2 else PALETTE["gold"]
        ax.plot(x, y, marker="o", markersize=16, color=color)

    ax.plot([0.5, 0.5], [0.16, 0.82], color=PALETTE["blue"], linewidth=4, linestyle="--", alpha=0.7)
    ax.text(0.5, 0.1, "The Practical Paradox", color=PALETTE["green"], fontsize=42, ha="center")


def draw_frame10(fig, ax):
    ax.text(0.5, 0.78, "Spacing Effect Takeaways", color=PALETTE["gold"], fontsize=68, ha="center", fontweight="bold")
    positions = [0.6, 0.42, 0.24]
    texts = [
        "Notice when you're cramming",
        "Design delays into your practice",
        "Trust the forgetting",
    ]
    for idx, (y, text) in enumerate(zip(positions, texts), start=1):
        ax.add_patch(
            Rectangle(
                (0.18, y - 0.08),
                0.64,
                0.12,
                facecolor=PALETTE["navy"],
                edgecolor=PALETTE["gold"],
                linewidth=3,
            )
        )
        ax.text(0.22, y, f"{idx}.", color=PALETTE["gold"], fontsize=48, va="center", fontweight="bold")
        ax.text(0.26, y, text, color=PALETTE["gray"], fontsize=40, va="center")


DRAWERS = [
    draw_frame1,
    draw_frame2,
    draw_frame3,
    draw_frame4,
    draw_frame5,
    draw_frame6,
    draw_frame7,
    draw_frame8,
    draw_frame9,
    draw_frame10,
]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for idx, drawer in enumerate(DRAWERS, start=1):
        name = f"frame{idx:02d}.png"
        save_frame(name, drawer)


if __name__ == "__main__":
    main()
