import numpy as np
from utatane import as_command


@as_command
def render(plt):
    xs = np.random.randn(1, 100)
    ys = np.random.randn(1, 100)

    plt.scatter(xs, ys, color="b", label="xs")

    zs = np.random.randn(1, 100) * 0.5 + 0.5
    plt.scatter(xs, zs, color="g", label="zs")
