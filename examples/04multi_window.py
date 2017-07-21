from utatane import as_command


@as_command
def main(plt):
    xs = range(100)
    plt.figure(0)
    plt.plot(xs, xs)
    plt.figure(1)
    plt.plot(xs, [x * x for x in xs])
