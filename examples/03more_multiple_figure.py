# from https://matplotlib.org/users/pyplot_tutorial.html
from utatane import yield_fixture, as_command, subplot
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale


@yield_fixture
def fixture():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # make up some data in the interval ]0, 1[
    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    y = y[(y > 0) & (y < 1)]
    y.sort()
    x = np.arange(len(y))
    yield {"x": x, "y": y}


@as_command
def main(plt, *, x, y):
    with subplot(plt, nrows=2, ncols=2) as nth:
        # linear
        with nth(1) as ax:
            plt.plot(x, y, "b")
            ax.set_yscale('linear')
            ax.set_title('linear')
            ax.grid(True)

        # log
        with nth(2) as ax:
            plt.plot(x, y, "b")
            ax.set_yscale('log')
            ax.set_title('log')
            ax.grid(True)

        # symmetric log
        with nth(3) as ax:
            plt.plot(x, y - y.mean(), "b")
            ax.set_yscale('symlog', linthreshy=0.01)
            ax.set_title('symlog')
            ax.grid(True)

        # logit
        with nth(4) as ax:
            plt.plot(x, y, "b")
            ax.set_yscale('logit')
            ax.set_title('logit')
            ax.grid(True)

    # Format the minor tick labels of the y-axis into empty strings with
    # `NullFormatter`, to avoid cumbering the axis with too many labels.
    plt.gca().yaxis.set_minor_formatter(NullFormatter())
    # Adjust the subplot layout, because the logit one may take more space
    # than usual, due to y-tick labels like "1 - 10^{-3}"
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
