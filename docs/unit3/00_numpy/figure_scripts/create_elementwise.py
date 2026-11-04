"""Create the element-by-element arithmetic diagram. Run from the repository root: python docs/unit3/00_numpy/figure_scripts/create_elementwise.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from array_diagram import ACCENT, HIGHLIGHT, UNSELECTED, draw_row


def main() -> None:
    quantities = np.array([120, 45, 300, 8])
    unit_prices = np.array([14.50, 62.00, 3.25, 410.00])
    line_totals = quantities * unit_prices

    width = 1.7
    figure, ax = plt.subplots(figsize=(9, 5.2))
    rows = [
        ("quantities", [str(q) for q in quantities], UNSELECTED, 3.0),
        ("unit_prices", [f"{p:.2f}" for p in unit_prices], UNSELECTED, 1.5),
        ("line_totals", [str(t) for t in line_totals], HIGHLIGHT, 0.0),
    ]
    for name, texts, color, y in rows:
        draw_row(ax, texts, y, [color] * 4, fontsize=20, width=width)
        ax.text(-0.15, y + 0.5, name, ha="right", va="center", family="monospace", fontsize=18)

    # An operator in the gap below the first and second rows, in every column.
    for c in range(4):
        ax.text(c * width + width / 2, 2.75, "×", ha="center", va="center", fontsize=30, color=ACCENT)
        ax.text(c * width + width / 2, 1.25, "=", ha="center", va="center", fontsize=30, color=ACCENT)

    ax.text(2 * width + 0.6, -0.6, "line_totals = quantities * unit_prices", ha="center", va="top",
            family="monospace", fontsize=18, fontweight="bold")
    ax.set_xlim(-3.0, 4 * width + 1.2)
    ax.set_ylim(-1.2, 4.1)
    ax.set_aspect("equal")
    ax.axis("off")

    output = Path(__file__).parents[1] / "images" / "elementwise.png"
    figure.savefig(output, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
