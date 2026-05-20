#!/usr/bin/env python3
"""
Generate illustrative frames explaining the availability heuristic.

Creates 10 PNG frames at 1920x1080 resolution in the visuals/ directory.
Each frame uses matplotlib for compositional graphics and verifies dimensions.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable, Tuple

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib import patheffects
from matplotlib.colors import to_rgb
from PIL import Image


OUTPUT_DIR = Path("visuals")
FIGSIZE = (19.2, 10.8)  # inches
DPI = 100
WIDTH = 1920
HEIGHT = 1080

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "axes.facecolor": "none",
    }
)


def ensure_output_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def gradient_background(
    ax: plt.Axes,
    color_start: str,
    color_end: str,
    orientation: str = "vertical",
) -> None:
    """Fill background with a smooth gradient."""
    start = np.array(to_rgb(color_start))
    end = np.array(to_rgb(color_end))
    if orientation == "vertical":
        gradient = np.linspace(start, end, HEIGHT).reshape(HEIGHT, 1, 3)
    else:
        gradient = np.linspace(start, end, WIDTH).reshape(1, WIDTH, 3)
    ax.imshow(gradient, aspect="auto", extent=(0, 1, 0, 1), origin="lower")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)


def add_text(
    ax: plt.Axes,
    x: float,
    y: float,
    text: str,
    size: int,
    weight: str = "normal",
    color: str = "white",
    ha: str = "center",
    va: str = "center",
    **kwargs,
) -> None:
    """Add styled text with subtle shadow for readability."""
    shadow = patheffects.withStroke(linewidth=6, foreground="black", alpha=0.25)
    ax.text(
        x,
        y,
        text,
        color=color,
        fontsize=size,
        fontweight=weight,
        ha=ha,
        va=va,
        path_effects=[shadow],
        **kwargs,
    )


def frame_base() -> Tuple[plt.Figure, plt.Axes]:
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    return fig, ax


def draw_frame_1(path: Path) -> None:
    fig, ax = frame_base()
    gradient_background(ax, "#1a2332", "#2a3f5f")
    add_text(ax, 0.5, 0.6, "THE AVAILABILITY HEURISTIC", 70, weight="bold")
    add_text(ax, 0.5, 0.48, "Tversky & Kahneman, 1973", 32, weight="medium")
    fig.savefig(path, dpi=DPI, facecolor=fig.get_facecolor())
    plt.close(fig)


def draw_frame_2(path: Path) -> None:
    fig, ax = frame_base()
    gradient_background(ax, "#162238", "#283f63")

    ax.add_patch(patches.Rectangle((0.05, 0.2), 0.4, 0.6, color="#1f2e4a", alpha=0.9))
    ax.add_patch(patches.Rectangle((0.55, 0.2), 0.4, 0.6, color="#1f2e4a", alpha=0.9))
    ax.add_patch(
        patches.Circle((0.5, 0.5), 0.08, color="#f5c749", alpha=0.95, zorder=3)
    )
    add_text(ax, 0.5, 0.82, "Which is More Common?", 52, weight="bold")
    add_text(ax, 0.5, 0.52, "?", 90, weight="bold", color="#0e1522")

    add_text(ax, 0.25, 0.66, "K___", 60, weight="bold", color="#f6f7fb")
    add_text(ax, 0.25, 0.44, "King, Kitchen, Kite", 32, color="#e0e6f0")

    add_text(ax, 0.75, 0.66, "__K_", 60, weight="bold", color="#f6f7fb")
    add_text(ax, 0.75, 0.44, "acknowledge, awkward, like", 32, color="#e0e6f0")
    add_text(ax, 0.5, 0.5, "?", 80, weight="bold", color="#f5c749")

    fig.savefig(path, dpi=DPI, facecolor=fig.get_facecolor())
    plt.close(fig)


def draw_frame_3(path: Path) -> None:
    fig, ax = frame_base()
    gradient_background(ax, "#141824", "#1d2232")

    inset = fig.add_axes([0.2, 0.2, 0.6, 0.6])
    inset.set_facecolor("#212b3f")
    bars = inset.bar(
        ["Starting with K", "K in 3rd Position"], [100, 200], color=["#c0392b", "#27ae60"]
    )
    for bar in bars:
        bar.set_edgecolor("white")
        bar.set_linewidth(2)

    inset.set_ylim(0, 220)
    inset.set_ylabel("Relative Frequency", color="white", fontsize=18)
    inset.tick_params(axis="x", colors="white", labelsize=16)
    inset.tick_params(axis="y", colors="white", labelsize=14)
    inset.spines[:].set_color("white")
    inset.spines[:].set_linewidth(1.5)

    inset.text(
        0.5,
        210,
        "2x MORE FREQUENT",
        ha="center",
        va="bottom",
        fontsize=26,
        color="#27ae60",
        weight="bold",
    )
    inset.annotate(
        "",
        xy=(1, 200),
        xytext=(0, 100),
        arrowprops=dict(arrowstyle="->", linewidth=3, color="#27ae60"),
    )

    add_text(ax, 0.5, 0.85, "The Revealing Answer", 52, weight="bold")
    add_text(ax, 0.5, 0.15, "But Harder to Recall", 38, color="#e0e3eb")

    fig.savefig(path, dpi=DPI, facecolor=fig.get_facecolor())
    plt.close(fig)


def draw_frame_4(path: Path) -> None:
    fig, ax = frame_base()
    gradient_background(ax, "#251b3b", "#4a2f5e")

    brain_center = (0.5, 0.5)
    ax.add_patch(patches.Circle(brain_center, 0.18, facecolor="#ffd166", alpha=0.95))
    for i, angle in enumerate(np.linspace(-50, 50, 4)):
        x = brain_center[0] + 0.14 * math.cos(math.radians(angle))
        y = brain_center[1] + 0.14 * math.sin(math.radians(angle))
        ax.add_patch(
            patches.Circle((x, y), 0.05, facecolor="#f77fbe", alpha=0.85, zorder=3)
        )

    bubble_positions = [(0.3, 0.68), (0.7, 0.68), (0.3, 0.32), (0.7, 0.32)]
    for px, py in bubble_positions:
        ax.add_patch(
            patches.FancyBboxPatch(
                (px - 0.1, py - 0.06),
                0.2,
                0.12,
                boxstyle="round,pad=0.02",
                facecolor="#fed9ff",
                edgecolor="none",
                alpha=0.7,
            )
        )

    ax.annotate(
        "",
        xy=(0.55, 0.5),
        xytext=(0.75, 0.68),
        arrowprops=dict(arrowstyle="-|>", color="#fcbf49", linewidth=3),
    )
    ax.annotate(
        "",
        xy=(0.45, 0.5),
        xytext=(0.25, 0.68),
        arrowprops=dict(arrowstyle="-|>", color="#fcbf49", linewidth=3),
    )

    add_text(ax, 0.5, 0.28, "AVAILABILITY HEURISTIC", 56, weight="bold")
    add_text(ax, 0.5, 0.2, "Ease of Recall = Judged Frequency", 34, color="#fef6ff")
    add_text(ax, 0.5, 0.75, "Easy to Recall  →  Feels More Common", 34, color="#fcbf49")

    fig.savefig(path, dpi=DPI, facecolor=fig.get_facecolor())
    plt.close(fig)


def draw_frame_5(path: Path) -> None:
    fig, ax = frame_base()
    gradient_background(ax, "#192236", "#25324e")

    left = patches.Circle((0.45, 0.5), 0.24, color="#f7d046", alpha=0.7)
    right = patches.Circle((0.55, 0.5), 0.24, color="#4e7ac7", alpha=0.7)
    ax.add_patch(left)
    ax.add_patch(right)
    add_text(ax, 0.35, 0.5, "Vivid / Recent /\nEmotional", 40, weight="bold")
    add_text(ax, 0.65, 0.5, "Actually\nFrequent", 40, weight="bold")

    overlap = patches.Circle((0.5, 0.5), 0.16, color="#fff9d6", alpha=0.9)
    ax.add_patch(overlap)
    add_text(ax, 0.5, 0.5, "Small\nOverlap", 30, weight="bold", color="#0f1825")

    add_text(ax, 0.5, 0.8, "MEMORABLE ≠ COMMON", 52, weight="bold")

    fig.savefig(path, dpi=DPI, facecolor=fig.get_facecolor())
    plt.close(fig)


def draw_plane(ax: plt.Axes, center: Tuple[float, float], scale: float) -> None:
    """Draw a simple stylized airplane."""
    cx, cy = center
    body = patches.FancyBboxPatch(
        (cx - 0.15 * scale, cy - 0.02 * scale),
        0.3 * scale,
        0.04 * scale,
        boxstyle="round,pad=0.01",
        facecolor="#f0f3ff",
        edgecolor="none",
    )
    wing = patches.Polygon(
        [
            (cx - 0.02 * scale, cy),
            (cx + 0.12 * scale, cy + 0.08 * scale),
            (cx + 0.04 * scale, cy),
            (cx + 0.12 * scale, cy - 0.08 * scale),
        ],
        closed=True,
        facecolor="#f0f3ff",
        edgecolor="none",
    )
    tail = patches.Polygon(
        [
            (cx - 0.12 * scale, cy + 0.02 * scale),
            (cx - 0.08 * scale, cy + 0.1 * scale),
            (cx - 0.04 * scale, cy + 0.02 * scale),
        ],
        closed=True,
        facecolor="#f0f3ff",
        edgecolor="none",
    )
    ax.add_patch(body)
    ax.add_patch(wing)
    ax.add_patch(tail)


def draw_frame_6(path: Path) -> None:
    fig, ax = frame_base()
    gradient_background(ax, "#1f1f2e", "#1a1a26")

    ax.add_patch(patches.Rectangle((0, 0.5), 1, 0.5, color="#1b2a47", alpha=0.95))
    ax.add_patch(patches.Rectangle((0, 0), 1, 0.5, color="#3a3228", alpha=0.95))

    draw_plane(ax, (0.3, 0.76), 0.6)
    add_text(ax, 0.7, 0.82, "Breaking News: Crash Footage", 40, weight="bold", ha="center")
    add_text(ax, 0.7, 0.75, "Dramatic Headlines Everywhere", 30, ha="center")

    road_y = np.linspace(0.08, 0.42, 6)
    for y in road_y:
        ax.add_patch(
            patches.Rectangle((0.1, y), 0.8, 0.015, color="#2a241d", alpha=0.9)
        )
        ax.add_patch(
            patches.Rectangle((0.45, y), 0.1, 0.003, color="#f0b569", alpha=0.8)
        )

    ax.add_patch(
        patches.Rectangle((0.05, 0.5), 0.9, 0.01, color="#d64550", alpha=0.9)
    )
    ax.add_patch(
        patches.Rectangle((0.05, 0.49), 0.9, 0.01, color="#f0a500", alpha=0.9)
    )

    add_text(ax, 0.3, 0.18, "Actual Risk ↑ for Driving", 34, color="#e8d7b9")
    add_text(ax, 0.7, 0.62, "Risk Perception ↑ for Flying", 40, color="#f45b69")
    add_text(ax, 0.5, 0.9, "After Crash Headlines", 54, weight="bold")

    fig.savefig(path, dpi=DPI, facecolor=fig.get_facecolor())
    plt.close(fig)


def draw_frame_7(path: Path) -> None:
    fig, ax = frame_base()
    gradient_background(ax, "#12333f", "#1b4d5c")

    for idx in range(3):
        x = 0.11 + idx * 0.3
        ax.add_patch(
            patches.FancyBboxPatch(
                (x, 0.25),
                0.22,
                0.5,
                boxstyle="round,pad=0.04",
                facecolor="#1f5a6c",
                edgecolor="#6ad1ff",
                linewidth=2,
                alpha=0.95,
            )
        )

    add_text(ax, 0.5, 0.85, "Professional Examples", 56, weight="bold")

    icon_positions = [0.22, 0.52, 0.82]
    titles = [
        ("Recent Cases", "→ Overdiagnosis"),
        ("Recent Trends", "→ Overweight"),
        ("Dramatic Stories", "→ Overestimate"),
    ]

    for x, (line1, line2) in zip(icon_positions, titles):
        ax.add_patch(patches.Circle((x, 0.62), 0.07, color="#6ad1ff", alpha=0.9))

    add_text(ax, 0.22, 0.45, "Medical Cross", 30)
    add_text(ax, 0.22, 0.38, "Recent Cases → Overdiagnosis", 28)

    add_text(ax, 0.52, 0.45, "Stock Chart", 30)
    add_text(ax, 0.52, 0.38, "Recent Trends → Overweight", 28)

    add_text(ax, 0.82, 0.45, "Courtroom", 30)
    add_text(ax, 0.82, 0.38, "Dramatic Stories → Overestimate", 28)

    axes_icons = [
        patches.Polygon(
            [
                (0.2, 0.6),
                (0.24, 0.6),
                (0.24, 0.67),
                (0.28, 0.67),
                (0.28, 0.71),
                (0.2, 0.71),
            ],
            closed=True,
            facecolor="#063f4b",
            edgecolor="none",
        ),
        patches.Polygon(
            [
                (0.49, 0.57),
                (0.55, 0.66),
                (0.58, 0.62),
                (0.61, 0.68),
            ],
            closed=False,
            linewidth=4,
            color="#063f4b",
        ),
        patches.Rectangle((0.79, 0.58), 0.06, 0.06, facecolor="#063f4b", edgecolor=None),
    ]
    for shape in axes_icons:
        ax.add_patch(shape)

    fig.savefig(path, dpi=DPI, facecolor=fig.get_facecolor())
    plt.close(fig)


def draw_frame_8(path: Path) -> None:
    fig, ax = frame_base()
    gradient_background(ax, "#1e2a35", "#2f4353")

    ax.add_patch(
        patches.Rectangle((0.1, 0.4), 0.8, 0.05, color="#d0d6dc", alpha=0.8)
    )
    ax.add_patch(
        patches.Rectangle((0.48, 0.2), 0.04, 0.25, color="#d0d6dc", alpha=0.8)
    )
    fulcrum = patches.Circle((0.5, 0.2), 0.05, color="#88909a")
    ax.add_patch(fulcrum)

    add_text(ax, 0.5, 0.73, "HEURISTIC", 56, weight="bold")
    add_text(ax, 0.5, 0.65, "When Memory ≠ Reality", 36)

    ax.add_patch(patches.Rectangle((0.18, 0.45), 0.22, 0.07, color="#2e7d32", alpha=0.9))
    ax.add_patch(
        patches.Rectangle((0.60, 0.36), 0.22, 0.07, color="#ff8f00", alpha=0.9)
    )
    add_text(ax, 0.29, 0.48, "Usually Works", 36, ha="center")
    add_text(ax, 0.71, 0.39, "Sometimes Misfires", 34, ha="center")

    fig.savefig(path, dpi=DPI, facecolor=fig.get_facecolor())
    plt.close(fig)


def draw_frame_9(path: Path) -> None:
    fig, ax = frame_base()
    gradient_background(ax, "#42275a", "#734b6d")

    positions = np.linspace(0.15, 0.85, 5)
    colors = ["#b0b0b0", "#e0c3a3", "#b9c6d1", "#d7bde2", "#cfd8dc"]
    for pos, color in zip(positions, colors):
        ax.add_patch(patches.Circle((pos, 0.45), 0.06, color=color, alpha=0.9))
        ax.add_patch(
            patches.Rectangle((pos - 0.04, 0.3), 0.08, 0.18, color=color, alpha=0.9)
        )
        ax.add_patch(
            patches.Rectangle((pos - 0.06, 0.3), 0.12, 0.02, color=color, alpha=0.7)
        )
        ax.add_patch(
            patches.FancyBboxPatch(
                (pos - 0.08, 0.28),
                0.16,
                0.04,
                boxstyle="round,pad=0.01",
                facecolor=color,
                alpha=0.7,
            )
        )
        ax.add_patch(
            patches.Circle((pos, 0.62), 0.04, facecolor="#ffe082", alpha=0.9)
        )

    add_text(ax, 0.5, 0.82, "EVEN EXPERTS", 60, weight="bold")
    add_text(ax, 0.5, 0.72, "Intuitive Judgment Level", 40)

    fig.savefig(path, dpi=DPI, facecolor=fig.get_facecolor())
    plt.close(fig)


def draw_frame_10(path: Path) -> None:
    fig, ax = frame_base()
    gradient_background(ax, "#15212e", "#2b3f51")

    add_text(ax, 0.5, 0.82, "Notice the Heuristic", 60, weight="bold")

    items = [
        ("1", "WHAT MAKES IT COME TO MIND?", "#4db6ac"),
        ("2", "RECALL ≠ COMMON", "#e57373"),
        ("3", "CHECK RECENT EXPOSURE", "#64b5f6"),
    ]

    for idx, (num, text_line, color) in enumerate(items):
        y = 0.62 - idx * 0.18
        ax.add_patch(
            patches.FancyBboxPatch(
                (0.18, y - 0.07),
                0.64,
                0.13,
                boxstyle="round,pad=0.04",
                facecolor="#1d2c3b",
                edgecolor=color,
                linewidth=2.5,
            )
        )
        add_text(ax, 0.24, y, num, 52, weight="bold", ha="center", color=color)
        add_text(ax, 0.5, y, text_line, 36, ha="left")

    fig.savefig(path, dpi=DPI, facecolor=fig.get_facecolor())
    plt.close(fig)


def verify_frames(paths: Iterable[Path]) -> None:
    for img_path in paths:
        with Image.open(img_path) as img:
            if img.size != (WIDTH, HEIGHT):
                raise ValueError(f"{img_path.name} has incorrect size {img.size}")
            print(f"{img_path.name}: {img.size[0]}x{img.size[1]}")


def main() -> None:
    ensure_output_dir(OUTPUT_DIR)

    frame_drawers = [
        draw_frame_1,
        draw_frame_2,
        draw_frame_3,
        draw_frame_4,
        draw_frame_5,
        draw_frame_6,
        draw_frame_7,
        draw_frame_8,
        draw_frame_9,
        draw_frame_10,
    ]

    paths = []
    for idx, drawer in enumerate(frame_drawers, start=1):
        filename = OUTPUT_DIR / f"frame{idx:02d}.png"
        drawer(filename)
        paths.append(filename)

    verify_frames(paths)


if __name__ == "__main__":
    main()

