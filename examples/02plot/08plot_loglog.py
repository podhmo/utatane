import numpy as np
from utatane import as_command


@as_command
def render(plt):
    xs = np.arange(20)
    plt.loglog(xs, np.power(xs, xs), label="x^x")
    plt.loglog(xs, np.power(np.pi, xs), label="e^x")
    plt.loglog(xs, np.power(xs, 2), label="x^2")
    plt.loglog(xs, xs, label="x")
