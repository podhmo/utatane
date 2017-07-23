import os.path
import sys
import weakref
import contextlib
import yieldfixture
from functools import partial

# xxx:
with_context = yieldfixture.with_context
_figure_pool = weakref.WeakKeyDictionary()


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

    if plt not in _figure_pool:
        plt.savefig(filename, dpi=dpi, format=format)
        print("save:", filename, file=sys.stderr)
    else:
        basename, ext = os.path.splitext(filename)
        for i, fig in enumerate(_figure_pool[plt]):
            name = "{}{}{}".format(basename, i, ext)
            fig.savefig(name, dpi=dpi, format=format)
            print("save:", name, file=sys.stderr)
            fig.canvas.draw_idle()  # need this if 'transparent=True' to reset colors


def get_parser():
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="action")
    parser.set_defaults(action="show")

    dump_parser = subparsers.add_parser("dump")
    dump_parser.add_argument("filename")
    dump_parser.add_argument("--width", default=None, type=float)
    dump_parser.add_argument("--height", default=None, type=float)

    show_parser = subparsers.add_parser("show")  # NOQA
    return parser


class App:
    scopes = {"show": show, "dump": dump}

    def __init__(self, scopes=None):
        self.scopes = scopes or self.scopes

        self._runner, self.yield_fixture = yieldfixture.create()

    @contextlib.contextmanager
    def run_fixture(self, parser=None):
        parser = parser or get_parser()
        args = parser.parse_args()
        with self.scopes[args.action](**vars(args)) as plt:
            with self._runner.run_fixture() as ctx:
                yield plt, ctx

    def run_with(self, fn, *, parser=None):
        with self.run_fixture(parser=parser) as (plt, ctx):
            return fn(plt, *ctx.args, **ctx.kwargs)


@contextlib.contextmanager
def _with_subplot(plt, nrows, ncols, i, **kwargs):
    yield plt.subplot(nrows, ncols, i, **kwargs)


@contextlib.contextmanager
def subplot(plt, nrows, ncols):
    yield partial(_with_subplot, plt, nrows, ncols)


@contextlib.contextmanager
def window(plt, i):
    if plt not in _figure_pool:
        _figure_pool[plt] = []
    fig = plt.figure(i)
    _figure_pool[plt].append(fig)
    yield fig


@contextlib.contextmanager
def plot3d(plt):
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = Axes3D(fig)
    yield ax


app = App()
yield_fixture = app.yield_fixture
as_command = app.run_with
