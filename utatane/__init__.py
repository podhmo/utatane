import sys
import contextlib


@contextlib.contextmanager
def show(**kwargs):
    import matplotlib.pyplot as plt
    plt.style.use("ggplot")
    yield plt
    plt.legend()
    plt.show()


@contextlib.contextmanager
def dump(*, filename="fig.svg", width=None, height=None, **kwargs):
    import matplotlib
    matplotlib.use("AGG")  # NOQA
    import matplotlib.pyplot as plt  # NOQA
    plt.style.use("ggplot")
    yield plt
    dpi = None
    if width or height:
        w = width or height
        h = height or width
        dpi = float(plt.gcf().get_dpi())
        plt.gcf().set_size_inches(w / dpi, h / dpi)
    print("save:", filename, file=sys.stderr)
    plt.savefig(filename, dpi=dpi)


def command(**kwargs):
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="action")
    subparsers.required = True

    dump_parser = subparsers.add_parser("dump")
    dump_parser.add_argument("filename")
    dump_parser.add_argument("--width", default=None)
    dump_parser.add_argument("--height", default=None)

    show_parser = subparsers.add_parser("show")  # NOQA

    args = parser.parse_args()
    return globals()[args.action](**vars(args))
