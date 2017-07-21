import sys
import os
import contextlib


@contextlib.contextmanager
def show():
    import matplotlib.pyplot as plt
    plt.style.use("ggplot")
    yield plt
    plt.legend()
    plt.show()


@contextlib.contextmanager
def save(*, name="fig.svg", w=400, h=300):
    import matplotlib
    matplotlib.use("AGG")  # NOQA
    import matplotlib.pyplot as plt  # NOQA
    plt.style.use("ggplot")
    yield plt
    dpi = float(plt.gcf().get_dpi())
    plt.gcf().set_size_inches(w / dpi, h / dpi)
    print("save:", name, file=sys.stderr)
    plt.savefig(name, dpi=dpi)


def draw(*, name="SAVE", **kwargs):
    filename = os.getenv(name)
    if filename:
        if "name" not in kwargs:
            kwargs["name"] = filename
        return save(**kwargs)
    else:
        return show()
