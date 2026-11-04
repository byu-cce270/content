"""Create the arange versus linspace number lines. Run from the repository root: python docs/unit3/00_numpy/figure_scripts/create_arange_linspace.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from array_diagram import ACCENT, HIGHLIGHT

SPAN = 50  # length of the number line, ft


def draw_number_line(ax, y, code, values, result):
    """Draw a 0-SPAN number line at height y with the code above it, dots at values, and the printed result below."""
    ax.plot([0, SPAN], [y, y], color="#444444", linewidth=2.5, zorder=1)
    for tick in range(0, SPAN + 1, 10):
        ax.plot([tick, tick], [y - 0.12, y + 0.12], color="#444444", linewidth=2.5, zorder=1)
        ax.text(tick, y - 0.25, str(tick), ha="center", va="top", fontsize=16)
    ax.plot(values, [y] * len(values), "o", color=HIGHLIGHT, markersize=17, markeredgecolor="#111111", zorder=3)
    ax.text(0, y + 0.55, code, ha="left", va="bottom", family="monospace", fontsize=19, fontweight="bold")
    ax.text(SPAN / 2, y - 0.95, result, ha="center", va="top", family="monospace", fontsize=16)


def main() -> None:
    stepped = np.arange(0, SPAN, 10)       # you choose the step; the stop value is left out
    spaced = np.linspace(0, SPAN, 9)       # you choose the count; NumPy works out the step
    segments = len(spaced) - 1

    figure, ax = plt.subplots(figsize=(10, 5.6))
    draw_number_line(ax, 3.6, f"np.arange(0, {SPAN}, 10)", stepped, str(stepped))
    draw_number_line(ax, 0, f"np.linspace(0, {SPAN}, 9)", spaced, str(spaced))

    # Open (hollow) marker where arange stops: the stop value is not included.
    ax.plot([SPAN], [3.6], "o", markersize=17, markerfacecolor="white", markeredgecolor=ACCENT, markeredgewidth=3,
            zorder=3)
    ax.text(SPAN, 4.15, f"{SPAN} not included", ha="right", va="bottom", fontsize=16, color=ACCENT)

    # linspace: the count is what you choose; the spacing comes out of it.
    ax.text(SPAN / 2, -1.6, f"{segments} equal segments need {len(spaced)} points, {spaced[1]} apart",
            ha="center", va="top", fontsize=16, color=ACCENT)

    ax.set_xlim(-3, SPAN + 3)
    ax.set_ylim(-2.4, 5.1)
    ax.axis("off")

    output = Path(__file__).parents[1] / "images" / "arange_linspace.png"
    figure.savefig(output, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
