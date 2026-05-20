import os

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle

OUTPUT_DIR = "visuals"

COLORS = {
    "deep_charcoal": "#1A1A1A",
    "contrast_orange": "#FF6B35",
    "neutral_gray": "#808080",
    "shift_blue": "#4A90E2",
    "frame_gold": "#FFD700",
    "light_gray": "#D3D3D3",
    "medium_gray": "#696969",
    "dark_gray": "#2F2F2F",
    "hot_red": "#FF4444",
    "lukewarm_purple": "#9370DB",
    "cold_blue": "#4444FF",
}


def base_figure():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)
    ax = fig.add_subplot(111)
    fig.patch.set_facecolor(COLORS["deep_charcoal"])
    ax.set_facecolor(COLORS["deep_charcoal"])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def save_frame(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor())
    plt.close(fig)


def frame01():
    fig, ax = base_figure()
    ax.text(
        0.5,
        0.5,
        "THE CONTRAST EFFECT",
        color=COLORS["contrast_orange"],
        fontsize=80,
        ha="center",
        va="center",
        fontweight="bold",
    )
    save_frame(fig, "frame01.png")


def frame02():
    fig, ax = base_figure()

    background_colors = ["light_gray", "medium_gray", "dark_gray"]
    for i, key in enumerate(background_colors):
        x = 0.15 + i * 0.25
        rect = Rectangle((x - 0.12, 0.25), 0.24, 0.5, facecolor=COLORS[key], edgecolor="none")
        ax.add_patch(rect)
        circle = Circle((x, 0.5), 0.095, facecolor=COLORS["neutral_gray"], edgecolor="white", linewidth=3)
        ax.add_patch(circle)

    ax.text(
        0.5,
        0.88,
        "Same Color, Different Context",
        color=COLORS["contrast_orange"],
        fontsize=42,
        ha="center",
        va="center",
    )

    save_frame(fig, "frame02.png")


def frame03():
    fig, ax = base_figure()

    bowls = [
        (0.2, COLORS["hot_red"], "HOT"),
        (0.5, COLORS["lukewarm_purple"], "LUKEWARM"),
        (0.8, COLORS["cold_blue"], "COLD"),
    ]

    for x, color, label in bowls:
        bowl = Circle((x, 0.45), 0.12, facecolor=color, edgecolor=COLORS["frame_gold"], linewidth=4)
        ax.add_patch(bowl)
        ax.text(x, 0.27, label, color=color, fontsize=32, ha="center", va="center", fontweight="bold")

    left_hand = FancyBboxPatch(
        (0.14, 0.55),
        0.12,
        0.08,
        boxstyle="round,pad=0.04",
        facecolor=COLORS["neutral_gray"],
        edgecolor="white",
        linewidth=2,
    )
    right_hand = FancyBboxPatch(
        (0.74, 0.55),
        0.12,
        0.08,
        boxstyle="round,pad=0.04",
        facecolor=COLORS["neutral_gray"],
        edgecolor="white",
        linewidth=2,
    )
    ax.add_patch(left_hand)
    ax.add_patch(right_hand)

    left_arrow = FancyArrowPatch(
        (0.2, 0.59),
        (0.47, 0.55),
        arrowstyle="->",
        linewidth=3,
        color=COLORS["contrast_orange"],
    )
    right_arrow = FancyArrowPatch(
        (0.8, 0.59),
        (0.53, 0.55),
        arrowstyle="->",
        linewidth=3,
        color=COLORS["contrast_orange"],
    )
    ax.add_patch(left_arrow)
    ax.add_patch(right_arrow)

    ax.text(0.2, 0.65, "Hand leaves HOT", color=COLORS["contrast_orange"], fontsize=20, ha="center")
    ax.text(0.8, 0.65, "Hand leaves COLD", color=COLORS["contrast_orange"], fontsize=20, ha="center")
    ax.text(0.5, 0.78, "Same lukewarm bowl feels different", color="white", fontsize=36, ha="center")

    save_frame(fig, "frame03.png")


def frame04():
    fig, ax = base_figure()

    for i, labels in enumerate((("A", "B"), ("B", "A"))):
        y = 0.65 - i * 0.35
        for j, label in enumerate(labels):
            x = 0.32 + j * 0.28
            color = COLORS["neutral_gray"] if label == "A" else COLORS["shift_blue"]
            box = FancyBboxPatch(
                (x, y),
                0.16,
                0.12,
                boxstyle="round,pad=0.04",
                facecolor=color,
                edgecolor="white",
                linewidth=2,
            )
            ax.add_patch(box)
            ax.text(x + 0.08, y + 0.06, label, color=COLORS["deep_charcoal"], fontsize=36, ha="center", va="center")

        arrow = FancyArrowPatch(
            (0.48, y - 0.04),
            (0.76, y - 0.04),
            arrowstyle="->",
            linewidth=3,
            color="white",
        )
        ax.add_patch(arrow)
        outcome = "+ More impressed" if i == 0 else "- Less impressed"
        ax.text(0.8, y - 0.04, outcome, color=COLORS["contrast_orange"], fontsize=26, va="center")

        ax.text(0.15, y + 0.06, "Order", color="white", fontsize=28, ha="center", va="center")
        ax.text(0.48, y + 0.1, "Evaluation", color="white", fontsize=22, ha="center")

    ax.text(0.5, 0.9, "Order Matters", color=COLORS["contrast_orange"], fontsize=42, ha="center")

    save_frame(fig, "frame04.png")


def frame05():
    fig, ax = base_figure()

    scenarios = [
        ("$2,000 suit", "$1,200 suit seems reasonable"),
        ("$20 burger", "$12 burger feels fair"),
        ("$5,000 TV", "$2,800 TV looks like a deal"),
    ]

    for i, (anchor, target) in enumerate(scenarios):
        y = 0.72 - i * 0.25
        anchor_box = FancyBboxPatch(
            (0.18, y),
            0.28,
            0.12,
            boxstyle="round,pad=0.05",
            facecolor=COLORS["frame_gold"],
            edgecolor="none",
        )
        target_box = FancyBboxPatch(
            (0.54, y),
            0.32,
            0.12,
            boxstyle="round,pad=0.05",
            facecolor=COLORS["shift_blue"],
            edgecolor="none",
        )
        ax.add_patch(anchor_box)
        ax.add_patch(target_box)
        ax.text(0.32, y + 0.06, anchor, color=COLORS["deep_charcoal"], fontsize=30, ha="center", fontweight="bold")
        ax.text(0.7, y + 0.06, target, color="white", fontsize=24, ha="center")
        arrow = FancyArrowPatch(
            (0.46, y + 0.06),
            (0.54, y + 0.06),
            arrowstyle="->",
            linewidth=3,
            color=COLORS["contrast_orange"],
        )
        ax.add_patch(arrow)

    ax.text(0.5, 0.92, "Price Perception Through Anchors", color=COLORS["contrast_orange"], fontsize=40, ha="center")

    save_frame(fig, "frame05.png")


def frame06():
    fig, ax = base_figure()
    x = [0.1, 0.3, 0.5, 0.7, 0.9]
    upward = [0.3, 0.5, 0.6, 0.7, 0.85]
    downward = [0.7, 0.6, 0.55, 0.4, 0.25]

    ax.plot(x, upward, color=COLORS["shift_blue"], linewidth=5)
    ax.plot(x, downward, color=COLORS["neutral_gray"], linewidth=5)
    ax.scatter([0.9], [0.85], color=COLORS["contrast_orange"], s=300, zorder=5)
    ax.scatter([0.9], [0.25], color=COLORS["contrast_orange"], s=300, zorder=5)

    ax.text(0.9, 0.88, "Peak End", color=COLORS["contrast_orange"], fontsize=24, ha="right")
    ax.text(0.9, 0.28, "Low End", color=COLORS["contrast_orange"], fontsize=24, ha="right")
    ax.text(0.5, 0.95, "Designing Experiences", color=COLORS["contrast_orange"], fontsize=40, ha="center")
    ax.text(0.1, 0.08, "Time", color="white", fontsize=28, ha="left")
    ax.text(0.02, 0.9, "Experience Quality", color="white", fontsize=28, rotation=90, ha="left")

    save_frame(fig, "frame06.png")


def frame07():
    fig, ax = base_figure()

    for i in range(3):
        x = 0.15 + i * 0.32
        frame = FancyBboxPatch(
            (x, 0.25),
            0.25,
            0.5,
            boxstyle="round,pad=0.04",
            facecolor="none",
            edgecolor=COLORS["frame_gold"],
            linewidth=4,
        )
        ax.add_patch(frame)
        context = Rectangle((x + 0.03, 0.28), 0.19, 0.44, facecolor=[(i + 1) * 0.13] * 3, alpha=0.4, edgecolor="none")
        ax.add_patch(context)
        obj = Circle((x + 0.125, 0.5), 0.08, facecolor=COLORS["shift_blue"], edgecolor="white", linewidth=3)
        ax.add_patch(obj)
        ax.text(x + 0.125, 0.78, "Same object", color="white", fontsize=22, ha="center")
        ax.text(x + 0.125, 0.2, "?", color=COLORS["contrast_orange"], fontsize=48, ha="center")

    ax.text(0.5, 0.88, "Context Changes Perception", color=COLORS["contrast_orange"], fontsize=42, ha="center")

    save_frame(fig, "frame07.png")


def frame08():
    fig, ax = base_figure()

    x = [0.05, 0.25, 0.45, 0.65, 0.85]
    baseline_old = 0.35
    baseline_new = 0.5
    curve = [0.35, 0.4, 0.7, 0.55, 0.5]

    ax.plot(x, curve, color=COLORS["contrast_orange"], linewidth=5)
    ax.axhline(baseline_old, xmin=0.05, xmax=0.5, color=COLORS["neutral_gray"], linestyle="--", linewidth=3)
    ax.axhline(baseline_new, xmin=0.5, xmax=0.95, color=COLORS["shift_blue"], linestyle="--", linewidth=3)
    ax.text(0.32, baseline_old + 0.02, "Old Baseline", color=COLORS["neutral_gray"], fontsize=24, ha="center")
    ax.text(0.68, baseline_new + 0.02, "New Baseline", color=COLORS["shift_blue"], fontsize=24, ha="center")
    ax.text(0.45, 0.74, "Spike", color="white", fontsize=26, ha="center")
    ax.text(0.55, 0.6, "Adaptation", color="white", fontsize=26, ha="center")

    ax.text(0.5, 0.92, "Hedonic Adaptation", color=COLORS["contrast_orange"], fontsize=42, ha="center")
    ax.text(0.05, 0.08, "Time", color="white", fontsize=28, ha="left")
    ax.text(0.02, 0.9, "Happiness / Satisfaction", color="white", fontsize=26, rotation=90, ha="left")

    save_frame(fig, "frame08.png")


def frame09():
    fig, ax = base_figure()

    divider = Rectangle((0.48, 0.1), 0.04, 0.8, facecolor="white", alpha=0.15, edgecolor="none")
    ax.add_patch(divider)

    left_panel = Rectangle((0.05, 0.15), 0.38, 0.7, facecolor="white", alpha=0.08, edgecolor="none")
    right_panel = Rectangle((0.57, 0.15), 0.38, 0.7, facecolor="white", alpha=0.12, edgecolor="none")
    ax.add_patch(left_panel)
    ax.add_patch(right_panel)

    ax.text(0.24, 0.78, "Could be better", color="white", fontsize=38, ha="center")
    ax.text(0.24, 0.7, "(Upward comparison)", color=COLORS["neutral_gray"], fontsize=22, ha="center")
    ax.text(0.76, 0.78, "Could be worse", color=COLORS["contrast_orange"], fontsize=38, ha="center")
    ax.text(0.76, 0.7, "(Downward comparison)", color=COLORS["neutral_gray"], fontsize=22, ha="center")

    ax.text(0.5, 0.5, "Same Life Situation", color="white", fontsize=32, ha="center", va="center")
    ax.text(0.24, 0.42, "Outcome: -", color="white", fontsize=30, ha="center")
    ax.text(0.76, 0.42, "Outcome: +", color=COLORS["contrast_orange"], fontsize=30, ha="center")

    sad_face = Circle((0.24, 0.32), 0.08, facecolor="none", edgecolor="white", linewidth=3)
    happy_face = Circle((0.76, 0.32), 0.08, facecolor="none", edgecolor=COLORS["contrast_orange"], linewidth=3)
    ax.add_patch(sad_face)
    ax.add_patch(happy_face)
    ax.text(0.24, 0.32, ":(", color="white", fontsize=36, ha="center", va="center")
    ax.text(0.76, 0.32, ":)", color=COLORS["contrast_orange"], fontsize=36, ha="center", va="center")

    save_frame(fig, "frame09.png")


def frame10():
    fig, ax = base_figure()

    takeaways = [
        "Notice your contrast:\nWhat are you comparing to?",
        "Choose your sequence:\nOrder shapes judgment",
        "Set your frame:\nChoose what you compare to",
    ]

    for i, text in enumerate(takeaways, start=1):
        y = 0.74 - (i - 1) * 0.26
        box = FancyBboxPatch(
            (0.18, y),
            0.64,
            0.18,
            boxstyle="round,pad=0.06",
            facecolor="none",
            edgecolor="white",
            linewidth=2,
        )
        ax.add_patch(box)
        ax.text(0.22, y + 0.09, f"{i}.", color=COLORS["contrast_orange"], fontsize=48, ha="left", va="center")
        ax.text(0.26, y + 0.09, text, color="white", fontsize=30, ha="left", va="center")

    ax.text(0.5, 0.92, "Three Takeaways", color=COLORS["contrast_orange"], fontsize=44, ha="center")

    save_frame(fig, "frame10.png")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    frame01()
    frame02()
    frame03()
    frame04()
    frame05()
    frame06()
    frame07()
    frame08()
    frame09()
    frame10()


if __name__ == "__main__":
    main()
