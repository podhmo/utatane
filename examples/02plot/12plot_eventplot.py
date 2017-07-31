from utatane import as_command
import numpy as np


@as_command
def render(plt):
    data = np.random.random([6, 50])
    colors = np.random.rand(6, 4)
    lineoffsets = np.array([-15, -3, 1, 1.5, 6, 10])
    linelengths = [5, 2, 1, 1, 3, 1.5]
    plt.eventplot(data, colors=colors, linelengths=linelengths, lineoffsets=lineoffsets)
