"""Create the 2 x 2 panel of 2D indexing examples. Run from the repository root: python docs/unit3/00_numpy/figure_scripts/create_index_2d.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from array_diagram import draw_grid


def main() -> None:
    concrete = np.array([[120, 95, 140, 110], [80, 85, 90, 100], [150, 160, 130, 145]])
    examples = [
        ("concrete[1]", concrete[1], [(1, c) for c in range(4)]),
        ("concrete[2, 2]", concrete[2, 2], [(2, 2)]),
        ("concrete[0, 1:4]", concrete[0, 1:4], [(0, c) for c in range(1, 4)]),
        ("concrete[:, 0]", concrete[:, 0], [(r, 0) for r in range(3)]),
    ]
    rows = [str(i) for i in range(3)]
    cols = [str(i) for i in range(4)]

    figure, axes = plt.subplots(2, 2, figsize=(8, 7.5))
    for ax, (code, result, selected) in zip(axes.flat, examples):
        draw_grid(ax, concrete, selected, rows, cols, fontsize=17, label_size=15)
        ax.set_title(code, family="monospace", fontsize=19, fontweight="bold", pad=30)
        ax.text(2, -3.3, str(result), ha="center", va="top", family="monospace", fontsize=17)
        ax.set_ylim(-3.9, 0.1)
    figure.tight_layout(h_pad=1.5, w_pad=0)

    output = Path(__file__).parents[1] / "images" / "index_2d.png"
    figure.savefig(output, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
