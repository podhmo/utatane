from utatane import as_command
import numpy as np


@as_command
def render(plt):
    xs = np.arange(20)
    ys = np.random.rand(5, 20)
    ys[1] += ys[0]
    ys[2] += ys[1]
    ys[3] += ys[2]
    ys[4] += ys[3]
    plt.stackplot(xs, ys[0], ys[1], ys[2], ys[3], ys[4])
