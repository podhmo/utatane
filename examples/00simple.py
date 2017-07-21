from utatane import command

with command() as plt:
    xs = list(range(10))
    ys = [x * x for x in xs]
    plt.plot(xs, xs, "g", label="x")
    plt.plot(xs, ys, "b", label="x * x")
