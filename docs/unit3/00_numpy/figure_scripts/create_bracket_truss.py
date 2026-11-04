"""Create the two-member wall bracket truss diagram. Run from the repository root: python docs/unit3/00_numpy/figure_scripts/create_bracket_truss.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Polygon

BLUE = "#0072B2"
ORANGE = "#E69F00"
RED = "#D62728"
GREY = "#666666"


def draw_pin(ax: plt.Axes, y: float, size: float = 1.0) -> None:
    """Orange triangle with its base on the wall (x = 0) and its tip at the joint (pointing right)."""
    ax.add_patch(Polygon([(0, y - size / 2), (0, y + size / 2), (size * 0.8, y)], closed=True, facecolor=ORANGE, edgecolor=ORANGE, zorder=2))


def main() -> None:
    L = 6.0
    h = L * np.tan(np.radians(30))
    theta = np.degrees(np.arctan2(h, L))

    figure, ax = plt.subplots(figsize=(8, 5))

    # Wall with hatch marks on its left side
    top, bottom = h + 0.9, -0.9
    ax.plot([0, 0], [bottom, top], color="#888888", linewidth=6, solid_capstyle="butt", zorder=1)
    for y in np.arange(bottom + 0.2, top, 0.4):
        ax.plot([0, -0.35], [y, y - 0.35], color="#888888", linewidth=1.8, zorder=1)

    # Members
    ax.plot([0, L], [h, h], color=BLUE, linewidth=7, solid_capstyle="round", zorder=3)
    ax.plot([0, L], [0, h], color=BLUE, linewidth=7, solid_capstyle="round", zorder=3)

    # Pin supports and joints
    draw_pin(ax, h)
    draw_pin(ax, 0)
    ax.plot([0, 0, L], [h, 0, h], "o", color="black", markersize=13, zorder=5)

    # Load P at C
    ax.annotate("", xy=(L, h - 1.5), xytext=(L, h - 0.25), arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=4, mutation_scale=30), zorder=4)
    ax.text(L + 0.2, h - 0.95, "P", color=RED, fontsize=22, ha="left", va="center")

    # Angle theta at B
    ax.plot([0, 2.6], [0, 0], color="black", linewidth=2, linestyle="--", zorder=2)
    ax.add_patch(Arc((0, 0), 3.2, 3.2, theta1=0, theta2=theta, color="black", linewidth=2, zorder=4))
    mid = np.radians(theta / 2)
    ax.text(2.35 * np.cos(mid) + 0.1, 2.35 * np.sin(mid) - 0.05, "θ", fontsize=24, ha="left", va="center")

    # Joint labels
    ax.text(0.8, h + 0.35, "A", fontsize=24, ha="center", va="bottom")
    ax.text(0.8, -0.35, "B", fontsize=24, ha="center", va="top")
    ax.text(L + 0.2, h + 0.2, "C", fontsize=24, ha="left", va="bottom")

    # Member labels
    ax.text(L / 2, h + 0.25, "AC", fontsize=16, color=GREY, ha="center", va="bottom")
    ax.text(L / 2 + 0.3, h / 2 - 0.3, "BC", fontsize=16, color=GREY, ha="center", va="top")

    ax.set_aspect("equal")
    ax.set_xlim(-1.0, L + 1.0)
    ax.set_ylim(-1.5, h + 1.5)
    ax.axis("off")

    output = Path(__file__).parents[1] / "images" / "bracket_truss.png"
    figure.savefig(output, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
