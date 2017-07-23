from utatane import as_command


@as_command
def main(plt):
    xs = list(range(10))
    ys = [x * x for x in xs]
    plt.plot(xs, xs, "g", label="x")
    plt.plot(xs, ys, "b", label="x * x")
