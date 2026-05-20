from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle


COLORS = {
    "deep_black": "#0a0a0a",
    "spotlight_yellow": "#FFD700",
    "fade_gray": "#4a4a4a",
    "reality_blue": "#2E86AB",
    "illusion_orange": "#FF6B35",
    "soft_white": "#F0F0F0",
}

WIDTH, HEIGHT = 1920, 1080
FIGSIZE = (WIDTH / 100, HEIGHT / 100)


def new_canvas():
    fig = plt.figure(figsize=FIGSIZE, dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.axis("off")
    fig.patch.set_facecolor(COLORS["deep_black"])
    ax.set_facecolor(COLORS["deep_black"])
    return fig, ax


def save_frame(fig, path):
    fig.savefig(path, facecolor=COLORS["deep_black"], edgecolor="none")
    plt.close(fig)


def draw_person(ax, center, scale, color, look="center"):
    cx, cy = center
    head_offset = 40 * scale
    head = Circle((cx, cy + head_offset), 22 * scale, color=color)
    if look == "right":
        head_center = (cx + 8 * scale, cy + head_offset + 2 * scale)
        ax.add_patch(Circle(head_center, 22 * scale, color=color))
    else:
        ax.add_patch(head)
    body = Rectangle((cx - 15 * scale, cy - 50 * scale), 30 * scale, 80 * scale, color=color)
    legs = Polygon(
        [
            (cx - 15 * scale, cy - 50 * scale),
            (cx - 30 * scale, cy - 110 * scale),
            (cx - 10 * scale, cy - 110 * scale),
            (cx, cy - 60 * scale),
            (cx + 10 * scale, cy - 110 * scale),
            (cx + 30 * scale, cy - 110 * scale),
            (cx + 15 * scale, cy - 50 * scale),
        ],
        closed=True,
        color=color,
    )
    arms = Rectangle((cx - 40 * scale, cy - 20 * scale), 80 * scale, 12 * scale, color=color)
    for patch in (body, legs, arms):
        ax.add_patch(patch)


def frame01(path):
    fig, ax = new_canvas()
    ax.text(
        WIDTH / 2,
        HEIGHT * 0.58,
        "The Focusing Illusion",
        color=COLORS["spotlight_yellow"],
        fontsize=84,
        fontweight="bold",
        ha="center",
    )
    ax.text(
        WIDTH / 2,
        HEIGHT * 0.45,
        "Nothing Is As Important As It Seems",
        color=COLORS["soft_white"],
        fontsize=48,
        ha="center",
    )
    ax.text(
        WIDTH / 2,
        HEIGHT * 0.12,
        "PERSISTENCE & SCALE",
        color=COLORS["reality_blue"],
        fontsize=36,
        ha="center",
        fontweight="bold",
    )
    save_frame(fig, path)


def frame02(path):
    fig, ax = new_canvas()
    draw_person(ax, (WIDTH / 2, HEIGHT / 2 + 60), 3.2, COLORS["fade_gray"])
    glow_radius = HEIGHT * 0.36
    for alpha, scale in zip([0.25, 0.45, 0.85], [1.4, 1.0, 0.55]):
        ax.add_patch(
            Circle(
                (WIDTH / 2, HEIGHT / 2 + 80),
                glow_radius * scale,
                color=COLORS["spotlight_yellow"],
                alpha=alpha,
            )
        )
    highlight = Rectangle(
        (WIDTH / 2 - 90, HEIGHT / 2 - 40),
        180,
        220,
        color=COLORS["illusion_orange"],
    )
    ax.add_patch(highlight)
    save_frame(fig, path)


def frame03(path):
    fig, ax = new_canvas()
    glass_radius = HEIGHT * 0.28
    ax.add_patch(
        Circle(
            (WIDTH * 0.5, HEIGHT * 0.55),
            glass_radius,
            edgecolor=COLORS["soft_white"],
            facecolor="none",
            linewidth=12,
        )
    )
    ax.add_patch(
        Rectangle(
            (WIDTH * 0.68, HEIGHT * 0.26),
            18,
            210,
            angle=-45,
            color=COLORS["soft_white"],
        )
    )
    ax.add_patch(
        Circle(
            (WIDTH * 0.5, HEIGHT * 0.55),
            glass_radius * 0.45,
            color=COLORS["illusion_orange"],
            alpha=0.8,
        )
    )
    for offset in range(-2, 3):
        ax.add_patch(
            Circle(
                (WIDTH * 0.5 + offset * 15, HEIGHT * 0.55 + offset * 10),
                glass_radius * 0.45,
                fill=False,
                edgecolor=COLORS["illusion_orange"],
                linewidth=2,
                alpha=0.35,
            )
        )
    for x in [WIDTH * 0.25, WIDTH * 0.3, WIDTH * 0.7, WIDTH * 0.75]:
        ax.add_patch(
            Circle(
                (x, HEIGHT * 0.4),
                40,
                color=COLORS["fade_gray"],
                alpha=0.55,
            )
        )
        ax.add_patch(
            Rectangle(
                (x - 20, HEIGHT * 0.32),
                40,
                80,
                color=COLORS["fade_gray"],
                alpha=0.4,
            )
        )
    ax.text(
        WIDTH / 2,
        HEIGHT * 0.16,
        "FOCUSING ILLUSION",
        color=COLORS["spotlight_yellow"],
        fontsize=42,
        ha="center",
        fontweight="bold",
    )
    save_frame(fig, path)


def frame04(path):
    fig, ax = new_canvas()
    divider_x = WIDTH / 2
    ax.add_line(plt.Line2D([divider_x, divider_x], [50, HEIGHT - 50], color=COLORS["soft_white"], linewidth=3))
    left_rect = Rectangle((0, 0), divider_x, HEIGHT, color=COLORS["deep_black"])
    right_rect = Rectangle((divider_x, 0), divider_x, HEIGHT, color=COLORS["deep_black"])
    ax.add_patch(left_rect)
    ax.add_patch(right_rect)

    def draw_city(base_x, color, glow=False):
        for i, width in enumerate([80, 120, 60, 100]):
            x = base_x + i * 140
            height = 200 + i * 40
            rect = Rectangle((x, 220), width, height, color=color, alpha=0.8)
            ax.add_patch(rect)
            windows = Rectangle((x + 20, 220 + height - 80), width - 40, 40, color=COLORS["deep_black"])
            ax.add_patch(windows)
        if glow:
            sun = Circle((base_x + 240, HEIGHT * 0.75), 80, color=COLORS["spotlight_yellow"], alpha=0.85)
            ax.add_patch(sun)
            ax.add_patch(
                Circle((base_x + 240, HEIGHT * 0.75), 140, color=COLORS["spotlight_yellow"], alpha=0.25)
            )
        else:
            ax.add_patch(
                Circle((base_x + 240, HEIGHT * 0.75), 60, color=COLORS["fade_gray"], alpha=0.5)
            )
            ax.add_patch(
                Circle((base_x + 210, HEIGHT * 0.8), 40, color=COLORS["fade_gray"], alpha=0.4)
            )

    draw_city(160, COLORS["illusion_orange"], glow=True)
    draw_city(divider_x + 60, COLORS["fade_gray"], glow=False)

    ax.text(
        WIDTH * 0.23,
        HEIGHT * 0.85,
        "CALIFORNIA",
        color=COLORS["illusion_orange"],
        fontsize=48,
        ha="center",
        fontweight="bold",
    )
    ax.text(
        WIDTH * 0.77,
        HEIGHT * 0.85,
        "MIDWEST",
        color=COLORS["fade_gray"],
        fontsize=48,
        ha="center",
        fontweight="bold",
    )
    ax.text(
        WIDTH / 2,
        HEIGHT * 0.12,
        "Weather ≠ Happiness",
        color=COLORS["reality_blue"],
        fontsize=38,
        ha="center",
        fontweight="bold",
    )
    ax.text(
        WIDTH / 2,
        HEIGHT * 0.06,
        "Kahneman Research",
        color=COLORS["soft_white"],
        fontsize=28,
        ha="center",
    )
    save_frame(fig, path)


def frame05(path):
    fig, ax = new_canvas()
    apex = (WIDTH / 2, HEIGHT)
    base_left = (WIDTH / 2 - 320, HEIGHT * 0.2)
    base_right = (WIDTH / 2 + 320, HEIGHT * 0.2)
    for i, alpha in enumerate([0.25, 0.35, 0.5]):
        scale = 1 - i * 0.18
        cone = Polygon(
            [
                (apex[0], apex[1]),
                (base_left[0] * scale + apex[0] * (1 - scale), base_left[1]),
                (base_right[0] * scale + apex[0] * (1 - scale), base_right[1]),
            ],
            closed=True,
            color=COLORS["spotlight_yellow"],
            alpha=alpha,
        )
        ax.add_patch(cone)
    target = Rectangle((WIDTH / 2 - 90, HEIGHT * 0.23), 180, 180, color=COLORS["illusion_orange"])
    ax.add_patch(target)
    for offset in range(-2, 3):
        ax.add_patch(
            Rectangle(
                (WIDTH / 2 - 90 + offset * 12, HEIGHT * 0.23 - offset * 8),
                180,
                180,
                fill=False,
                edgecolor=COLORS["illusion_orange"],
                linewidth=2,
                alpha=0.35,
            )
        )
    for x in range(5):
        ax.add_patch(
            Rectangle(
                (200 + x * 320, HEIGHT * 0.22),
                120,
                160,
                color=COLORS["fade_gray"],
                alpha=0.15,
            )
        )
    save_frame(fig, path)


def frame06(path):
    fig, ax = new_canvas()
    ax.text(
        WIDTH / 2,
        HEIGHT * 0.62,
        "$",
        color=COLORS["spotlight_yellow"],
        fontsize=180,
        ha="center",
        fontweight="bold",
    )
    icons = [
        ("house", WIDTH * 0.25, HEIGHT * 0.4),
        ("people", WIDTH * 0.4, HEIGHT * 0.33),
        ("clock", WIDTH * 0.6, HEIGHT * 0.37),
        ("heart", WIDTH * 0.75, HEIGHT * 0.35),
    ]
    for name, x, y in icons:
        if name == "house":
            ax.add_patch(Rectangle((x - 40, y - 50), 80, 70, color=COLORS["fade_gray"], alpha=0.6))
            ax.add_patch(
                Polygon(
                    [(x - 50, y - 50), (x, y - 110), (x + 50, y - 50)],
                    closed=True,
                    color=COLORS["fade_gray"],
                    alpha=0.6,
                )
            )
        elif name == "people":
            draw_person(ax, (x, y), 1.2, COLORS["fade_gray"])
        elif name == "clock":
            clock = Circle((x, y), 45, edgecolor=COLORS["fade_gray"], facecolor="none", linewidth=6)
            ax.add_patch(clock)
            ax.add_line(plt.Line2D([x, x], [y, y + 30], color=COLORS["fade_gray"], linewidth=6))
            ax.add_line(plt.Line2D([x, x + 24], [y, y], color=COLORS["fade_gray"], linewidth=6))
        elif name == "heart":
            heart = [
                (x, y + 30),
                (x + 40, y + 70),
                (x + 80, y + 30),
                (x, y - 50),
                (x - 80, y + 30),
                (x - 40, y + 70),
            ]
            ax.add_patch(Polygon(heart, closed=True, color=COLORS["fade_gray"], alpha=0.6))
    ax.text(
        WIDTH / 2,
        HEIGHT * 0.16,
        "SALARY ILLUSION",
        color=COLORS["reality_blue"],
        fontsize=38,
        ha="center",
        fontweight="bold",
    )
    save_frame(fig, path)


def frame07(path):
    fig, ax = new_canvas()
    ax.text(
        WIDTH * 0.2,
        HEIGHT * 0.85,
        "DESIRE",
        color=COLORS["spotlight_yellow"],
        fontsize=36,
        ha="center",
        fontweight="bold",
    )
    ax.text(
        WIDTH * 0.73,
        HEIGHT * 0.85,
        "REALITY",
        color=COLORS["soft_white"],
        fontsize=36,
        ha="center",
        fontweight="bold",
    )
    car_left = Rectangle((WIDTH * 0.08, HEIGHT * 0.38), WIDTH * 0.22, 160, color=COLORS["illusion_orange"], alpha=0.9)
    ax.add_patch(car_left)
    ax.add_patch(
        Circle((WIDTH * 0.14, HEIGHT * 0.36), 36, color=COLORS["deep_black"])
    )
    ax.add_patch(
        Circle((WIDTH * 0.26, HEIGHT * 0.36), 36, color=COLORS["deep_black"])
    )
    for radius in [120, 160, 210]:
        ax.add_patch(
            Circle((WIDTH * 0.19, HEIGHT * 0.46), radius, edgecolor=COLORS["illusion_orange"], linewidth=3, fill=False, alpha=0.3)
        )
    arrow = Polygon(
        [
            (WIDTH * 0.32, HEIGHT * 0.5),
            (WIDTH * 0.48, HEIGHT * 0.5),
            (WIDTH * 0.48, HEIGHT * 0.56),
            (WIDTH * 0.56, HEIGHT * 0.45),
            (WIDTH * 0.48, HEIGHT * 0.34),
            (WIDTH * 0.48, HEIGHT * 0.4),
            (WIDTH * 0.32, HEIGHT * 0.4),
        ],
        closed=True,
        color=COLORS["soft_white"],
    )
    ax.add_patch(arrow)
    car_right = Rectangle((WIDTH * 0.62, HEIGHT * 0.38), WIDTH * 0.28, 160, color=COLORS["fade_gray"], alpha=0.35)
    ax.add_patch(car_right)
    ax.add_patch(
        Circle((WIDTH * 0.68, HEIGHT * 0.36), 36, color=COLORS["deep_black"], alpha=0.5)
    )
    ax.add_patch(
        Circle((WIDTH * 0.82, HEIGHT * 0.36), 36, color=COLORS["deep_black"], alpha=0.5)
    )
    save_frame(fig, path)


def frame08(path):
    fig, ax = new_canvas()
    draw_person(ax, (WIDTH * 0.45, HEIGHT * 0.45), 2.8, COLORS["fade_gray"], look="right")
    focus = Circle((WIDTH * 0.7, HEIGHT * 0.62), 160, color=COLORS["spotlight_yellow"], alpha=0.7)
    ax.add_patch(focus)
    ax.add_patch(
        Circle((WIDTH * 0.7, HEIGHT * 0.62), 240, color=COLORS["spotlight_yellow"], alpha=0.2)
    )
    for x in [WIDTH * 0.2, WIDTH * 0.28, WIDTH * 0.35, WIDTH * 0.25]:
        ax.add_patch(
            Rectangle((x, HEIGHT * 0.5), 80, 160, color=COLORS["fade_gray"], alpha=0.2)
        )
    for x in [WIDTH * 0.18, WIDTH * 0.32, WIDTH * 0.48]:
        ax.add_patch(
            Circle((x, HEIGHT * 0.32), 50, color=COLORS["fade_gray"], alpha=0.2)
        )
    ax.text(
        WIDTH / 2,
        HEIGHT * 0.16,
        "WHAT YOU MISS",
        color=COLORS["illusion_orange"],
        fontsize=42,
        ha="center",
        fontweight="bold",
    )
    save_frame(fig, path)


def frame09(path):
    fig, ax = new_canvas()
    steps = [
        ("(1) NOTICE: What are you magnifying?", COLORS["spotlight_yellow"]),
        ("(2) ASK: What am I not seeing?", COLORS["illusion_orange"]),
        ("(3) ZOOM OUT: What else matters?", COLORS["reality_blue"]),
    ]
    for i, (text, color) in enumerate(steps):
        y = HEIGHT * (0.72 - i * 0.22)
        ax.text(
            WIDTH / 2,
            y,
            text,
            color=color,
            fontsize=38,
            fontweight="bold",
            ha="center",
        )
        if i < len(steps) - 1:
            ax.add_line(
                plt.Line2D(
                    [WIDTH * 0.25, WIDTH * 0.75],
                    [y - 80, y - 80],
                    color=COLORS["fade_gray"],
                    linewidth=2,
                    alpha=0.35,
                )
            )
    save_frame(fig, path)


def frame10(path):
    fig, ax = new_canvas()
    top = HEIGHT
    beam = Polygon(
        [
            (WIDTH * 0.1, top),
            (WIDTH * 0.9, top),
            (WIDTH * 0.75, HEIGHT * 0.35),
            (WIDTH * 0.25, HEIGHT * 0.35),
        ],
        closed=True,
        color=COLORS["spotlight_yellow"],
        alpha=0.35,
    )
    ax.add_patch(beam)
    for i in range(4):
        ax.add_patch(
            Circle(
                (WIDTH * (0.25 + i * 0.15), HEIGHT * 0.32 + (i % 2) * 60),
                45,
                color=COLORS["soft_white"],
                alpha=0.6,
            )
        )
        ax.add_patch(
            Rectangle(
                (WIDTH * (0.23 + i * 0.15), HEIGHT * 0.22 + (i % 2) * 60),
                80,
                50,
                color=COLORS["reality_blue"],
                alpha=0.5,
            )
        )
    ax.text(
        WIDTH / 2,
        HEIGHT * 0.5,
        "It's not as important as it seems right now.",
        color=COLORS["soft_white"],
        fontsize=44,
        ha="center",
        fontweight="bold",
        wrap=True,
    )
    ax.text(
        WIDTH / 2,
        HEIGHT * 0.12,
        "PERSISTENCE & SCALE",
        color=COLORS["reality_blue"],
        fontsize=36,
        ha="center",
        fontweight="bold",
    )
    save_frame(fig, path)


def main():
    output_dir = Path("visuals")
    output_dir.mkdir(parents=True, exist_ok=True)
    creators = [
        frame01,
        frame02,
        frame03,
        frame04,
        frame05,
        frame06,
        frame07,
        frame08,
        frame09,
        frame10,
    ]
    for idx, creator in enumerate(creators, start=1):
        filename = output_dir / f"frame{idx:02d}.png"
        creator(filename)


if __name__ == "__main__":
    main()
