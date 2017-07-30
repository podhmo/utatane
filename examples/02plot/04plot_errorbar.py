import numpy as np
from utatane import as_command


@as_command
def render(plt):
    xs = np.arange(0.1, 4, 0.5)
    ys = np.exp(-xs)

    plt.errorbar(xs, ys, xerr=0.2, yerr=0.4, color="r", label="ys")

    zs = ys + 1

    # example variable error bar values
    yerr = 0.1 + 0.2 * np.sqrt(xs)
    xerr = 0.1 + yerr
    plt.errorbar(xs, zs, xerr=xerr, yerr=yerr, color="b", label="zs")
