# https://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html
import numpy as np
from utatane import as_command


@as_command
def main(plt):
    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.barh(y_pos, performance, xerr=error, align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')
