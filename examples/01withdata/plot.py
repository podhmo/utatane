import math
from utatane import as_command, yield_fixture


@yield_fixture
def data():
    data = [
        [(i, i) for i in range(1, 11)],
        [(i, i * i) for i in range(1, 11)],
        [(i, math.sqrt(i)) for i in range(1, 11)],
    ]
    yield {"data": {"values": data, "labels": ["i", "i*i", "sqrt(i)"]}}


@as_command
def render(plt, *, data):
    for label, rows in zip(data["labels"], data["values"]):
        xs = [row[0] for row in rows]
        ys = [row[1] for row in rows]
        plt.plot(xs, ys, label=label)
