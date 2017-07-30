import numpy as np
from utatane import as_command


@as_command
def render(plt):
    xs = np.arange(10)

    ys0 = np.power(xs, 2)
    plt.plot(xs, ys0, "bo")  # blue circle

    ys1 = np.power(xs, 1.5)
    plt.plot(xs, ys1, "r+")  # red ditto
