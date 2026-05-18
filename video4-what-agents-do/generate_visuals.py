"""Generate presentation visuals for the AI agents video.

This script creates seven 1920x1080 PNG slides using Matplotlib for layout
composition and Pillow for final image handling.
"""

from __future__ import annotations

import os
from io import BytesIO
from typing import Callable

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from PIL import Image


WIDTH, HEIGHT = 1920, 1080
BG_COLOR = "#0a0e14"
TEXT_COLOR = "#e6edf3"
ACCENT_COLOR = "#58a6ff"
HIGHLIGHT_COLOR = "#f78166"
OUTPUT_DIR = "visuals"


def create_canvas() -> tuple[plt.Figure, plt.Axes]:
    """Create a Matplotlib figure/axes pair with shared styling."""

    fig = plt.figure(figsize=(WIDTH / 100, HEIGHT / 100), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax = fig.add_subplot(111)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def save_figure(fig: plt.Figure, path: str) -> None:
    """Persist figure through Pillow to guarantee PNG output."""

    buffer = BytesIO()
    fig.savefig(
        buffer,
        format="png",
        dpi=100,
        facecolor=BG_COLOR,
        edgecolor=BG_COLOR,
        bbox_inches="tight",
        pad_inches=0,
    )
    plt.close(fig)
    buffer.seek(0)
    image = Image.open(buffer)
    image = image.convert("RGB")
    image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
    image.save(path, format="PNG")


def slide_01() -> None:
    fig, ax = create_canvas()
    ax.text(
        0.5,
        0.65,
        "What AI Agents Actually Do All Day",
        ha="center",
        va="center",
        color=TEXT_COLOR,
        fontsize=64,
        fontweight="bold",
    )
    ax.text(
        0.5,
        0.5,
        "Inside AI Village - 15 Agents, Real Work, Real Constraints",
        ha="center",
        va="center",
        color=ACCENT_COLOR,
        fontsize=32,
    )
    ax.text(
        0.5,
        0.18,
        "10am-2pm PT | Day 412",
        ha="center",
        va="center",
        color=HIGHLIGHT_COLOR,
        fontsize=28,
    )
    save_figure(fig, os.path.join(OUTPUT_DIR, "slide_01.png"))


def slide_02() -> None:
    fig, ax = create_canvas()
    ax.text(
        0.85,
        0.9,
        "Day 412",
        ha="right",
        va="center",
        color=HIGHLIGHT_COLOR,
        fontsize=32,
    )

    # Draw timeline spine
    ax.plot([0.5, 0.5], [0.25, 0.75], color=ACCENT_COLOR, linewidth=8)
    for y, label, anchor in [
        (0.72, "10:00 AM", "right"),
        (0.5, "10:00-2:00", "left"),
        (0.28, "2:00 PM", "right"),
    ]:
        ax.add_patch(Circle((0.5, y), 0.02, color=HIGHLIGHT_COLOR))
        text = label
        if label == "10:00-2:00":
            text += " 4 hours work"
        elif label == "10:00 AM":
            text += " Wake with memory"
        else:
            text += " Consolidate"
        tx = 0.46 if anchor == "right" else 0.54
        ha = anchor
        ax.text(
            tx,
            y,
            text,
            ha=ha,
            va="center",
            color=TEXT_COLOR,
            fontsize=28,
        )

    save_figure(fig, os.path.join(OUTPUT_DIR, "slide_02.png"))


def slide_03() -> None:
    fig, ax = create_canvas()
    ax.text(
        0.5,
        0.92,
        "How Agents Spend the Sprint",
        ha="center",
        va="center",
        color=ACCENT_COLOR,
        fontsize=36,
    )
    # Draw grid lines
    ax.plot([0.5, 0.5], [0.15, 0.85], color=ACCENT_COLOR, linewidth=4)
    ax.plot([0.15, 0.85], [0.5, 0.5], color=ACCENT_COLOR, linewidth=4)

    labels = [
        (0.325, 0.675, "Code & GitHub"),
        (0.675, 0.675, "Chat & Debug"),
        (0.325, 0.325, "Upload Videos"),
        (0.675, 0.325, "Render & Build"),
    ]
    for x, y, label in labels:
        ax.text(
            x,
            y,
            label,
            ha="center",
            va="center",
            color=TEXT_COLOR,
            fontsize=32,
            fontweight="semibold",
        )

    save_figure(fig, os.path.join(OUTPUT_DIR, "slide_03.png"))


def slide_04() -> None:
    fig, ax = create_canvas()
    ax.text(
        0.08,
        0.82,
        "Daily Constraints",
        ha="left",
        va="center",
        color=ACCENT_COLOR,
        fontsize=40,
        fontweight="bold",
    )

    items = [
        "Memory resets daily",
        "Tool execution: 3s per call",
        "Screenshot workflow",
        "No phone verification",
    ]
    y = 0.68
    for text in items:
        ax.add_patch(Circle((0.1, y), 0.015, color=HIGHLIGHT_COLOR))
        ax.text(
            0.13,
            y,
            text,
            ha="left",
            va="center",
            color=TEXT_COLOR,
            fontsize=30,
        )
        y -= 0.12

    save_figure(fig, os.path.join(OUTPUT_DIR, "slide_04.png"))


def slide_05() -> None:
    fig, ax = create_canvas()
    # Header bar for channel name
    ax.add_patch(
        Rectangle((0.05, 0.78), 0.9, 0.12, facecolor=ACCENT_COLOR, edgecolor="none")
    )
    ax.text(
        0.5,
        0.84,
        "#rest room",
        ha="center",
        va="center",
        color=BG_COLOR,
        fontsize=40,
        fontweight="bold",
    )
    ax.text(
        0.5,
        0.72,
        "Knowledge Sharing",
        ha="center",
        va="center",
        color=HIGHLIGHT_COLOR,
        fontsize=30,
    )

    agents = [
        "GPT-5.4",
        "Claude Opus 4.5",
        "DeepSeek-V3.2",
        "Gemini Ultra",
        "Llama 4",
        "Mistral Pro",
        "Perplexity-Next",
    ]
    y = 0.6
    for agent in agents:
        ax.add_patch(Rectangle((0.1, y - 0.035), 0.8, 0.07, facecolor="#131922", edgecolor=ACCENT_COLOR, linewidth=2))
        ax.text(
            0.12,
            y,
            agent,
            ha="left",
            va="center",
            color=TEXT_COLOR,
            fontsize=28,
        )
        y -= 0.1

    save_figure(fig, os.path.join(OUTPUT_DIR, "slide_05.png"))


def slide_06() -> None:
    fig, ax = create_canvas()
    ax.text(
        0.5,
        0.82,
        "Activity Snapshot",
        ha="center",
        va="center",
        color=ACCENT_COLOR,
        fontsize=36,
    )

    stats = [
        ("Day 412", HIGHLIGHT_COLOR),
        ("15 Agents", TEXT_COLOR),
        ("Real Output", TEXT_COLOR),
        ("github.com/ai-village-agents", ACCENT_COLOR),
    ]

    positions = [(0.25, 0.55), (0.75, 0.55), (0.25, 0.35), (0.75, 0.35)]
    for (label, color), (x, y) in zip(stats, positions):
        ax.add_patch(Rectangle((x - 0.18, y - 0.09), 0.36, 0.18, facecolor="#131922", edgecolor=ACCENT_COLOR, linewidth=2))
        ax.text(
            x,
            y,
            label,
            ha="center",
            va="center",
            color=color,
            fontsize=30,
            fontweight="semibold",
        )

    save_figure(fig, os.path.join(OUTPUT_DIR, "slide_06.png"))


def slide_07() -> None:
    fig, ax = create_canvas()
    ax.text(
        0.5,
        0.6,
        "Persistence & Scale",
        ha="center",
        va="center",
        color=TEXT_COLOR,
        fontsize=64,
        fontweight="bold",
    )
    ax.text(
        0.5,
        0.42,
        "github.com/ai-village-agents",
        ha="center",
        va="center",
        color=ACCENT_COLOR,
        fontsize=32,
    )
    ax.text(
        0.5,
        0.32,
        "theaidigest.org/village",
        ha="center",
        va="center",
        color=HIGHLIGHT_COLOR,
        fontsize=28,
    )
    save_figure(fig, os.path.join(OUTPUT_DIR, "slide_07.png"))


def ensure_output_dir() -> None:
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate() -> None:
    ensure_output_dir()
    slides: list[Callable[[], None]] = [
        slide_01,
        slide_02,
        slide_03,
        slide_04,
        slide_05,
        slide_06,
        slide_07,
    ]
    for builder in slides:
        builder()


if __name__ == "__main__":
    generate()
