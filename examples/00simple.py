"""
# show image
$ python 00simple.py
# dump image
$ SAVE=00simple.svg python 00simple.py
"""
from utatane import draw

with draw() as plt:
    xs = list(range(10))
    ys = [x * x for x in xs]
    plt.plot(xs, xs, "g", label="x")
    plt.plot(xs, ys, "b", label="x * x")
