"""Create the labelled 3 x 4 array diagram. Run from the repository root: python docs/unit3/00_numpy/figure_scripts/create_array_shape.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from array_diagram import draw_grid


def main() -> None:
    concrete = np.array([[120, 95, 140, 110], [80, 85, 90, 100], [150, 160, 130, 145]])
    rows = [f"Site {name}   {i}" for i, name in enumerate("ABC")]
    cols = [f"Week {i + 1}\n{i}" for i in range(4)]

    figure, ax = plt.subplots(figsize=(10, 5.5))
    draw_grid(ax, concrete, row_labels=rows, col_labels=cols, fontsize=22, label_size=16, aspect=0.7)

    arrow = dict(arrowstyle="-|>", color="#0072B2", linewidth=2.5, mutation_scale=22)
    ax.annotate("", xy=(-1.5, -3), xytext=(-1.5, 0), arrowprops=arrow)
    ax.text(-1.85, -1.5, "axis 0 (rows)", rotation=90, ha="center", va="center", fontsize=16, color="#0072B2")
    ax.annotate("", xy=(4, 1.35), xytext=(0, 1.35), arrowprops=arrow)
    ax.text(2, 1.6, "axis 1 (columns)", ha="center", va="bottom", fontsize=16, color="#0072B2")
    ax.text(2, -3.4, "concrete.shape is (3, 4)", ha="center", va="top", fontsize=18, family="monospace")
    ax.set_xlim(-2.0, 4.1)
    ax.set_ylim(-3.9, 2.2)

    output = Path(__file__).parents[1] / "images" / "array_shape.png"
    figure.savefig(output, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
