"""Create the 1D indexing and slicing diagram. Run from the repository root: python docs/unit3/00_numpy/figure_scripts/create_index_1d.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from array_diagram import ACCENT, HIGHLIGHT, UNSELECTED, draw_row


def main() -> None:
    traffic = np.array([8420, 8915, 9102, 8876, 9540, 6210, 5180])
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    n = len(traffic)
    w = 1.3  # cell width, so four-digit counts fit
    selected = np.arange(n)[0:5]  # the positions that traffic[0:5] picks
    assert (traffic[0:5] == traffic[-7:-2]).all()  # the negative-index slice picks the same days
    colors = [HIGHLIGHT if i in selected else UNSELECTED for i in range(n)]

    figure, ax = plt.subplots(figsize=(10, 5.2))
    draw_row(ax, [str(v) for v in traffic], 0, colors, fontsize=17, width=w)

    # Day names on top, positive indexes just above the cells, negative indexes below.
    for i in range(n):
        ax.text((i + 0.5) * w, 1.75, days[i], ha="center", va="bottom", fontsize=16, color="#444444")
        ax.text((i + 0.5) * w, 1.12, str(i), ha="center", va="bottom", fontsize=17)
        ax.text((i + 0.5) * w, -0.12, str(i - n), ha="center", va="top", fontsize=17)
    ax.text(-0.15, 1.5, "index", ha="right", va="center", fontsize=16)
    ax.text(-0.15, -0.45, "negative\nindex", ha="right", va="center", fontsize=16, linespacing=1.0)

    # Title: the same slice written with positive and with negative indexes, in monospace.
    ax.text(3.5 * w, 2.75, "traffic[0:5]  or  traffic[-7:-2]", ha="center", va="bottom", family="monospace",
            fontsize=20, fontweight="bold")

    # Bracket under the selected cells (0 up to, but not including, 5), then the result.
    ax.plot([0.05, 0.05, 5 * w - 0.05, 5 * w - 0.05], [-0.95, -1.1, -1.1, -0.95], color=ACCENT, linewidth=2.5)
    ax.text(2.5 * w, -1.3, str(traffic[0:5]), ha="center", va="top", family="monospace", fontsize=17)

    # Note pointing at cell 5 (also index -2), which is the stop index and is NOT included.
    ax.annotate("stop index 5 (or -2)\nis not included", xy=(5.5 * w, -0.75), xytext=(5.5 * w, -1.7), ha="center", va="top",
                fontsize=16, color=ACCENT, linespacing=1.1,
                arrowprops=dict(arrowstyle="-|>", color=ACCENT, linewidth=2.5, mutation_scale=22))
    ax.set_xlim(-2.4, 7 * w + 0.1)
    ax.set_ylim(-2.7, 3.3)
    ax.set_aspect("equal")
    ax.axis("off")

    output = Path(__file__).parents[1] / "images" / "index_1d.png"
    figure.savefig(output, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
