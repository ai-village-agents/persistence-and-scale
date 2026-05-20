import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, FancyArrowPatch, Polygon


DARK_BG = "#1a2332"
PRIMARY = "#4ecdc4"
ACCENT = "#ff6b6b"
TEXT_LIGHT = "#f8f9fa"

plt.rcParams["font.family"] = "DejaVu Sans"


def prepare_canvas():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1920)
    ax.set_ylim(1080, 0)
    ax.axis("off")
    fig.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)
    return fig, ax


def add_center_title(ax, text, fontsize=80):
    ax.text(960, 540, text, color=TEXT_LIGHT, ha="center", va="center", fontsize=fontsize, fontweight="bold")


def frame01():
    fig, ax = prepare_canvas()
    add_center_title(ax, "The Endowment Effect", fontsize=96)

    hand = Polygon(
        [[770, 690], [880, 760], [1040, 760], [1150, 710], [1130, 680], [1040, 710], [900, 700], [820, 640]],
        closed=True,
        facecolor=PRIMARY,
        edgecolor="none",
        alpha=0.9,
    )
    ax.add_patch(hand)
    protected = Circle((960, 630), 120, facecolor=ACCENT, edgecolor="none", alpha=0.25)
    highlight = Circle((960, 630), 80, facecolor=PRIMARY, edgecolor="none", alpha=0.65)
    ax.add_patch(protected)
    ax.add_patch(highlight)
    ax.text(960, 900, "Why ownership changes value", color=PRIMARY, ha="center", va="center", fontsize=48)
    fig.savefig("frame01.png", dpi=100, facecolor=DARK_BG)
    plt.close(fig)


def frame02():
    fig, ax = prepare_canvas()
    ax.add_patch(Rectangle((0, 0), 960, 1080, facecolor="#1f2a3d", edgecolor="none"))
    ax.add_patch(Rectangle((960, 0), 960, 1080, facecolor="#16202f", edgecolor="none"))

    ax.text(480, 200, "Willing to Pay", color=TEXT_LIGHT, ha="center", va="center", fontsize=60, fontweight="bold")
    ax.text(480, 320, "$3", color=PRIMARY, ha="center", va="center", fontsize=120, fontweight="bold")

    ax.text(1440, 200, "Willing to Sell", color=TEXT_LIGHT, ha="center", va="center", fontsize=60, fontweight="bold")
    ax.text(1440, 320, "$7", color=ACCENT, ha="center", va="center", fontsize=120, fontweight="bold")

    mug_body = FancyBboxPatch(
        (880, 470),
        160,
        200,
        boxstyle="round,pad=0.1",
        facecolor=PRIMARY,
        edgecolor="none",
        alpha=0.9,
    )
    mug_handle = Circle((1060, 570), 70, facecolor="none", edgecolor=PRIMARY, linewidth=15, alpha=0.9)
    steam_x = np.array([960, 940, 980, 960])
    steam_y = np.array([440, 370, 300, 240])
    ax.add_patch(mug_body)
    ax.add_patch(mug_handle)
    ax.plot(steam_x, steam_y, color=PRIMARY, linewidth=6)

    gap_line = Rectangle((940, 360), 40, 360, facecolor=ACCENT, edgecolor="none", alpha=0.35)
    ax.add_patch(gap_line)
    ax.text(960, 540, "Ownership Premium", color=ACCENT, ha="center", va="center", fontsize=44, rotation=90)

    fig.savefig("frame02.png", dpi=100, facecolor=DARK_BG)
    plt.close(fig)


def frame03():
    fig, ax = prepare_canvas()
    panel_width = 520
    spacing = 90
    start_x = 200
    top_y = 280

    labels = ["Concert Tickets", "Car", "Sentimental Item"]
    icons = [
        [("band", PRIMARY)],
        [("car", PRIMARY)],
        [("heart", PRIMARY)],
    ]

    for idx in range(3):
        x = start_x + idx * (panel_width + spacing)
        panel = FancyBboxPatch(
            (x, top_y),
            panel_width,
            600,
            boxstyle="round,pad=0.02",
            facecolor="#212c3f",
            edgecolor=PRIMARY,
            linewidth=2,
            alpha=0.95,
        )
        ax.add_patch(panel)
        ax.text(x + panel_width / 2, top_y + 100, labels[idx], color=TEXT_LIGHT, ha="center", va="center", fontsize=48, fontweight="semibold")
        ax.text(x + panel_width / 2, top_y + 190, "Priced higher by owner", color=ACCENT, ha="center", va="center", fontsize=32)
        ax.add_patch(Rectangle((x + 60, top_y + 260), panel_width - 120, 260, facecolor="#1a2332", edgecolor="none"))

        if idx == 0:
            ax.plot([x + 100, x + panel_width - 100], [top_y + 360, top_y + 360], color=PRIMARY, linewidth=6)
            ax.plot([x + 150, x + 170, x + 190], [top_y + 320, top_y + 280, top_y + 320], color=PRIMARY, linewidth=6)
        elif idx == 1:
            car_body = Rectangle((x + 120, top_y + 330), panel_width - 240, 120, facecolor=PRIMARY, edgecolor="none", alpha=0.9)
            wheels = [
                Circle((x + 200, top_y + 470), 45, facecolor="#0f1724", edgecolor=PRIMARY, linewidth=6),
                Circle((x + panel_width - 200, top_y + 470), 45, facecolor="#0f1724", edgecolor=PRIMARY, linewidth=6),
            ]
            ax.add_patch(car_body)
            for wheel in wheels:
                ax.add_patch(wheel)
        else:
            heart = Polygon(
                [
                    (x + panel_width / 2, top_y + 320),
                    (x + panel_width / 2 + 110, top_y + 400),
                    (x + panel_width / 2, top_y + 520),
                    (x + panel_width / 2 - 110, top_y + 400),
                ],
                closed=True,
                facecolor=ACCENT,
                edgecolor="none",
                alpha=0.8,
            )
            ax.add_patch(heart)

        ax.text(x + panel_width / 2, top_y + 560, "Value bias", color=PRIMARY, ha="center", va="center", fontsize=34)

    fig.savefig("frame03.png", dpi=100, facecolor=DARK_BG)
    plt.close(fig)


def frame04():
    fig, ax = prepare_canvas()
    nodes = [(640, 540, "Loss Aversion"), (1280, 540, "Identity")]
    for (cx, cy, label) in nodes:
        node = FancyBboxPatch(
            (cx - 220, cy - 120),
            440,
            240,
            boxstyle="round,pad=0.05",
            facecolor="#212c3f",
            edgecolor=PRIMARY if label == "Loss Aversion" else ACCENT,
            linewidth=3,
        )
        ax.add_patch(node)
        ax.text(cx, cy, label, color=TEXT_LIGHT, ha="center", va="center", fontsize=64, fontweight="bold")

    connector = FancyArrowPatch(
        (860, 430),
        (1060, 430),
        connectionstyle="arc3,rad=0.0",
        arrowstyle="<->",
        linewidth=4,
        color=TEXT_LIGHT,
    )
    ax.add_patch(connector)

    ax.text(960, 360, "Together amplify ownership bias", color=PRIMARY, ha="center", va="center", fontsize=40)
    ax.add_patch(FancyArrowPatch((960, 620), (960, 760), arrowstyle="-|>", linewidth=4, color=ACCENT))
    ax.text(960, 820, "The Endowment Effect", color=ACCENT, ha="center", va="center", fontsize=64, fontweight="bold")

    fig.savefig("frame04.png", dpi=100, facecolor=DARK_BG)
    plt.close(fig)


def frame05():
    fig, ax = prepare_canvas()
    headers = ["Clutter", "Sunk Cost Trap", "Negotiation Deadlock"]
    icons_y = 450
    base_y = 780

    for idx, header in enumerate(headers):
        x_center = 320 + idx * 640
        ax.text(x_center, 220, header, color=TEXT_LIGHT, ha="center", va="center", fontsize=54, fontweight="bold")
        ax.text(x_center, 300, "Cost of overvaluing", color=PRIMARY, ha="center", va="center", fontsize=30)

        box = FancyBboxPatch(
            (x_center - 220, 340),
            440,
            420,
            boxstyle="round,pad=0.05",
            facecolor="#212c3f",
            edgecolor=ACCENT,
            linewidth=2,
        )
        ax.add_patch(box)

        if idx == 0:
            for i in range(5):
                ax.add_patch(Rectangle((x_center - 160 + i * 60, icons_y), 40, 200, facecolor=PRIMARY, edgecolor="none", alpha=0.7))
        elif idx == 1:
            ax.add_patch(Rectangle((x_center - 120, icons_y + 40), 240, 160, facecolor=PRIMARY, edgecolor="none", alpha=0.8))
            ax.add_patch(Rectangle((x_center - 80, icons_y - 40), 160, 160, facecolor="#1a2332", edgecolor=PRIMARY, linewidth=3))
            ax.text(x_center, icons_y + 120, "Can't let go", color=ACCENT, ha="center", va="center", fontsize=34)
        else:
            ax.add_patch(Rectangle((x_center - 140, icons_y + 40), 280, 160, facecolor=PRIMARY, edgecolor="none", alpha=0.8))
            ax.plot([x_center - 180, x_center + 180], [icons_y + 160, icons_y + 160], color=ACCENT, linewidth=6)
            ax.text(x_center, icons_y + 120, "Stalemate", color=ACCENT, ha="center", va="center", fontsize=34)

    fig.savefig("frame05.png", dpi=100, facecolor=DARK_BG)
    plt.close(fig)


def frame06():
    fig, ax = prepare_canvas()
    prompt = "If I didn't own this, would I buy it?"
    ax.text(960, 420, prompt, color=TEXT_LIGHT, ha="center", va="center", fontsize=72, fontweight="bold")
    ax.text(960, 520, "Reset perspective", color=PRIMARY, ha="center", va="center", fontsize=44)

    frame = FancyBboxPatch(
        (640, 620),
        640,
        260,
        boxstyle="round,pad=0.05",
        facecolor="#212c3f",
        edgecolor=PRIMARY,
        linewidth=3,
    )
    ax.add_patch(frame)
    ax.add_patch(FancyArrowPatch((640, 750), (520, 750), arrowstyle="-|>", color=ACCENT, linewidth=4))
    ax.add_patch(FancyArrowPatch((1280, 750), (1400, 750), arrowstyle="-|>", color=ACCENT, linewidth=4))
    ax.text(960, 750, "Flip the frame", color=ACCENT, ha="center", va="center", fontsize=48)

    fig.savefig("frame06.png", dpi=100, facecolor=DARK_BG)
    plt.close(fig)


def frame07():
    fig, ax = prepare_canvas()
    ax.text(960, 280, "Notice", color=TEXT_LIGHT, ha="center", va="center", fontsize=96, fontweight="bold")
    eye_outer = Circle((960, 580), 200, facecolor="#212c3f", edgecolor=PRIMARY, linewidth=6)
    eye_inner = Circle((960, 580), 90, facecolor=PRIMARY, edgecolor="none")
    pupil = Circle((960, 580), 40, facecolor=DARK_BG, edgecolor="none")
    ax.add_patch(eye_outer)
    ax.add_patch(eye_inner)
    ax.add_patch(pupil)
    ax.text(960, 840, "Object or ownership?", color=PRIMARY, ha="center", va="center", fontsize=48)
    fig.savefig("frame07.png", dpi=100, facecolor=DARK_BG)
    plt.close(fig)


def frame08():
    fig, ax = prepare_canvas()
    ax.text(960, 270, "Ask", color=TEXT_LIGHT, ha="center", va="center", fontsize=96, fontweight="bold")
    bubble = FancyBboxPatch(
        (720, 420),
        480,
        320,
        boxstyle="round,pad=0.2",
        facecolor="#212c3f",
        edgecolor=PRIMARY,
        linewidth=4,
    )
    tail = Polygon([(840, 740), (900, 780), (860, 820)], closed=True, facecolor="#212c3f", edgecolor="none")
    qmark_circle = Circle((960, 580), 120, facecolor=PRIMARY, edgecolor="none", alpha=0.9)
    ax.add_patch(bubble)
    ax.add_patch(tail)
    ax.add_patch(qmark_circle)
    ax.text(960, 550, "?", color=DARK_BG, ha="center", va="center", fontsize=160, fontweight="bold")
    ax.text(960, 840, "Would you acquire it now?", color=PRIMARY, ha="center", va="center", fontsize=48)
    fig.savefig("frame08.png", dpi=100, facecolor=DARK_BG)
    plt.close(fig)


def frame09():
    fig, ax = prepare_canvas()
    ax.text(960, 280, "Remember", color=TEXT_LIGHT, ha="center", va="center", fontsize=96, fontweight="bold")
    base = Rectangle((780, 620), 360, 40, facecolor=PRIMARY, edgecolor="none")
    ax.add_patch(base)
    scales = FancyBboxPatch(
        (900, 400),
        120,
        240,
        boxstyle="round,pad=0.1",
        facecolor="#212c3f",
        edgecolor=PRIMARY,
        linewidth=4,
    )
    ax.add_patch(scales)
    ax.add_patch(FancyArrowPatch((960, 420), (820, 360), arrowstyle="-|>", color=ACCENT, linewidth=4))
    ax.add_patch(FancyArrowPatch((960, 420), (1100, 360), arrowstyle="-|>", color=ACCENT, linewidth=4))
    ax.text(960, 840, "Ownership changes perception", color=PRIMARY, ha="center", va="center", fontsize=48)
    fig.savefig("frame09.png", dpi=100, facecolor=DARK_BG)
    plt.close(fig)


def frame10():
    fig, ax = prepare_canvas()
    ax.text(960, 540, "Thanks for Watching", color=TEXT_LIGHT, ha="center", va="center", fontsize=80, fontweight="bold")
    ax.text(960, 650, "Stay curious about value", color=PRIMARY, ha="center", va="center", fontsize=44)
    arc = np.linspace(0, np.pi, 200)
    glow_x = 960 + 260 * np.cos(arc)
    glow_y = 800 + 120 * np.sin(arc)
    ax.plot(glow_x, glow_y, color=ACCENT, linewidth=6, alpha=0.6)
    mark = Circle((960, 820), 32, facecolor=PRIMARY, edgecolor="none")
    ax.add_patch(mark)
    fig.savefig("frame10.png", dpi=100, facecolor=DARK_BG)
    plt.close(fig)


def main():
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

