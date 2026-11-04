"""Shared helpers that draw NumPy arrays as grids or rows of labelled cells."""

import matplotlib.pyplot as plt

HIGHLIGHT = "#E69F00"   # selected cells (colorblind-safe orange)
UNSELECTED = "#E6E6E6"  # ordinary cells (light gray)
ACCENT = "#0072B2"      # arrows, brackets, and notes (blue)
ACCENT2 = "#56B4E9"     # second accent (light blue) for the column totals
TEXT = "#111111"        # dark text that is readable on every cell color


def draw_cell(ax, x, y, text, color=UNSELECTED, fontsize=18, width=1.0, height=1.0, edgecolor="white"):
    """Draw one filled rectangle with its lower-left corner at (x, y) and centered text."""
    ax.add_patch(plt.Rectangle((x, y), width, height, facecolor=color, edgecolor=edgecolor, linewidth=3))
    ax.text(x + width / 2, y + height / 2, text, ha="center", va="center", fontsize=fontsize, color=TEXT)


def draw_grid(ax, data, selected=(), row_labels=None, col_labels=None, fontsize=18, label_size=14, aspect=1):
    """Draw a 2D array as cells (row 0 on top); cells in selected (row, col) are highlighted."""
    n_rows, n_cols = data.shape
    for r in range(n_rows):
        for c in range(n_cols):
            color = HIGHLIGHT if (r, c) in selected else UNSELECTED
            draw_cell(ax, c, -r - 1, str(data[r, c]), color, fontsize)
    for r, label in enumerate(row_labels or []):
        ax.text(-0.12, -r - 0.5, label, ha="right", va="center", fontsize=label_size)
    for c, label in enumerate(col_labels or []):
        ax.text(c + 0.5, 0.12, label, ha="center", va="bottom", fontsize=label_size)
    ax.set_xlim(-0.1, n_cols + 0.1)
    ax.set_ylim(-n_rows - 0.1, 0.1)
    ax.set_aspect(aspect)
    ax.axis("off")


def draw_row(ax, texts, y, colors=None, fontsize=18, width=1.0, x0=0.0):
    """Draw a single row of cells (one text per cell) at height y; colors gives one color per cell."""
    for i, text in enumerate(texts):
        color = colors[i] if colors is not None else UNSELECTED
        draw_cell(ax, x0 + i * width, y, text, color, fontsize, width)
