from utatane import command


with command() as plt:
    xs = range(100)
    plt.figure(0)
    plt.plot(xs, xs)
    plt.figure(1)
    plt.hold(True)
    plt.plot(xs, [x * x for x in xs])
