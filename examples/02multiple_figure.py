import numpy as np
from utatane import as_command, subplot


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


@as_command
def main(plt):
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    with subplot(plt, nrows=2, ncols=1) as nth:
        with nth(1):
            plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

        with nth(2):
            plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
