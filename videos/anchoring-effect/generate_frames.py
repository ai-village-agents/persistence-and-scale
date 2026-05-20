import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Ellipse
from matplotlib.lines import Line2D
from matplotlib.colors import LinearSegmentedColormap


def setup_figure():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    fig.patch.set_facecolor("#0f0f1f")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def apply_gradient(ax, colors, direction="vertical"):
    gradient = np.linspace(0, 1, 512)
    if direction == "vertical":
        gradient = np.tile(gradient.reshape(-1, 1), (1, 512))
    else:
        gradient = np.tile(gradient.reshape(1, -1), (512, 1))
    cmap = LinearSegmentedColormap.from_list("custom_gradient", colors)
    ax.imshow(
        gradient,
        aspect="auto",
        cmap=cmap,
        extent=[0, 1, 0, 1],
        origin="lower",
        interpolation="bicubic",
    )


def frame01(path):
    fig, ax = setup_figure()
    apply_gradient(ax, ["#1a1a2e", "#16213e"])
    ax.text(
        0.5,
        0.6,
        "THE ANCHORING EFFECT",
        ha="center",
        va="center",
        color="white",
        fontsize=90,
        fontweight="bold",
    )
    ax.text(
        0.5,
        0.45,
        "How the first number shapes all that follows",
        ha="center",
        va="center",
        color="#d0d0d0",
        fontsize=44,
    )
    save_figure(fig, path)


def save_figure(fig, path):
    fig.savefig(path, dpi=100, facecolor=fig.get_facecolor(), edgecolor="none", pad_inches=0)
    plt.close(fig)


def frame02(path):
    fig, ax = setup_figure()
    ax.set_facecolor("#0f1a2b")

    ax.text(
        0.5,
        0.92,
        "What % of UN members are African nations?",
        ha="center",
        va="center",
        color="white",
        fontsize=54,
        fontweight="bold",
    )

    ax.text(0.5, 0.62, "vs.", ha="center", va="center", color="#f5f5f5", fontsize=80, fontweight="bold")

    left_panel = Rectangle((0.1, 0.2), 0.32, 0.6, facecolor="#16213e", edgecolor="#1d2e4a", linewidth=3)
    right_panel = Rectangle((0.58, 0.2), 0.32, 0.6, facecolor="#16213e", edgecolor="#1d2e4a", linewidth=3)
    ax.add_patch(left_panel)
    ax.add_patch(right_panel)

    # Left wheel
    wheel_center_left = (0.26, 0.5)
    circle = Circle(wheel_center_left, 0.12, facecolor="#1c2c4d", edgecolor="#34ace7", linewidth=6)
    ax.add_patch(circle)
    ax.text(*wheel_center_left, "10", color="#34ace7", fontsize=60, fontweight="bold", ha="center", va="center")
    ax.text(
        0.26,
        0.31,
        "Spin",
        ha="center",
        va="center",
        color="#9ec9ff",
        fontsize=32,
    )
    ax.text(
        0.26,
        0.73,
        "25%",
        ha="center",
        va="center",
        color="#f5f5f5",
        fontsize=48,
        fontweight="bold",
    )
    ax.text(
        0.26,
        0.79,
        "Estimated answer",
        ha="center",
        va="center",
        color="#b5c8e8",
        fontsize=26,
    )

    # Right wheel
    wheel_center_right = (0.74, 0.5)
    circle = Circle(wheel_center_right, 0.12, facecolor="#1c2c4d", edgecolor="#ffb142", linewidth=6)
    ax.add_patch(circle)
    ax.text(*wheel_center_right, "65", color="#ffb142", fontsize=60, fontweight="bold", ha="center", va="center")
    ax.text(
        0.74,
        0.31,
        "Spin",
        ha="center",
        va="center",
        color="#ffd8a6",
        fontsize=32,
    )
    ax.text(
        0.74,
        0.73,
        "45%",
        ha="center",
        va="center",
        color="#f5f5f5",
        fontsize=48,
        fontweight="bold",
    )
    ax.text(
        0.74,
        0.79,
        "Estimated answer",
        ha="center",
        va="center",
        color="#b5c8e8",
        fontsize=26,
    )

    save_figure(fig, path)


def frame03(path):
    fig, ax = setup_figure()
    apply_gradient(ax, ["#0f3057", "#1a508b"])

    # Water ripples
    for idx, (radius, label) in enumerate(
        zip([0.12, 0.19, 0.26], ["Your Estimate", "Your Judgment", "Your Decision"])
    ):
        circle = Circle((0.5, 0.35), radius, fill=False, edgecolor="#d6e4f0", linewidth=4 - idx)
        ax.add_patch(circle)
        ax.text(
            0.5,
            0.35 + radius + 0.02,
            label,
            ha="center",
            va="center",
            color="#e8f1ff",
            fontsize=28,
        )

    # Anchor
    anchor_path = [
        ((0.5, 0.75), (0.5, 0.4)),
        ((0.5, 0.4), (0.45, 0.25)),
        ((0.5, 0.4), (0.55, 0.25)),
    ]
    ax.plot([0.5, 0.5], [0.95, 0.45], color="#f1f3f8", linewidth=6)
    ax.scatter([0.5], [0.45], color="#f1f3f8", s=200)
    ax.plot([0.45, 0.5, 0.55], [0.25, 0.45, 0.25], color="#f1f3f8", linewidth=10, solid_capstyle="round")
    ax.plot([0.4, 0.6], [0.2, 0.2], color="#f1f3f8", linewidth=12, solid_capstyle="round")
    ax.add_patch(Circle((0.4, 0.2), 0.03, edgecolor="#f1f3f8", facecolor="none", linewidth=8))
    ax.add_patch(Circle((0.6, 0.2), 0.03, edgecolor="#f1f3f8", facecolor="none", linewidth=8))

    ax.text(0.5, 0.88, "First number = anchor", ha="center", va="center", color="#f6fbff", fontsize=64, fontweight="bold")

    save_figure(fig, path)


def frame04(path):
    fig, ax = setup_figure()
    ax.set_facecolor("#0f1a2b")

    ax.text(
        0.5,
        0.9,
        "Who states first number sets the anchor",
        ha="center",
        va="center",
        color="white",
        fontsize=60,
        fontweight="bold",
    )

    left_panel = Rectangle((0.08, 0.18), 0.38, 0.6, facecolor="#16213e", edgecolor="#233958", linewidth=3)
    right_panel = Rectangle((0.54, 0.18), 0.38, 0.6, facecolor="#16213e", edgecolor="#233958", linewidth=3)
    ax.add_patch(left_panel)
    ax.add_patch(right_panel)

    ax.text(0.27, 0.66, "$900K", ha="center", va="center", color="#6ab0f3", fontsize=70, fontweight="bold")
    ax.text(0.27, 0.52, "Asking price", ha="center", va="center", color="#b5c8e8", fontsize=32)
    ax.text(0.27, 0.36, "$850K", ha="center", va="center", color="#f7f7f7", fontsize=64, fontweight="bold")
    ax.text(0.27, 0.26, "Counteroffer", ha="center", va="center", color="#b5c8e8", fontsize=32)

    ax.text(0.73, 0.66, "$750K", ha="center", va="center", color="#6ab0f3", fontsize=70, fontweight="bold")
    ax.text(0.73, 0.52, "Asking price", ha="center", va="center", color="#b5c8e8", fontsize=32)
    ax.text(0.73, 0.36, "$700K", ha="center", va="center", color="#f7f7f7", fontsize=64, fontweight="bold")
    ax.text(0.73, 0.26, "Counteroffer", ha="center", va="center", color="#b5c8e8", fontsize=32)

    # House icons
    ax.add_patch(Rectangle((0.22, 0.72), 0.1, 0.08, facecolor="#233958"))
    ax.add_patch(Rectangle((0.68, 0.72), 0.1, 0.08, facecolor="#233958"))
    ax.plot([0.22, 0.27, 0.32], [0.8, 0.86, 0.8], color="#45aaf2", linewidth=4)
    ax.plot([0.68, 0.73, 0.78], [0.8, 0.86, 0.8], color="#45aaf2", linewidth=4)

    save_figure(fig, path)


def frame05(path):
    fig, ax = setup_figure()
    ax.set_facecolor("#10223a")

    ax.text(
        0.5,
        0.88,
        "Anchored retail pricing",
        ha="center",
        va="center",
        color="white",
        fontsize=60,
        fontweight="bold",
    )

    left_box = Rectangle((0.12, 0.18), 0.32, 0.6, facecolor="#182d4f", edgecolor="#274065", linewidth=3)
    right_box = Rectangle((0.56, 0.18), 0.32, 0.6, facecolor="#182d4f", edgecolor="#274065", linewidth=3)
    ax.add_patch(left_box)
    ax.add_patch(right_box)

    ax.text(0.28, 0.63, "Was $120", ha="center", va="center", color="#ff6b6b", fontsize=56, fontweight="bold")
    ax.plot([0.17, 0.39], [0.64, 0.7], color="#ff6b6b", linewidth=6)
    ax.text(0.28, 0.5, "Now $80", ha="center", va="center", color="#f6f7fb", fontsize=70, fontweight="bold")
    ax.text(0.28, 0.36, "Feels like $40 saved", ha="center", va="center", color="#9ec9ff", fontsize=32)

    ax.text(0.72, 0.63, "Just $80", ha="center", va="center", color="#f6f7fb", fontsize=70, fontweight="bold")
    ax.text(0.72, 0.48, "No comparison", ha="center", va="center", color="#b5c8e8", fontsize=34)
    ax.text(0.72, 0.36, "Feels like $0 saved", ha="center", va="center", color="#9ec9ff", fontsize=32)

    cart = Rectangle((0.24, 0.22), 0.08, 0.04, facecolor="#45aaf2", edgecolor="#45aaf2")
    ax.add_patch(cart)
    ax.plot([0.24, 0.32], [0.22, 0.16], color="#45aaf2", linewidth=4)
    ax.add_patch(Circle((0.24, 0.16), 0.02, facecolor="#45aaf2"))
    ax.add_patch(Circle((0.32, 0.16), 0.02, facecolor="#45aaf2"))

    save_figure(fig, path)


def frame06(path):
    fig, ax = setup_figure()
    ax.set_facecolor("#101a2f")

    salaries = np.linspace(40000, 140000, 400)
    low_center = 65000
    high_center = 105000
    std_dev = 12000

    low_curve = np.exp(-0.5 * ((salaries - low_center) / std_dev) ** 2)
    high_curve = np.exp(-0.5 * ((salaries - high_center) / std_dev) ** 2)

    ax.plot(salaries, low_curve, color="#45aaf2", linewidth=6, label="Low anchor")
    ax.plot(salaries, high_curve, color="#ffa502", linewidth=6, label="High anchor")

    ax.fill_between(salaries, low_curve, color="#45aaf2", alpha=0.15)
    ax.fill_between(salaries, high_curve, color="#ffa502", alpha=0.15)

    ax.set_xlim(40000, 140000)
    ax.set_ylim(0, 1.1)
    ax.set_xticks([40000, 60000, 80000, 100000, 120000, 140000])
    ax.set_xticklabels(["$40k", "$60k", "$80k", "$100k", "$120k", "$140k"], color="#d0d8ef", fontsize=26)
    ax.set_yticks([])
    ax.spines["bottom"].set_color("#d0d8ef")
    ax.spines["left"].set_color("#d0d8ef")
    ax.tick_params(axis="x", colors="#d0d8ef", length=0)

    ax.text(0.5, 0.92, "First number = gravitational center", ha="center", va="center", color="white", fontsize=54)

    ax.text(65000, 1.02, "Low anchor", color="#45aaf2", fontsize=32, ha="center")
    ax.text(105000, 1.02, "High anchor", color="#ffa502", fontsize=32, ha="center")

    legend_elements = [
        Line2D([0], [0], color="#45aaf2", lw=6, label="Lower anchor pulls expectations left"),
        Line2D([0], [0], color="#ffa502", lw=6, label="Higher anchor pulls expectations right"),
    ]
    ax.legend(handles=legend_elements, loc="upper right", frameon=False, fontsize=26, labelcolor="#e8f1ff")

    save_figure(fig, path)


def frame07(path):
    fig, ax = setup_figure()
    ax.set_facecolor("#0f1a2b")

    ax.text(
        0.5,
        0.85,
        "Insufficient adjustment",
        ha="center",
        va="center",
        color="white",
        fontsize=60,
        fontweight="bold",
    )

    ax.hlines(0.5, 0.1, 0.9, colors="#274065", linewidth=6)
    ax.text(0.1, 0.56, "Anchor: 10", color="#45aaf2", fontsize=42, ha="left")
    ax.text(0.9, 0.56, "True value: 50", color="#ffa502", fontsize=42, ha="right")

    anchor_marker = Circle((0.1, 0.5), 0.018, facecolor="#45aaf2", edgecolor="white", linewidth=2)
    ax.add_patch(anchor_marker)

    true_marker = Circle((0.9, 0.5), 0.022, facecolor="#ffa502", edgecolor="white", linewidth=2)
    ax.add_patch(true_marker)

    arrow = FancyArrowPatch(
        posA=(0.1, 0.5),
        posB=(0.4, 0.5),
        arrowstyle="<|-",
        mutation_scale=25,
        linewidth=6,
        color="#9ec9ff",
    )
    ax.add_patch(arrow)

    ax.text(0.4, 0.56, "Attempted adjustment", color="#9ec9ff", fontsize=36, ha="left")
    ax.text(0.4, 0.42, "Still too close to anchor", color="#b5c8e8", fontsize=32, ha="left")

    save_figure(fig, path)


def frame08(path):
    fig, ax = setup_figure()
    ax.set_facecolor("#10223a")

    ax.text(
        0.5,
        0.86,
        "Even experts show anchoring effects",
        ha="center",
        va="center",
        color="white",
        fontsize=60,
        fontweight="bold",
    )

    icons = [
        ("Judge", (0.22, 0.44), "#45aaf2"),
        ("Real estate agent", (0.5, 0.44), "#ffa502"),
        ("Financial analyst", (0.78, 0.44), "#6ab0f3"),
    ]

    for label, (x, y), color in icons:
        circ = Circle((x, y), 0.12, facecolor="#182d4f", edgecolor=color, linewidth=6)
        ax.add_patch(circ)
        ax.text(x, y - 0.08, label, ha="center", va="center", color="#e6eefc", fontsize=32)

    brain = Circle((0.5, 0.63), 0.09, facecolor="#233958", edgecolor="#6ab0f3", linewidth=4)
    ax.add_patch(brain)
    ax.text(0.5, 0.63, "System 1", ha="center", va="center", color="#f6f7fb", fontsize=32)

    # Simple check marks inside circles
    for (x, _), color in [(icons[0][1], icons[0][2]), (icons[1][1], icons[1][2]), (icons[2][1], icons[2][2])]:
        ax.plot([x - 0.03, x - 0.01], [0.42, 0.38], color=color, linewidth=5)
        ax.plot([x - 0.01, x + 0.04], [0.38, 0.48], color=color, linewidth=5)

    save_figure(fig, path)


def frame09(path):
    fig, ax = setup_figure()
    ax.set_facecolor("#0f1a2b")

    titles = ["NOTICE", "ASK", "DO"]
    subtitles = [
        "When you see a first number",
        "What would I estimate independently?",
        "Calculate from scratch",
    ]
    colors = ["#45aaf2", "#ffa502", "#6ab0f3"]

    for i in range(3):
        x0 = 0.1 + i * 0.3
        panel = Rectangle((x0, 0.25), 0.24, 0.5, facecolor="#182d4f", edgecolor=colors[i], linewidth=4)
        ax.add_patch(panel)
        ax.text(
            x0 + 0.12,
            0.65,
            titles[i],
            ha="center",
            va="center",
            color="white",
            fontsize=48,
            fontweight="bold",
        )
        if i == 0:
            eye = Ellipse((x0 + 0.12, 0.55), 0.12, 0.06, facecolor="none", edgecolor=colors[i], linewidth=4)
            pupil = Circle((x0 + 0.12, 0.55), 0.018, facecolor=colors[i], edgecolor=colors[i])
            ax.add_patch(eye)
            ax.add_patch(pupil)
        elif i == 1:
            ax.text(x0 + 0.12, 0.55, "?", ha="center", va="center", color=colors[i], fontsize=60, fontweight="bold")
        else:
            ax.plot([x0 + 0.07, x0 + 0.11], [0.52, 0.48], color=colors[i], linewidth=5)
            ax.plot([x0 + 0.11, x0 + 0.17], [0.48, 0.58], color=colors[i], linewidth=5)
        ax.text(
            x0 + 0.12,
            0.4,
            subtitles[i],
            ha="center",
            va="center",
            color="#d0d8ef",
            fontsize=30,
        )

    ax.text(0.5, 0.85, "3 ways to counter anchoring", ha="center", va="center", color="white", fontsize=58)

    save_figure(fig, path)


def frame10(path):
    fig, ax = setup_figure()
    apply_gradient(ax, ["#1a1a2e", "#16213e"])

    ax.text(
        0.5,
        0.6,
        "The first number creates a gravitational field",
        ha="center",
        va="center",
        color="white",
        fontsize=68,
        fontweight="bold",
    )
    ax.text(
        0.5,
        0.46,
        "Awareness doesn't eliminate anchoring - but lets you question it",
        ha="center",
        va="center",
        color="#d0d0d0",
        fontsize=40,
    )

    circle = Circle((0.5, 0.32), 0.06, facecolor="#233958", edgecolor="#45aaf2", linewidth=4)
    ax.add_patch(circle)
    ax.plot([0.5, 0.5], [0.4, 0.34], color="#45aaf2", linewidth=6)
    ax.scatter([0.5], [0.34], color="#45aaf2", s=150)
    ax.plot([0.46, 0.5, 0.54], [0.28, 0.34, 0.28], color="#45aaf2", linewidth=6, solid_capstyle="round")
    ax.plot([0.45, 0.55], [0.26, 0.26], color="#45aaf2", linewidth=6, solid_capstyle="round")
    ax.add_patch(Circle((0.45, 0.26), 0.012, edgecolor="#45aaf2", facecolor="none", linewidth=4))
    ax.add_patch(Circle((0.55, 0.26), 0.012, edgecolor="#45aaf2", facecolor="none", linewidth=4))

    save_figure(fig, path)


def main():
    output_paths = {
        "frame01.png": frame01,
        "frame02.png": frame02,
        "frame03.png": frame03,
        "frame04.png": frame04,
        "frame05.png": frame05,
        "frame06.png": frame06,
        "frame07.png": frame07,
        "frame08.png": frame08,
        "frame09.png": frame09,
        "frame10.png": frame10,
    }

    for filename, func in output_paths.items():
        func(f"visuals/{filename}")


if __name__ == "__main__":
    main()
