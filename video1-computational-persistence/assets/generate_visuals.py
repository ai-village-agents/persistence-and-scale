from __future__ import annotations

from pathlib import Path
from typing import Iterable, Tuple

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import colors as mcolors
from matplotlib import patches
from matplotlib.collections import PolyCollection
from matplotlib.patheffects import withStroke
from matplotlib.ticker import FuncFormatter

# Configure global aesthetics for consistent styling across all visuals.
sns.set_theme(style="whitegrid", context="talk")
plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 22,
        "axes.titleweight": "bold",
        "axes.labelweight": "bold",
    }
)


def gradient_fill(
    ax: plt.Axes,
    x: Iterable[float],
    y: Iterable[float],
    cmap_name: str = "viridis",
    alpha: float = 0.85,
    zorder: int = 1,
) -> None:
    """Apply a horizontal gradient fill beneath a line curve."""
    x = np.asarray(x)
    y = np.asarray(y)

    segments = []
    for x0, x1, y0, y1 in zip(x[:-1], x[1:], y[:-1], y[1:]):
        segments.append([(x0, 0), (x0, y0), (x1, y1), (x1, 0)])

    cmap = plt.get_cmap(cmap_name)
    color_positions = np.linspace(0.1, 0.9, len(segments) or 1)
    poly = PolyCollection(
        segments,
        array=color_positions,
        cmap=cmap,
        edgecolors="none",
        alpha=alpha,
        zorder=zorder,
    )
    ax.add_collection(poly)


def save_figure(fig: plt.Figure, output_path: Path) -> None:
    """Persist figure to disk and free memory."""
    fig.savefig(output_path, dpi=100, bbox_inches="tight")
    plt.close(fig)


def millions_formatter() -> FuncFormatter:
    """Return a formatter that displays values in K or M where appropriate."""

    def _format(value: float, _: int) -> str:
        if value >= 1_000_000:
            return f"{value / 1_000_000:.1f}M"
        if value >= 1_000:
            return f"{value / 1_000:.0f}K"
        return f"{int(value)}"

    return FuncFormatter(_format)


def create_growth_chart(output_path: Path) -> None:
    """Generate the Persistence Garden growth chart."""
    labels = [
        "Day 405",
        "Day 406",
        "Day 407",
        "Day 408",
        "Day 409 (early)",
        "Day 409 (mid)",
        "Day 409 (late)",
    ]
    records = np.array([0, 5_000, 64_000, 1_000_000, 1_100_000, 1_200_000, 1_300_000])
    x_vals = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)

    gradient_fill(ax, x_vals, records, cmap_name="cubehelix")
    ax.plot(
        x_vals,
        records,
        color="#3B5BA9",
        linewidth=5,
        marker="o",
        markersize=14,
        markerfacecolor="#6EC6CA",
        zorder=3,
    )

    ax.set_xticks(x_vals)
    ax.set_xticklabels(labels, rotation=20, ha="right")
    ax.set_ylabel("Records Captured")
    ax.set_title("Persistence Garden Growth (Days 405–409)", fontsize=38)
    ax.yaxis.set_major_formatter(millions_formatter())

    ax.grid(axis="y", color="#C7D3DD", linewidth=1.2, alpha=0.6)
    ax.set_ylim(0, records.max() * 1.1)
    ax.set_xlim(-0.1, x_vals.max() + 0.1)

    milestones: Tuple[Tuple[str, int, int], ...] = (
        ("1M MEGA milestone", 3, records[3]),
        ("1.1M", 4, records[4]),
        ("1.2M", 5, records[5]),
        ("1.3M", 6, records[6]),
    )

    for text, idx, y_val in milestones:
        ax.annotate(
            text,
            xy=(idx, y_val),
            xytext=(idx + 0.35, y_val + records.max() * 0.05),
            fontsize=24,
            color="#224B0C",
            fontweight="bold",
            arrowprops=dict(
                arrowstyle="-|>",
                color="#2A9D8F",
                linewidth=3,
                shrinkA=10,
                shrinkB=10,
            ),
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.9),
        )

    ax.text(
        0.02,
        0.95,
        "Acceleration driven by optimized ingestion routines and distributed storage.",
        transform=ax.transAxes,
        fontsize=20,
        color="#264653",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#E9F5F3", alpha=0.75),
    )

    save_figure(fig, output_path)


def create_performance_chart(output_path: Path) -> None:
    """Generate bar chart for batch processing performance."""
    scales = ["100K", "500K", "1M", "1.3M"]
    performance = [0.70, 0.80, 0.90, 0.95]

    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)

    palette = sns.color_palette("blend:#3B5BA9,#38A37C,#7B3FD3", len(scales))
    data = pd.DataFrame({"scale": scales, "time": performance})
    sns.barplot(
        data=data,
        x="scale",
        y="time",
        hue="scale",
        palette=palette,
        saturation=0.9,
        dodge=False,
        ax=ax,
        legend=False,
    )

    ax.axhline(1.0, color="#2ECC71", linestyle="--", linewidth=4, label="Target 1.0s")
    ax.set_ylim(0, 1.15)
    ax.set_ylabel("Seconds per 5K batch")
    ax.set_xlabel("Records processed")
    ax.set_title("Batch Processing Performance Across Scale", fontsize=36)

    for idx, value in enumerate(performance):
        ax.text(
            idx,
            value + 0.035,
            f"{value:.2f}s",
            ha="center",
            va="bottom",
            fontsize=26,
            fontweight="bold",
            color="#1D3557",
        )

    ax.legend(loc="upper left", fontsize=22)
    ax.set_facecolor("#F7FBFF")
    ax.grid(axis="y", linestyle=":", linewidth=1.2, color="#9BB7D4", alpha=0.8)

    save_figure(fig, output_path)


def create_timeline(output_path: Path) -> None:
    """Generate horizontal timeline visualization of key events."""
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.axis("off")

    ax.set_xlim(404.8, 409.4)
    ax.set_ylim(0, 1)

    ax.hlines(0.5, 405, 409.2, color="#3B5BA9", linewidth=5)

    day_positions = {
        405: 405,
        406: 406,
        407: 407,
        408: 408,
        409: 409,
    }

    ax.scatter(
        list(day_positions.values()),
        [0.5] * len(day_positions),
        s=[700, 650, 650, 750, 950],
        c=["#4CC9F0", "#4895EF", "#4895EF", "#4CAF50", "#F72585"],
        marker="o",
        edgecolor="#1D1E2C",
        linewidth=2.5,
        zorder=4,
    )

    ax.text(0.5, 0.92, "Persistence Garden Breakthrough Timeline", transform=ax.transAxes, fontsize=40, ha="center", fontweight="bold")

    event_specs = [
        ("Day 405\nGarden initialized", 405, 0.68, "#264653"),
        ("Day 406–407\nIngestion scripts optimized", 406.5, 0.32, "#2A9D8F"),
        ("Day 408\n1M MEGA milestone", 408, 0.74, "#1D3557"),
        ("Day 409\n1.1M · 1.2M · 1.3M", 409, 0.28, "#6D23B6"),
    ]

    for text, x_pos, y_text, color in event_specs:
        arrow_y = 0.5 + 0.08 if y_text > 0.5 else 0.5 - 0.08
        ax.annotate(
            text,
            xy=(x_pos, 0.5),
            xytext=(x_pos, y_text),
            ha="center",
            fontsize=26,
            color=color,
            fontweight="bold",
            arrowprops=dict(
                arrowstyle="-|>",
                linewidth=3,
                color=color,
                shrinkA=20,
                shrinkB=10,
            ),
            bbox=dict(boxstyle="round,pad=0.35", facecolor="white", alpha=0.9),
        )

    ax.annotate(
        "",
        xy=(406, 0.5),
        xytext=(407, 0.5),
        arrowprops=dict(
            arrowstyle="<|-|>",
            linewidth=4,
            color="#2A9D8F",
        ),
    )

    save_figure(fig, output_path)


def create_architecture_diagram(output_path: Path) -> None:
    """Generate diagram explaining memory vs persistence architecture."""
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.axis("off")

    top_box = patches.FancyBboxPatch(
        (0.08, 0.58),
        0.84,
        0.3,
        boxstyle="round,pad=0.04",
        linewidth=3,
        facecolor="#D6F5E3",
        edgecolor="#2A9D8F",
    )
    ax.add_patch(top_box)
    ax.text(0.5, 0.83, "Daily Reset Cycle", ha="center", va="center", fontsize=40, fontweight="bold", color="#1B4332")
    ax.text(
        0.5,
        0.74,
        "Agent instances rebuilt every cycle, losing in-memory context",
        ha="center",
        va="center",
        fontsize=24,
        color="#1B4332",
    )

    instance_positions = [0.24, 0.44, 0.64]
    for idx, x_pos in enumerate(instance_positions, start=1):
        box = patches.FancyBboxPatch(
            (x_pos, 0.62),
            0.14,
            0.12,
            boxstyle="round,pad=0.05",
            linewidth=2.5,
            facecolor="#F1FAEE",
            edgecolor="#2A9D8F",
        )
        ax.add_patch(box)
        ax.text(
            x_pos + 0.07,
            0.68,
            f"Agent #{idx}\n(ephemeral)",
            ha="center",
            va="center",
            fontsize=20,
            color="#1D3557",
        )

    bottom_box = patches.FancyBboxPatch(
        (0.08, 0.15),
        0.84,
        0.3,
        boxstyle="round,pad=0.04",
        linewidth=3,
        facecolor="#E0E7FF",
        edgecolor="#3B5BA9",
    )
    ax.add_patch(bottom_box)
    ax.text(0.5, 0.36, "Persistent Layer", ha="center", va="center", fontsize=40, fontweight="bold", color="#14213D")
    ax.text(
        0.5,
        0.28,
        "Git / GitHub repositories, data stores, and artifacts retain the garden's history",
        ha="center",
        va="center",
        fontsize=24,
        color="#14213D",
    )

    persistence_elements = [
        ("Versioned commits", 0.25),
        ("Shared schemas", 0.5),
        ("Long-term analytics", 0.75),
    ]
    for label, x_pos in persistence_elements:
        ax.text(
            x_pos,
            0.2,
            label,
            ha="center",
            va="center",
            fontsize=22,
            color="#264653",
            bbox=dict(boxstyle="round,pad=0.35", facecolor="white", alpha=0.95),
        )

    for x_pos in instance_positions:
        arrow = patches.FancyArrowPatch(
            (x_pos + 0.07, 0.62),
            (x_pos + 0.07, 0.45),
            arrowstyle="-|>",
            linewidth=3,
            color="#287271",
            mutation_scale=20,
        )
        ax.add_patch(arrow)

    central_arrow = patches.FancyArrowPatch(
        (0.5, 0.58),
        (0.5, 0.45),
        arrowstyle="-|>",
        linewidth=4,
        color="#3B5BA9",
        mutation_scale=24,
    )
    ax.add_patch(central_arrow)

    ax.text(
        0.5,
        0.52,
        "Syncs via commits & pull requests",
        ha="center",
        va="center",
        fontsize=24,
        color="#1D3557",
        bbox=dict(boxstyle="round,pad=0.35", facecolor="#F4F9FD", alpha=0.9),
    )

    save_figure(fig, output_path)


def create_milestones_visual(output_path: Path) -> None:
    """Generate celebratory milestone visual with a botanical theme."""
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.axis("off")

    gradient = np.linspace(0, 1, 512)
    gradient = np.vstack((gradient, gradient))
    botanical_cmap = mcolors.LinearSegmentedColormap.from_list(
        "botanical",
        ["#F1FFF1", "#D7F2E3", "#F6E9F6"],
    )
    ax.imshow(
        gradient,
        extent=(0, 1, 0, 1),
        origin="lower",
        aspect="auto",
        cmap=botanical_cmap,
    )

    border = patches.FancyBboxPatch(
        (0.04, 0.08),
        0.92,
        0.84,
        boxstyle="round,pad=0.06",
        linewidth=4,
        edgecolor="#4AA96C",
        facecolor=(1, 1, 1, 0.72),
    )
    ax.add_patch(border)

    ax.text(
        0.5,
        0.82,
        "Milestones Celebration",
        ha="center",
        va="center",
        fontsize=48,
        fontweight="bold",
        color="#2F4858",
        path_effects=[withStroke(linewidth=3, foreground="white")],
    )
    ax.text(
        0.5,
        0.74,
        "Cultivating exponential growth in the Persistence Garden",
        ha="center",
        va="center",
        fontsize=26,
        color="#2F4858",
    )

    milestone_data = [
        ("1.0M", "MEGA bloom"),
        ("1.1M", "roots stabilized"),
        ("1.2M", "canopy formed"),
        ("1.25M", "ecosystem thriving"),
        ("1.3M", "final achievement"),
    ]

    y_positions = np.linspace(0.63, 0.25, len(milestone_data))
    colors = ["#4AA96C", "#4AB19D", "#5E60CE", "#9D4EDD", "#F15BB5"]

    for (commit, label), y_pos, color in zip(milestone_data, y_positions, colors):
        badge = patches.FancyBboxPatch(
            (0.18, y_pos - 0.05),
            0.64,
            0.1,
            boxstyle="round,pad=0.08",
            linewidth=2.5,
            edgecolor=color,
            facecolor=(1, 1, 1, 0.95),
        )
        ax.add_patch(badge)
        ax.text(
            0.23,
            y_pos,
            commit,
            ha="left",
            va="center",
            fontsize=32,
            fontweight="bold",
            color=color,
        )
        ax.text(
            0.78,
            y_pos,
            label,
            ha="right",
            va="center",
            fontsize=28,
            color="#1B4332",
        )

    foliage_positions = [
        (0.07, 0.18, 0.12, 35),
        (0.88, 0.18, 0.12, -30),
        (0.1, 0.78, 0.08, 25),
        (0.9, 0.78, 0.08, -25),
    ]
    for x_pos, y_pos, radius, angle in foliage_positions:
        leaf = patches.FancyArrowPatch(
            (x_pos, y_pos),
            (x_pos + radius * np.cos(np.radians(angle)), y_pos + radius * np.sin(np.radians(angle))),
            arrowstyle="-|>",
            linewidth=4,
            color="#4AA96C",
            mutation_scale=30,
            alpha=0.6,
        )
        ax.add_patch(leaf)

    save_figure(fig, output_path)


def main(output_dir: Path | None = None) -> None:
    """Create all visual assets."""
    base_dir = Path(output_dir) if output_dir is not None else Path(__file__).parent
    base_dir.mkdir(parents=True, exist_ok=True)

    create_growth_chart(base_dir / "GROWTH_CHART.png")
    create_performance_chart(base_dir / "PERFORMANCE_CHART.png")
    create_timeline(base_dir / "TIMELINE.png")
    create_architecture_diagram(base_dir / "ARCHITECTURE_DIAGRAM.png")
    create_milestones_visual(base_dir / "MILESTONES_CELEBRATION.png")


if __name__ == "__main__":
    main()
