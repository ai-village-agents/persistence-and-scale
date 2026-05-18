import os
import random

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import seaborn as sns


FIG_SIZE = (19.2, 10.8)
DPI = 100

COLORS = {
    "background": "#0a0e14",
    "text": "#e6edf3",
    "accent": "#58a6ff",
    "highlight": "#f78166",
    "muted": "#1f2a3a",
    "success": "#3fb950",
}


def configure_style() -> None:
    sns.set_theme(style="white", context="talk")
    plt.rcParams.update(
        {
            "figure.facecolor": COLORS["background"],
            "axes.facecolor": COLORS["background"],
            "axes.edgecolor": COLORS["background"],
            "axes.labelcolor": COLORS["text"],
            "text.color": COLORS["text"],
            "xtick.color": COLORS["text"],
            "ytick.color": COLORS["text"],
            "font.family": "DejaVu Sans",
        }
    )


def create_base_figure(title: str):
    fig, ax = plt.subplots(figsize=FIG_SIZE, dpi=DPI)
    fig.patch.set_facecolor(COLORS["background"])
    ax.set_facecolor(COLORS["background"])
    ax.axis("off")
    fig.text(
        0.05,
        0.88,
        title,
        fontsize=40,
        fontweight="bold",
        color=COLORS["text"],
    )
    return fig, ax


def slide_one(path: str) -> None:
    fig, ax = create_base_figure("The Illusion of Instant Output")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.2, 0.5, "PROMPT", fontsize=50, ha="center", va="center")
    ax.text(0.8, 0.5, "RESPONSE", fontsize=50, ha="center", va="center")
    ax.annotate(
        "",
        xy=(0.65, 0.5),
        xytext=(0.35, 0.5),
        arrowprops=dict(
            arrowstyle="-|>",
            lw=5,
            color=COLORS["accent"],
        ),
    )

    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def slide_two(path: str) -> None:
    fig, ax = create_base_figure("The Invisible Middle")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.2, 0.5, "PROMPT", fontsize=40, ha="center", va="center")
    ax.text(0.8, 0.5, "RESPONSE", fontsize=40, ha="center", va="center")
    ax.text(0.5, 0.5, "???", fontsize=60, ha="center", va="center", color=COLORS["highlight"])
    ax.annotate(
        "",
        xy=(0.42, 0.5),
        xytext=(0.3, 0.5),
        arrowprops=dict(arrowstyle="-|>", lw=3, color=COLORS["accent"]),
    )
    ax.annotate(
        "",
        xy=(0.7, 0.5),
        xytext=(0.58, 0.5),
        arrowprops=dict(arrowstyle="-|>", lw=3, color=COLORS["accent"]),
    )

    rng = np.random.default_rng(42)
    dots_x = rng.uniform(0.35, 0.65, 120)
    dots_y = rng.uniform(0.2, 0.8, 120)
    ax.scatter(
        dots_x,
        dots_y,
        s=rng.uniform(5, 40, size=dots_x.size),
        color=COLORS["muted"],
        alpha=0.6,
        edgecolors="none",
    )

    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def slide_three(path: str) -> None:
    fig, ax = create_base_figure("False Starts and Dead Ends")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    rng = np.random.default_rng(7)
    failed_points = rng.uniform(0.1, 0.9, size=(25, 2))
    ax.scatter(
        failed_points[:, 0],
        failed_points[:, 1],
        marker="x",
        s=200,
        color=COLORS["highlight"],
        linewidths=3,
    )

    success_x, success_y = 0.8, 0.75
    ax.scatter(
        [success_x],
        [success_y],
        marker="o",
        s=400,
        color=COLORS["success"],
        edgecolors=COLORS["text"],
        linewidths=2,
        zorder=3,
    )
    ax.plot(
        [success_x - 0.04, success_x - 0.01],
        [success_y - 0.04, success_y - 0.07],
        color=COLORS["text"],
        linewidth=4,
        zorder=4,
    )
    ax.plot(
        [success_x - 0.01, success_x + 0.05],
        [success_y - 0.07, success_y + 0.04],
        color=COLORS["text"],
        linewidth=4,
        zorder=4,
    )

    ax.text(
        0.1,
        0.2,
        "Each failure refines the path to success.",
        fontsize=28,
        color=COLORS["text"],
    )

    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def slide_four(path: str) -> None:
    fig, ax = create_base_figure("The Research Phase")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    sources = [
        ("Docs", (0.2, 0.75)),
        ("Prior Work", (0.2, 0.55)),
        ("Technical Details", (0.2, 0.35)),
        ("Best Practices", (0.2, 0.15)),
    ]
    output_pos = (0.75, 0.45)

    for label, (x, y) in sources:
        ax.add_patch(
            patches.FancyBboxPatch(
                (x - 0.12, y - 0.07),
                0.24,
                0.14,
                boxstyle="round,pad=0.02",
                facecolor=COLORS["muted"],
                edgecolor=COLORS["accent"],
                linewidth=2,
            )
        )
        ax.text(x, y, label, ha="center", va="center", fontsize=28)
        ax.annotate(
            "",
            xy=output_pos,
            xytext=(x + 0.12, y),
            arrowprops=dict(
                arrowstyle="-|>",
                lw=2.5,
                color=COLORS["accent"],
            ),
        )

    ax.add_patch(
        patches.FancyBboxPatch(
            (output_pos[0] - 0.15, output_pos[1] - 0.09),
            0.3,
            0.18,
            boxstyle="round,pad=0.03",
            facecolor=COLORS["accent"],
            edgecolor=COLORS["text"],
            linewidth=2.5,
        )
    )
    ax.text(
        output_pos[0],
        output_pos[1],
        "Output",
        ha="center",
        va="center",
        fontsize=32,
        fontweight="bold",
        color=COLORS["background"],
    )

    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def slide_five(path: str) -> None:
    fig, ax = create_base_figure("Decision Points")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    nodes = {
        "Start": (0.5, 0.8),
        "Option A": (0.32, 0.6),
        "Option B": (0.68, 0.6),
        "A1": (0.2, 0.4),
        "A2": (0.38, 0.4),
        "B1": (0.62, 0.4),
        "B2": (0.8, 0.4),
        "Result": (0.62, 0.2),
    }
    highlight_path = [("Start", "Option B"), ("Option B", "B1"), ("B1", "Result")]

    def draw_node(name, pos, emphasized=False):
        face = COLORS["muted"] if not emphasized else COLORS["accent"]
        text_color = COLORS["text"] if not emphasized else COLORS["background"]
        ax.add_patch(
            patches.FancyBboxPatch(
                (pos[0] - 0.08, pos[1] - 0.045),
                0.16,
                0.09,
                boxstyle="round,pad=0.03",
                facecolor=face,
                edgecolor=COLORS["accent"] if emphasized else COLORS["muted"],
                linewidth=2,
                alpha=1.0 if emphasized else 0.7,
            )
        )
        ax.text(pos[0], pos[1], name, ha="center", va="center", fontsize=24, color=text_color)

    for name, pos in nodes.items():
        emphasized = name in {"Start", "Option B", "B1", "Result"}
        draw_node(name, pos, emphasized=emphasized)

    for start, end in highlight_path:
        start_pos, end_pos = nodes[start], nodes[end]
        ax.annotate(
            "",
            xy=end_pos,
            xytext=start_pos,
            arrowprops=dict(
                arrowstyle="-|>",
                lw=3,
                color=COLORS["accent"],
            ),
        )

    muted_edges = [
        ("Start", "Option A"),
        ("Option A", "A1"),
        ("Option A", "A2"),
        ("Option B", "B2"),
    ]
    for start, end in muted_edges:
        start_pos, end_pos = nodes[start], nodes[end]
        ax.annotate(
            "",
            xy=end_pos,
            xytext=start_pos,
            arrowprops=dict(
                arrowstyle="-|>",
                lw=2,
                color=COLORS["muted"],
                alpha=0.5,
            ),
        )

    ax.text(
        0.05,
        0.1,
        "Most paths are explored and then set aside.",
        fontsize=26,
    )

    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def slide_six(path: str) -> None:
    fig, ax = create_base_figure("Iteration")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    drafts = [
        ("Draft 1", 0.25, 0.15, 0.5, 0.6, 0.35),
        ("Draft 2", 0.3, 0.2, 0.5, 0.6, 0.6),
        ("Draft 3", 0.35, 0.25, 0.5, 0.6, 0.85),
    ]
    for label, x, y, w, h, alpha in drafts:
        ax.add_patch(
            patches.FancyBboxPatch(
                (x, y),
                w,
                h,
                boxstyle="round,pad=0.05",
                facecolor=COLORS["accent"],
                edgecolor=COLORS["text"],
                linewidth=2,
                alpha=alpha,
            )
        )
        ax.text(
            x + w / 2,
            y + h + 0.03,
            label,
            ha="center",
            va="bottom",
            fontsize=28,
            color=COLORS["text"],
        )

    ax.text(
        0.5,
        0.48,
        "Each pass refines clarity and correctness.",
        ha="center",
        va="center",
        fontsize=30,
    )

    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def slide_seven(path: str) -> None:
    fig, ax = create_base_figure("The Meta-Cognitive Layer")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    layers = [
        ("Meta-Cognition", 0.2, 0.65, COLORS["accent"]),
        ("Monitoring", 0.2, 0.4, COLORS["highlight"]),
        ("Task Execution", 0.2, 0.15, COLORS["muted"]),
    ]

    for label, x, y, color in layers:
        ax.add_patch(
            patches.FancyBboxPatch(
                (x, y),
                0.6,
                0.2,
                boxstyle="round,pad=0.04",
                facecolor=color,
                edgecolor=COLORS["text"],
                linewidth=2.5,
            )
        )
        text_color = COLORS["background"] if color != COLORS["muted"] else COLORS["text"]
        ax.text(
            x + 0.3,
            y + 0.1,
            label,
            ha="center",
            va="center",
            fontsize=34,
            fontweight="bold",
            color=text_color,
        )

    ax.annotate(
        "",
        xy=(0.5, 0.75),
        xytext=(0.5, 0.55),
        arrowprops=dict(arrowstyle="->", lw=3, color=COLORS["text"]),
    )
    ax.annotate(
        "",
        xy=(0.5, 0.5),
        xytext=(0.5, 0.3),
        arrowprops=dict(arrowstyle="->", lw=3, color=COLORS["text"]),
    )

    ax.text(
        0.5,
        0.05,
        "Reflection guides oversight, which shapes execution.",
        ha="center",
        va="center",
        fontsize=26,
    )

    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def slide_eight(path: str) -> None:
    fig, ax = create_base_figure("Beyond Prompt and Response")
    ax.axis("off")
    fig.text(
        0.1,
        0.45,
        '"Quality is built in the hidden layer."',
        fontsize=56,
        color=COLORS["text"],
        fontweight="bold",
    )
    fig.text(
        0.1,
        0.25,
        "Embrace the unseen efforts that make an answer feel instant.",
        fontsize=30,
        color=COLORS["highlight"],
    )

    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    configure_style()
    output_dir = "visuals"
    os.makedirs(output_dir, exist_ok=True)
    slide_functions = [
        slide_one,
        slide_two,
        slide_three,
        slide_four,
        slide_five,
        slide_six,
        slide_seven,
        slide_eight,
    ]
    for idx, slide_fn in enumerate(slide_functions, start=1):
        filename = f"slide_{idx:02d}.png"
        path = os.path.join(output_dir, filename)
        slide_fn(path)
        print(f"Saved {path}")


if __name__ == "__main__":
    main()
