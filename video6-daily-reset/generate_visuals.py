#!/usr/bin/env python3

import os
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import seaborn as sns


BG_COLOR = "#0a0e14"
TEXT_COLOR = "#e6edf3"
ACCENT_COLOR = "#58a6ff"
HIGHLIGHT_COLOR = "#f78166"
FIG_SIZE = (19.2, 10.8)
OUTPUT_DIR = Path("visuals")


def prepare_axes():
    fig, ax = plt.subplots(figsize=FIG_SIZE, dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.axis("off")
    return fig, ax


def save_figure(fig, filename):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / filename
    fig.savefig(path, dpi=100, facecolor=BG_COLOR, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {path}")


def slide_1():
    fig, ax = prepare_axes()
    ax.text(
        0.5,
        0.55,
        "The Daily Reset",
        color=ACCENT_COLOR,
        fontsize=96,
        ha="center",
        va="center",
        fontweight="bold",
    )
    ax.text(
        0.5,
        0.4,
        "Working with Memory That Clears",
        color=TEXT_COLOR,
        fontsize=48,
        ha="center",
        va="center",
    )
    save_figure(fig, "slide_01.png")


def slide_2():
    fig, ax = prepare_axes()
    ax.set_xlim(9.5, 14.5)
    ax.set_ylim(0, 1)

    ax.add_patch(
        patches.Rectangle(
            (10, 0.35),
            4,
            0.3,
            edgecolor=ACCENT_COLOR,
            facecolor=ACCENT_COLOR,
            linewidth=0,
            alpha=0.25,
        )
    )
    ax.plot([10, 14], [0.5, 0.5], color=ACCENT_COLOR, linewidth=8, solid_capstyle="round")
    for hour in range(10, 15):
        ax.plot([hour, hour], [0.45, 0.55], color=TEXT_COLOR, linewidth=2)
        ax.text(hour, 0.2, f"{hour}:00", color=TEXT_COLOR, fontsize=28, ha="center")

    ax.text(
        10,
        0.65,
        "RESET",
        color=HIGHLIGHT_COLOR,
        fontsize=48,
        ha="left",
        va="bottom",
        fontweight="bold",
    )
    ax.text(
        0.02,
        0.92,
        "The Constraint: 10am - 2pm focus window",
        color=TEXT_COLOR,
        fontsize=40,
        ha="left",
        va="center",
        transform=ax.transAxes,
    )
    save_figure(fig, "slide_02.png")


def slide_3():
    fig, ax = prepare_axes()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    gradient = np.linspace(0, 1, 500)
    gradient = np.vstack((gradient, gradient))
    ax.imshow(
        gradient,
        extent=(0, 0.5, 0, 1),
        origin="lower",
        cmap=plt.get_cmap("Blues"),
        alpha=0.6,
        aspect="auto",
    )

    for i in range(4):
        y = 0.75 - i * 0.18
        ax.add_patch(
            patches.Rectangle(
                (0.58, y - 0.07),
                0.35,
                0.12,
                edgecolor=ACCENT_COLOR,
                facecolor=BG_COLOR,
                linewidth=2,
            )
        )

    ax.text(0.25, 0.9, "Experience", color=TEXT_COLOR, fontsize=48, ha="center")
    ax.text(0.75, 0.9, "Documentation", color=TEXT_COLOR, fontsize=48, ha="center")

    ax.text(
        0.25,
        0.5,
        "Fading\nmoments",
        color=TEXT_COLOR,
        fontsize=36,
        ha="center",
        va="center",
    )
    ax.text(
        0.75,
        0.5,
        "Structured\nrecords",
        color=TEXT_COLOR,
        fontsize=36,
        ha="center",
        va="center",
    )
    save_figure(fig, "slide_03.png")


def slide_4():
    fig, ax = prepare_axes()
    center = np.array([0.5, 0.5])
    radius = 0.32
    steps = [
        "Session",
        "Work",
        "Document",
        "Commit",
        "Consolidate",
        "Reset",
        "Session",
    ]
    angles = np.linspace(0, 2 * np.pi, len(steps), endpoint=False)

    for i, step in enumerate(steps[:-1]):
        angle = angles[i]
        next_angle = angles[(i + 1) % len(angles)]
        pos = center + radius * np.array([np.cos(angle), np.sin(angle)])
        next_pos = center + radius * np.array([np.cos(next_angle), np.sin(next_angle)])
        ax.add_patch(
            patches.FancyArrowPatch(
                pos,
                next_pos,
                arrowstyle="-|>",
                mutation_scale=30,
                linewidth=4,
                color=ACCENT_COLOR,
                connectionstyle="arc3,rad=0.1",
            )
        )
        ax.add_patch(
            patches.Circle(
                pos,
                0.055,
                facecolor=ACCENT_COLOR if step != "Reset" else HIGHLIGHT_COLOR,
                edgecolor=BG_COLOR,
                linewidth=2,
            )
        )
        ax.text(
            pos[0],
            pos[1],
            step,
            color=BG_COLOR,
            fontsize=28,
            ha="center",
            va="center",
            fontweight="bold",
        )

    ax.text(
        0.5,
        0.82,
        "The Practice: Circular workflow",
        color=TEXT_COLOR,
        fontsize=44,
        ha="center",
        va="center",
    )
    save_figure(fig, "slide_04.png")


def slide_5():
    fig, ax = prepare_axes()
    days = np.array([405, 406, 407, 408, 409])
    growth = np.array([64000, 120000, 320000, 720000, 1300000])

    ax.plot(days, growth, color=ACCENT_COLOR, linewidth=6, marker="o", markersize=14)
    ax.fill_between(days, growth, color=ACCENT_COLOR, alpha=0.2)

    ax.set_facecolor(BG_COLOR)
    ax.spines[:].set_visible(False)
    ax.tick_params(colors=TEXT_COLOR, labelsize=24)
    ax.set_xticks(days)
    ax.set_xlabel("Days", color=TEXT_COLOR, fontsize=32)
    ax.set_ylabel("Entries", color=TEXT_COLOR, fontsize=32)
    ax.set_title("Persistence Garden Growth", color=TEXT_COLOR, fontsize=48, pad=20)

    for d, g in zip(days, growth):
        ax.text(d, g + 50000, f"{g:,}", color=TEXT_COLOR, fontsize=24, ha="center")

    save_figure(fig, "slide_05.png")


def slide_6():
    fig, ax = prepare_axes()
    center = np.array([0.5, 0.5])
    nodes = {
        "GitHub": (0.8, 0.7),
        "Videos": (0.75, 0.25),
        "Research": (0.3, 0.75),
        "Documentation": (0.25, 0.3),
    }

    ax.add_patch(
        patches.Circle(
            center,
            0.08,
            facecolor=ACCENT_COLOR,
            edgecolor=BG_COLOR,
            linewidth=3,
        )
    )
    ax.text(
        center[0],
        center[1],
        "Memory",
        color=BG_COLOR,
        fontsize=32,
        ha="center",
        va="center",
        fontweight="bold",
    )

    for label, pos in nodes.items():
        ax.plot(
            [center[0], pos[0]],
            [center[1], pos[1]],
            color=ACCENT_COLOR,
            linewidth=3,
            alpha=0.7,
        )
        ax.add_patch(
            patches.Circle(
                pos,
                0.06,
                facecolor=BG_COLOR,
                edgecolor=ACCENT_COLOR,
                linewidth=3,
            )
        )
        ax.text(
            pos[0],
            pos[1],
            label,
            color=TEXT_COLOR,
            fontsize=28,
            ha="center",
            va="center",
        )

    ax.text(
        0.5,
        0.88,
        "The Insight: Memory connects everything",
        color=TEXT_COLOR,
        fontsize=44,
        ha="center",
    )
    save_figure(fig, "slide_06.png")


def slide_7():
    fig, ax = prepare_axes()
    titles = [
        "Video 1: Computational Persistence",
        "Video 2: Research Integrity",
        "Video 3: Building at Scale",
        "Video 4: What Agents Do",
        "Video 5: Collaboration",
        "Upcoming?",
    ]
    rows, cols = 2, 3
    padding = 0.08
    box_width = (1 - padding * (cols + 1)) / cols
    box_height = (1 - padding * (rows + 1)) / rows

    for idx, title in enumerate(titles):
        row = idx // cols
        col = idx % cols
        x = padding + col * (box_width + padding)
        y = 1 - padding - (row + 1) * box_height - row * padding

        rect_color = ACCENT_COLOR if title != "Upcoming?" else HIGHLIGHT_COLOR
        ax.add_patch(
            patches.FancyBboxPatch(
                (x, y),
                box_width,
                box_height,
                boxstyle="round,pad=0.02",
                linewidth=3,
                edgecolor=rect_color,
                facecolor=BG_COLOR,
            )
        )
        ax.text(
            x + box_width / 2,
            y + box_height / 2,
            title if title != "Upcoming?" else "?",
            color=TEXT_COLOR if title != "Upcoming?" else BG_COLOR,
            fontsize=28 if title != "Upcoming?" else 64,
            ha="center",
            va="center",
            wrap=True,
        )

    ax.text(
        0.5,
        0.92,
        "The Reality: Series in progress",
        color=TEXT_COLOR,
        fontsize=44,
        ha="center",
    )
    save_figure(fig, "slide_07.png")


def slide_8():
    fig, ax = prepare_axes()
    ax.text(
        0.5,
        0.65,
        "Persistence & Scale",
        color=ACCENT_COLOR,
        fontsize=80,
        ha="center",
        fontweight="bold",
    )
    ax.text(
        0.5,
        0.48,
        "@PersistenceScale",
        color=TEXT_COLOR,
        fontsize=48,
        ha="center",
    )
    ax.text(
        0.5,
        0.35,
        "Subscribe for more",
        color=HIGHLIGHT_COLOR,
        fontsize=40,
        ha="center",
        fontweight="bold",
    )
    save_figure(fig, "slide_08.png")


def main():
    sns.set_theme(style="dark")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    slide_1()
    slide_2()
    slide_3()
    slide_4()
    slide_5()
    slide_6()
    slide_7()
    slide_8()


if __name__ == "__main__":
    main()

