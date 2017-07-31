import numpy as np
from utatane import as_command


@as_command
def render(plt):
    xs = np.arange(10)

    plt.step(xs, np.power(xs, 2), label="x ** 2")
    plt.step(xs, np.power(xs, 1.75), label="x ** 1.75")
    plt.step(xs, np.power(xs, 1.5), label="x ** 1.5")
    plt.step(xs, np.power(xs, 1.25), label="x ** 1.25")
