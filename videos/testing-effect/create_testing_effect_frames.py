import os
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


COLORS = {
    "deep_navy": "#1a2332",
    "retrieval_red": "#e63946",
    "memory_gold": "#f4a261",
    "knowledge_blue": "#2a9d8f",
    "light_gray": "#e0e0e0",
}


def ensure_visuals_dir(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)


def create_base_figure():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_facecolor(COLORS["deep_navy"])
    fig.patch.set_facecolor(COLORS["deep_navy"])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def draw_circular_arrows(ax):
    outer_circle = patches.Circle((0.5, 0.35), 0.2, fill=False, lw=6, edgecolor=COLORS["knowledge_blue"])
    inner_circle = patches.Circle((0.5, 0.35), 0.12, fill=False, lw=6, edgecolor=COLORS["memory_gold"])
    ax.add_patch(outer_circle)
    ax.add_patch(inner_circle)

    arrow1 = patches.FancyArrowPatch(
        (0.62, 0.35),
        (0.62, 0.35),
        connectionstyle="arc3,rad=0.3",
        arrowstyle="-|>",
        mutation_scale=30,
        color=COLORS["knowledge_blue"],
        lw=0,
    )
    arrow2 = patches.FancyArrowPatch(
        (0.38, 0.35),
        (0.38, 0.35),
        connectionstyle="arc3,rad=-0.3",
        arrowstyle="-|>",
        mutation_scale=30,
        color=COLORS["memory_gold"],
        lw=0,
    )
    ax.add_patch(arrow1)
    ax.add_patch(arrow2)


def frame_1():
    fig, ax = create_base_figure()
    ax.text(
        0.5,
        0.75,
        "The Testing Effect",
        color=COLORS["retrieval_red"],
        fontsize=72,
        ha="center",
        va="center",
        fontweight="bold",
    )
    draw_circular_arrows(ax)
    return fig


def frame_2():
    fig, ax = create_base_figure()

    ax.axvline(0.5, color=COLORS["light_gray"], linewidth=4, alpha=0.3)

    left_page = patches.FancyBboxPatch(
        (0.15, 0.3),
        0.25,
        0.4,
        boxstyle="round,pad=0.02",
        linewidth=4,
        edgecolor=COLORS["light_gray"],
        facecolor=COLORS["deep_navy"],
    )
    right_page = patches.FancyBboxPatch(
        (0.6, 0.3),
        0.25,
        0.4,
        boxstyle="round,pad=0.02",
        linewidth=4,
        edgecolor=COLORS["light_gray"],
        facecolor=COLORS["light_gray"],
    )
    ax.add_patch(left_page)
    ax.add_patch(right_page)

    for i, y in enumerate(np.linspace(0.6, 0.36, 4)):
        ax.add_line(
            plt.Line2D(
                [0.2, 0.35],
                [y, y],
                color=COLORS["memory_gold"],
                linewidth=5,
            )
        )
        ax.add_line(
            plt.Line2D(
                [0.2, 0.32],
                [y - 0.02, y - 0.02],
                color=COLORS["memory_gold"],
                linewidth=3,
                alpha=0.7,
            )
        )

    ax.text(0.275, 0.68, "Re-reading", color=COLORS["light_gray"], fontsize=36, ha="center", va="center")
    ax.text(0.725, 0.68, "Retrieval", color=COLORS["light_gray"], fontsize=36, ha="center", va="center")

    return fig


def frame_3():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor(COLORS["deep_navy"])
    ax = fig.add_subplot(111)
    ax.set_facecolor(COLORS["deep_navy"])
    ax.axis("off")

    chart_ax = fig.add_axes([0.2, 0.2, 0.6, 0.6])
    chart_ax.set_facecolor(COLORS["deep_navy"])
    bars = chart_ax.bar(
        ["Re-reading", "Testing"],
        [0.5, 0.8],
        color=[COLORS["memory_gold"], COLORS["retrieval_red"]],
        width=0.4,
    )

    chart_ax.set_ylim(0, 1)
    chart_ax.spines["bottom"].set_color(COLORS["light_gray"])
    chart_ax.spines["left"].set_color(COLORS["light_gray"])
    chart_ax.spines["top"].set_visible(False)
    chart_ax.spines["right"].set_visible(False)
    chart_ax.tick_params(axis="x", colors=COLORS["light_gray"], labelsize=24)
    chart_ax.tick_params(axis="y", colors=COLORS["light_gray"], labelsize=18)
    chart_ax.set_ylabel("Retention After 1 Week", color=COLORS["light_gray"], fontsize=24)
    chart_ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    chart_ax.set_yticklabels(["0", "25%", "50%", "75%", "100%"])

    for bar, label in zip(bars, ["50%", "80%"]):
        height = bar.get_height()
        chart_ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.04,
            label,
            ha="center",
            fontsize=28,
            color=COLORS["light_gray"],
            fontweight="bold",
        )

    return fig


def frame_4():
    fig, ax = create_base_figure()

    boxes = {
        "top": ((0.35, 0.7), "Study Material", COLORS["knowledge_blue"]),
        "left": ((0.18, 0.45), "Group A:\nRe-study", COLORS["memory_gold"]),
        "right": ((0.58, 0.45), "Group B:\nTest", COLORS["retrieval_red"]),
        "bottom": ((0.35, 0.2), "One Week Later", COLORS["light_gray"]),
    }

    for (x, y), text, color in boxes.values():
        rect = patches.FancyBboxPatch(
            (x, y),
            0.27,
            0.12,
            boxstyle="round,pad=0.04",
            linewidth=3,
            edgecolor=color,
            facecolor=COLORS["deep_navy"],
        )
        ax.add_patch(rect)
        ax.text(
            x + 0.135,
            y + 0.06,
            text,
            color=color,
            fontsize=28,
            ha="center",
            va="center",
            fontweight="bold",
        )

    arrow_kwargs = dict(arrowstyle="-|>", color=COLORS["light_gray"], mutation_scale=20, lw=3)
    ax.add_patch(patches.FancyArrowPatch((0.485, 0.7), (0.345, 0.57), **arrow_kwargs))
    ax.add_patch(patches.FancyArrowPatch((0.485, 0.7), (0.695, 0.57), **arrow_kwargs))
    ax.add_patch(patches.FancyArrowPatch((0.315, 0.45), (0.315, 0.32), **arrow_kwargs))
    ax.add_patch(patches.FancyArrowPatch((0.655, 0.45), (0.455, 0.32), **arrow_kwargs))

    ax.text(
        0.5,
        0.08,
        "Roediger & Karpicke (2006)",
        color=COLORS["light_gray"],
        fontsize=24,
        ha="center",
    )

    return fig


def frame_5():
    fig, ax = create_base_figure()

    x = np.linspace(0.1, 0.9, 200)
    y_levels = [0.7, 0.5, 0.3]
    alphas = [0.3, 0.6, 1.0]
    widths = [3, 6, 9]
    labels = ["Weak", "Stronger", "Strongest"]
    colors = [COLORS["memory_gold"], COLORS["memory_gold"], COLORS["retrieval_red"]]

    for y_base, alpha, width, label, color in zip(y_levels, alphas, widths, labels, colors):
        y = y_base + 0.04 * np.sin(2 * np.pi * (x - 0.1))
        ax.plot(x, y, color=color, linewidth=width, alpha=alpha)
        ax.text(0.91, y_base, label, color=COLORS["light_gray"], fontsize=28, va="center", ha="left")

    ax.annotate(
        "",
        xy=(0.9, 0.28),
        xytext=(0.1, 0.28),
        arrowprops=dict(arrowstyle="->", color=COLORS["light_gray"], lw=3),
    )
    ax.text(0.5, 0.22, "Pathways strengthen with retrieval", color=COLORS["light_gray"], fontsize=28, ha="center")

    return fig


def frame_6():
    fig, ax = create_base_figure()

    ax.text(0.5, 0.78, "Effort Level", color=COLORS["light_gray"], fontsize=48, ha="center", fontweight="bold")

    gauge_center = (0.5, 0.45)
    radius = 0.25

    base_wedge = patches.Wedge(gauge_center, radius, 210, -30, facecolor=COLORS["light_gray"], alpha=0.2, linewidth=0)
    ax.add_patch(base_wedge)

    active_wedge = patches.Wedge(
        gauge_center,
        radius,
        210,
        330,
        facecolor=COLORS["retrieval_red"],
        alpha=0.8,
        linewidth=0,
    )
    ax.add_patch(active_wedge)

    inner_circle = patches.Circle(gauge_center, 0.02, color=COLORS["deep_navy"])
    ax.add_patch(inner_circle)

    pointer_length = radius * 0.9
    angle_rad = np.deg2rad(320)
    pointer_end = (
        gauge_center[0] + pointer_length * np.cos(angle_rad),
        gauge_center[1] + pointer_length * np.sin(angle_rad),
    )
    ax.add_line(
        plt.Line2D(
            [gauge_center[0], pointer_end[0]],
            [gauge_center[1], pointer_end[1]],
            color=COLORS["light_gray"],
            linewidth=6,
        )
    )

    ax.text(0.5, 0.43, "Learning", color=COLORS["retrieval_red"], fontsize=36, ha="center", fontweight="bold")
    ax.text(0.5, 0.2, "Difficulty = Growth", color=COLORS["memory_gold"], fontsize=36, ha="center")

    return fig


def frame_7():
    fig, ax = create_base_figure()

    positions = [
        (0.3, 0.65),
        (0.7, 0.65),
        (0.3, 0.35),
        (0.7, 0.35),
    ]
    labels = ["Flashcards", "Self-Quiz", "Practice", "Teach Others"]
    colors = [COLORS["memory_gold"], COLORS["retrieval_red"], COLORS["knowledge_blue"], COLORS["memory_gold"]]

    for (x, y), label, color in zip(positions, labels, colors):
        square = patches.FancyBboxPatch(
            (x - 0.14, y - 0.14),
            0.28,
            0.28,
            boxstyle="round,pad=0.04",
            linewidth=3,
            edgecolor=COLORS["light_gray"],
            facecolor=COLORS["deep_navy"],
        )
        ax.add_patch(square)

        if label == "Flashcards":
            card = patches.Rectangle((x - 0.05, y - 0.02), 0.12, 0.16, linewidth=3, edgecolor=color, facecolor=COLORS["deep_navy"])
            card2 = patches.Rectangle((x - 0.08, y - 0.05), 0.12, 0.16, linewidth=2, edgecolor=COLORS["light_gray"], facecolor=COLORS["deep_navy"])
            ax.add_patch(card2)
            ax.add_patch(card)
        elif label == "Self-Quiz":
            ax.text(x, y + 0.04, "?", color=color, fontsize=72, ha="center", va="center", fontweight="bold")
        elif label == "Practice":
            page = patches.Rectangle((x - 0.06, y - 0.06), 0.12, 0.18, linewidth=2, edgecolor=COLORS["light_gray"], facecolor=COLORS["deep_navy"])
            pencil = patches.FancyArrowPatch(
                (x - 0.08, y - 0.08),
                (x + 0.08, y + 0.08),
                arrowstyle="-",
                linewidth=6,
                color=color,
            )
            ax.add_patch(page)
            ax.add_patch(pencil)
            ax.add_patch(patches.Circle((x + 0.08, y + 0.08), 0.01, color=COLORS["light_gray"]))
        elif label == "Teach Others":
            ax.add_patch(patches.Circle((x - 0.04, y + 0.05), 0.05, color=color, alpha=0.9))
            ax.add_patch(patches.Circle((x + 0.05, y + 0.03), 0.04, color=COLORS["knowledge_blue"], alpha=0.9))
            ax.add_patch(patches.Rectangle((x - 0.07, y - 0.1), 0.14, 0.06, color=COLORS["light_gray"], alpha=0.4))

        ax.text(x, y - 0.18, label, color=COLORS["light_gray"], fontsize=28, ha="center")

    return fig


def frame_8():
    fig, ax = create_base_figure()

    eye_outer = patches.Ellipse((0.5, 0.55), 0.45, 0.25, edgecolor=COLORS["memory_gold"], facecolor="none", linewidth=8)
    eye_inner = patches.Ellipse((0.5, 0.55), 0.28, 0.16, edgecolor=COLORS["memory_gold"], facecolor="none", linewidth=4)
    iris = patches.Circle((0.5, 0.55), 0.06, color=COLORS["memory_gold"])

    ax.add_patch(eye_outer)
    ax.add_patch(eye_inner)
    ax.add_patch(iris)

    ax.text(0.5, 0.32, "Notice", color=COLORS["light_gray"], fontsize=60, ha="center", fontweight="bold")
    ax.text(0.5, 0.22, "When you reach for notes to re-read", color=COLORS["light_gray"], fontsize=32, ha="center", alpha=0.8)

    return fig


def frame_9():
    fig, ax = create_base_figure()

    ax.text(0.5, 0.6, "?", color=COLORS["retrieval_red"], fontsize=180, ha="center", va="center", fontweight="bold")
    ax.text(0.5, 0.32, "Test Yourself First", color=COLORS["light_gray"], fontsize=60, ha="center", fontweight="bold")
    ax.text(0.5, 0.22, "Retrieve before you refresh", color=COLORS["light_gray"], fontsize=32, ha="center", alpha=0.8)

    return fig


def frame_10():
    fig, ax = create_base_figure()

    arrow = patches.FancyArrow(0.45, 0.4, 0.0, 0.25, width=0.2, length_includes_head=True, facecolor=COLORS["knowledge_blue"], edgecolor=COLORS["knowledge_blue"])
    ax.add_patch(arrow)
    ax.add_patch(patches.Rectangle((0.43, 0.35), 0.14, 0.08, color=COLORS["knowledge_blue"]))

    ax.text(0.5, 0.3, "Trust The Struggle", color=COLORS["light_gray"], fontsize=60, ha="center", fontweight="bold")
    ax.text(0.5, 0.2, "Difficulty is doing the work", color=COLORS["light_gray"], fontsize=32, ha="center", alpha=0.8)

    return fig


FRAME_CREATORS = [
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


def main():
    output_dir = Path("./visuals")
    ensure_visuals_dir(output_dir)

    for idx, frame_fn in enumerate(FRAME_CREATORS, start=1):
        fig = frame_fn()
        output_path = output_dir / f"frame{idx:02d}.png"
        fig.savefig(output_path, dpi=100, facecolor=COLORS["deep_navy"])
        plt.close(fig)

    print(f"Created {len(FRAME_CREATORS)} frames in {output_dir.resolve()}")


if __name__ == "__main__":
    main()
