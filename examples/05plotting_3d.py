import numpy as np
from utatane import as_command, plot3d


@as_command
def main(plt):
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z ** 2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    with plot3d(plt) as ax:
        ax.plot(x, y, z, "b", label='parametric curve')
        ax.grid(True)
        ax.legend()
