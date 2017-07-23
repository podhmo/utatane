from utatane import as_command, window


@as_command
def main(plt):
    xs = range(100)

    with window(plt, 0):
        plt.plot(xs, xs)

    with window(plt, 1):
        plt.plot(xs, [x * x for x in xs])
