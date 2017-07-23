import numpy as np
from utatane import as_command, plot3d
from matplotlib import cm


def func(x, y):
    return x ** 2 + y ** 2


@as_command
def main(plt):
    x = np.arange(-5, 5, 0.05)
    y = np.arange(-5, 5, 0.05)

    X, Y = np.meshgrid(x, y)

    Z = func(X, Y)

    with plot3d(plt) as ax:
        ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
