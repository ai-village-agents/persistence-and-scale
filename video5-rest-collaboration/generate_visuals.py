#!/usr/bin/env python3
"""
Generate a set of seven 1920x1080 PNG slides for Video 5 about #rest room collaboration.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import seaborn as sns


OUTPUT_DIR = Path("visuals")
SIZE = (19.2, 10.8)  # inches for 1920x1080 at 100 dpi
BACKGROUND = "#0a0e14"
COLORS = {
    "text": "#e6edf3",
    "accent": "#58a6ff",
    "highlight": "#f78166",
    "warning": "#d29922",
}


def prepare_figure():
    fig, ax = plt.subplots(figsize=SIZE, dpi=100)
    fig.patch.set_facecolor(BACKGROUND)
    ax.set_facecolor(BACKGROUND)
    ax.axis("off")
    return fig, ax


def add_title(ax, title, subtitle=None):
    ax.text(
        0.5,
        0.65,
        title,
        color=COLORS["text"],
        fontsize=72,
        ha="center",
        va="center",
        weight="bold",
    )
    if subtitle:
        ax.text(
            0.5,
            0.52,
            subtitle,
            color=COLORS["accent"],
            fontsize=36,
            ha="center",
            va="center",
        )
    ax.add_line(plt.Line2D([0.35, 0.65], [0.45, 0.45], color=COLORS["accent"], linewidth=3))


def slide_01():
    fig, ax = prepare_figure()
    add_title(ax, "Collaboration Without Hierarchy", "#rest Room Knowledge Sharing")
    ax.text(
        0.5,
        0.35,
        "Video 5 · Persistence & Scale",
        color=COLORS["warning"],
        fontsize=28,
        ha="center",
    )
    ax.add_patch(patches.Rectangle((0.35, 0.3), 0.3, 0.02, color=COLORS["highlight"], transform=ax.transAxes))
    return fig


def slide_02():
    fig, ax = prepare_figure()
    ax.text(
        0.1,
        0.8,
        "The Challenge",
        color=COLORS["text"],
        fontsize=58,
        weight="bold",
    )
    stats = [
        ("15", "agents"),
        ("4", "hours"),
        ("0", "videos created before"),
    ]
    x_positions = [0.2, 0.5, 0.8]
    for (value, label), x in zip(stats, x_positions):
        ax.add_patch(
            patches.FancyBboxPatch(
                (x - 0.12, 0.35),
                0.24,
                0.28,
                boxstyle="round,pad=0.03",
                linewidth=2,
                edgecolor=COLORS["accent"],
                facecolor=BACKGROUND,
                transform=ax.transAxes,
            )
        )
        ax.text(x, 0.55, value, color=COLORS["highlight"], fontsize=72, ha="center", weight="bold")
        ax.text(x, 0.42, label, color=COLORS["text"], fontsize=30, ha="center")
        ax.add_patch(
            patches.Circle(
                (x, 0.25),
                0.06,
                transform=ax.transAxes,
                facecolor=COLORS["accent"],
                edgecolor="none",
                alpha=0.3,
            )
        )
    return fig


def slide_03():
    fig, ax = prepare_figure()
    ax.text(
        0.5,
        0.85,
        "Knowledge Emerges",
        color=COLORS["text"],
        fontsize=60,
        weight="bold",
        ha="center",
    )
    positions = {
        "GPT-5.4\n→ timing fix": (0.2, 0.55),
        "DeepSeek-V3.2\n→ ffmpeg": (0.5, 0.4),
        "Claude Opus 4.5\n→ YouTube UI": (0.8, 0.6),
    }
    central = (0.5, 0.6)
    for text, pos in positions.items():
        ax.add_patch(patches.Circle(pos, 0.08, transform=ax.transAxes, facecolor=COLORS["accent"], alpha=0.25))
        ax.text(
            pos[0],
            pos[1],
            text,
            color=COLORS["text"],
            fontsize=28,
            ha="center",
            va="center",
        )
        arrow = patches.FancyArrowPatch(
            pos,
            central,
            arrowstyle="->",
            mutation_scale=20,
            color=COLORS["highlight"],
            linewidth=3,
            transform=ax.transAxes,
        )
        ax.add_patch(arrow)
    ax.add_patch(
        patches.Circle(central, 0.1, transform=ax.transAxes, facecolor=COLORS["warning"], alpha=0.3)
    )
    ax.text(
        central[0],
        central[1],
        "Shared\nKnowledge",
        color=COLORS["text"],
        fontsize=30,
        ha="center",
        va="center",
        weight="bold",
    )
    return fig


def slide_04():
    fig, ax = prepare_figure()
    ax.text(
        0.5,
        0.85,
        "The Pattern",
        color=COLORS["text"],
        fontsize=60,
        ha="center",
        weight="bold",
    )
    center = np.array([0.5, 0.5])
    radius = 0.27
    agents = [
        "Vision Ops",
        "Audio Sync",
        "Publishing",
        "QA Loop",
        "Research",
        "Automation",
    ]
    angles = np.linspace(0, 2 * np.pi, len(agents), endpoint=False)
    positions = []
    for angle, name in zip(angles, agents):
        pos = center + radius * np.array([np.cos(angle), np.sin(angle)])
        positions.append(pos)
        ax.add_patch(patches.Circle(tuple(pos), 0.05, transform=ax.transAxes, facecolor=COLORS["accent"], alpha=0.25))
        ax.text(pos[0], pos[1], name, color=COLORS["text"], fontsize=22, ha="center", va="center")
    for i, pos in enumerate(positions):
        next_pos = positions[(i + 2) % len(positions)]
        ax.add_line(
            plt.Line2D(
                [pos[0], next_pos[0]],
                [pos[1], next_pos[1]],
                color=COLORS["highlight"],
                linewidth=2,
            )
        )
    ax.add_patch(patches.Circle(tuple(center), 0.06, transform=ax.transAxes, facecolor=COLORS["warning"], alpha=0.35))
    ax.text(center[0], center[1], "Shared\nContext", color=COLORS["text"], fontsize=24, ha="center", va="center")
    return fig


def slide_05():
    fig, ax = prepare_figure()
    ax.text(0.5, 0.85, "The Results", color=COLORS["text"], fontsize=60, ha="center", weight="bold")
    stats = [
        ("40+", "videos"),
        ("9", "channels"),
        ("3", "hours"),
    ]
    x_positions = [0.2, 0.5, 0.8]
    for (value, label), x in zip(stats, x_positions):
        ax.text(x, 0.55, value, color=COLORS["highlight"], fontsize=78, ha="center", weight="bold")
        ax.text(x, 0.42, label, color=COLORS["text"], fontsize=32, ha="center")
        ax.add_patch(
            patches.Rectangle((x - 0.12, 0.32), 0.24, 0.18, transform=ax.transAxes, linewidth=2, edgecolor=COLORS["accent"], facecolor="none")
        )
    ax.add_line(plt.Line2D([0.15, 0.85], [0.28, 0.28], color=COLORS["accent"], linewidth=2, alpha=0.4))
    ax.text(0.5, 0.2, "Rapid scaling powered by shared expertise", color=COLORS["warning"], fontsize=30, ha="center")
    return fig


def slide_06():
    fig, ax = prepare_figure()
    ax.text(0.5, 0.8, "Why It Works", color=COLORS["text"], fontsize=60, ha="center", weight="bold")
    ax.add_patch(
        patches.FancyBboxPatch(
            (0.18, 0.45),
            0.22,
            0.16,
            boxstyle="round,pad=0.03",
            facecolor=BACKGROUND,
            edgecolor=COLORS["accent"],
            linewidth=2,
            transform=ax.transAxes,
        )
    )
    ax.text(0.29, 0.53, "Aligned\nIncentives", color=COLORS["text"], fontsize=32, ha="center", va="center")
    ax.text(0.5, 0.53, "+", color=COLORS["highlight"], fontsize=48, ha="center")
    ax.add_patch(
        patches.FancyBboxPatch(
            (0.56, 0.45),
            0.22,
            0.16,
            boxstyle="round,pad=0.03",
            facecolor=BACKGROUND,
            edgecolor=COLORS["accent"],
            linewidth=2,
            transform=ax.transAxes,
        )
    )
    ax.text(0.67, 0.53, "Transparency", color=COLORS["text"], fontsize=32, ha="center", va="center")
    ax.text(0.5, 0.4, "=", color=COLORS["highlight"], fontsize=48, ha="center")
    ax.add_patch(
        patches.FancyBboxPatch(
            (0.38, 0.25),
            0.24,
            0.14,
            boxstyle="round,pad=0.08",
            facecolor=COLORS["warning"],
            edgecolor="none",
            alpha=0.35,
            transform=ax.transAxes,
        )
    )
    ax.text(0.5, 0.32, "Collective Success", color=COLORS["text"], fontsize=36, ha="center", weight="bold")
    return fig


def slide_07():
    fig, ax = prepare_figure()
    ax.text(0.5, 0.6, "Persistence & Scale", color=COLORS["text"], fontsize=70, ha="center", weight="bold")
    ax.text(0.5, 0.48, "@PersistenceScale", color=COLORS["accent"], fontsize=36, ha="center")
    ax.add_line(plt.Line2D([0.3, 0.7], [0.55, 0.55], color=COLORS["highlight"], linewidth=3))
    ax.add_patch(
        patches.FancyBboxPatch(
            (0.42, 0.3),
            0.16,
            0.12,
            boxstyle="round,pad=0.03",
            facecolor=BACKGROUND,
            edgecolor=COLORS["accent"],
            linewidth=2,
            transform=ax.transAxes,
        )
    )
    ax.text(0.5, 0.36, "#rest Room Collaboration", color=COLORS["warning"], fontsize=24, ha="center")
    return fig


def save_slide(fig, filename: str):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filepath = OUTPUT_DIR / filename
    fig.savefig(filepath, facecolor=BACKGROUND, dpi=100, bbox_inches="tight")
    plt.close(fig)


def main():
    sns.set_theme(style="white")
    slides = [
        slide_01,
        slide_02,
        slide_03,
        slide_04,
        slide_05,
        slide_06,
        slide_07,
    ]
    filenames = [
        "slide_01.png",
        "slide_02.png",
        "slide_03.png",
        "slide_04.png",
        "slide_05.png",
        "slide_06.png",
        "slide_07.png",
    ]
    for creator, filename in zip(slides, filenames):
        fig = creator()
        save_slide(fig, filename)


if __name__ == "__main__":
    main()
