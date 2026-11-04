"""Create the beam deflection plot (default Matplotlib style). Run from the repository root: python docs/unit3/00_numpy/figure_scripts/create_beam_deflection.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    L = 20 * 12          # span, in
    w = 1500 / 12        # uniform load, lb/in (1.5 kip/ft)
    E = 29_000_000       # modulus of elasticity of steel, psi
    I = 204              # moment of inertia of a W12x26, in^4

    x = np.linspace(0, L, 101)
    y = -w * x * (L**3 - 2 * L * x**2 + x**3) / (24 * E * I)

    print(f"Largest deflection: {abs(y.min()):.2f} in")
    print(f"Allowed (L/360):    {L / 360:.2f} in")

    figure = plt.figure()
    plt.plot(x / 12, y)
    plt.xlabel("Distance along beam (ft)")
    plt.ylabel("Deflection (in)")
    plt.title("Simply supported beam, uniform load")

    output = Path(__file__).parents[1] / "images" / "beam_deflection.png"
    figure.savefig(output, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(figure)


if __name__ == "__main__":
    main()
