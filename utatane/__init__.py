import sys
import contextlib
from collections import ChainMap


@contextlib.contextmanager
def show(**kwargs):
    import matplotlib.pyplot as plt
    plt.style.use("ggplot")

    yield plt

    # subplot's label is not supported, yet
    if plt.gca().get_legend_handles_labels()[0]:
        plt.legend()
    plt.show()


@contextlib.contextmanager
def dump(*, filename="fig.svg", width=None, height=None, format=None, **kwargs):
    import matplotlib
    matplotlib.use("AGG")  # NOQA
    import matplotlib.pyplot as plt  # NOQA
    plt.style.use("ggplot")

    yield plt

    # subplot's label is not supported, yet
    if plt.gca().get_legend_handles_labels()[0]:
        plt.legend()

    dpi = None
    if width or height:
        w = width or height
        h = height or width
        dpi = float(plt.gcf().get_dpi())
        plt.gcf().set_size_inches(w / dpi, h / dpi)

    # it is not supported yet, in multiple windows, saving multiple images
    print("save:", filename, file=sys.stderr)
    plt.savefig(filename, dpi=dpi, format=format)


def get_parser():
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="action")
    parser.set_defaults(action="show")

    dump_parser = subparsers.add_parser("dump")
    dump_parser.add_argument("filename")
    dump_parser.add_argument("--width", default=None)
    dump_parser.add_argument("--height", default=None)

    show_parser = subparsers.add_parser("show")  # NOQA
    return parser


class App:
    scopes = {"show": show, "dump": dump}

    def __init__(self, scopes=None):
        self.fixtures = []
        self.scopes = scopes or self.scopes

    def yield_fixture(self, fixture):
        self.fixtures.append(contextlib.contextmanager(fixture))

    @contextlib.contextmanager
    def activate_scope(self, ctx, fixtures):
        if not fixtures:
            yield ctx
        else:
            args = []
            if need_context(fixtures[0]):
                args.append(ctx)
            with fixtures[0](*args) as kwargs:
                if kwargs:
                    ctx = ChainMap(kwargs, ctx)
                with self.activate_scope(ctx, fixtures[1:]) as ctx:
                    yield ctx

    def run_with(self, fn, *, parser=None):
        parser = parser or get_parser()
        args = parser.parse_args()
        with self.activate_scope({}, self.fixtures) as ctx:
            with self.scopes[args.action](**vars(args)) as plt:
                return fn(plt, **ctx)


@contextlib.contextmanager
def plot3d(plt):
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = Axes3D(fig)
    yield ax


def with_context(fn):
    fn._with_context = True
    return fn


def need_context(fn):
    return hasattr(fn, "_with_context")


app = App()
yield_fixture = app.yield_fixture
as_command = app.run_with
