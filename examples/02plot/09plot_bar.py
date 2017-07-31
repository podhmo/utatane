import numpy as np
from utatane import as_command


@as_command
def render(plt):
    xs = np.arange(10)
    ys = np.array(xs, copy=True)
    ys.fill(5)

    plt.bar(xs, xs, label="xs", color="r", alpha=0.3)
    plt.bar(xs, ys, label="ys", color="b", alpha=0.3)
