"""Create the sum(axis=...) diagram. Run from the repository root: python docs/unit3/00_numpy/figure_scripts/create_axis_sum.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from array_diagram import ACCENT2, HIGHLIGHT, draw_cell, draw_grid


def main() -> None:
    concrete = np.array([[120, 95, 140, 110], [80, 85, 90, 100], [150, 160, 130, 145]])
    per_site = concrete.sum(axis=1)  # one total for each row
    per_week = concrete.sum(axis=0)  # one total for each column

    rows = [f"Site {name}" for name in "ABC"]
    cols = [f"Week\n{i + 1}" for i in range(4)]
    figure, ax = plt.subplots(figsize=(10, 6.2))
    draw_grid(ax, concrete, row_labels=rows, col_labels=cols, fontsize=22, label_size=15)

    # Row totals sit to the right of each row; column totals sit below each column.
    for r, total in enumerate(per_site):
        draw_cell(ax, 4.4, -r - 1, str(total), HIGHLIGHT, fontsize=22)
    for c, total in enumerate(per_week):
        draw_cell(ax, c, -4.4, str(total), ACCENT2, fontsize=22)

    ax.text(5.6, -1.5, "concrete.sum(axis=1)", ha="left", va="bottom", family="monospace", fontsize=17, fontweight="bold")
    ax.text(5.6, -1.6, "total per site\n(across each row)", ha="left", va="top", fontsize=16, linespacing=1.2)
    ax.text(2, -4.6, "concrete.sum(axis=0)", ha="center", va="top", family="monospace", fontsize=17, fontweight="bold")
    ax.text(2, -5.05, "total per week (down each column)", ha="center", va="top", fontsize=16)

    ax.set_xlim(-1.3, 8.9)
    ax.set_ylim(-5.5, 1.1)
    ax.set_aspect("equal")
    ax.axis("off")

    output = Path(__file__).parents[1] / "images" / "axis_sum.png"
    figure.savefig(output, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
