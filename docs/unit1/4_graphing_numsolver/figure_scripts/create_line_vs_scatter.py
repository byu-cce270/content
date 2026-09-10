"""Create the line-chart versus XY-scatter comparison used in Topic 4."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    x = np.array([0, 1, 4, 10, 11], dtype=float)
    y = np.array([1.0, 2.1, 3.0, 5.2, 5.7])
    categories = np.arange(len(x))

    figure, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)

    axes[0].plot(categories, y, color="#0072B2", marker="o", linewidth=2.2)
    axes[0].set_xticks(categories, [f"{value:g}" for value in x])
    axes[0].set_title("Line chart: x-values are categories")
    axes[0].set_xlabel("Displayed x-value (equally spaced)")
    axes[0].set_ylabel("Measured response, y")

    axes[1].plot(x, y, color="#D55E00", marker="o", linewidth=2.2)
    axes[1].set_xticks(x)
    axes[1].set_title("XY scatter: x-values set position")
    axes[1].set_xlabel("Numerical x-value (true spacing)")

    for axis in axes:
        axis.grid(True, color="#D9D9D9", linewidth=0.8)
        axis.set_ylim(0, 6.3)
        axis.spines[["top", "right"]].set_visible(False)

    figure.suptitle("Same data pairs, different horizontal-axis interpretation", fontsize=13)
    figure.tight_layout()

    output = Path(__file__).resolve().parents[1] / "graphing_images" / "line_vs_scatter.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
