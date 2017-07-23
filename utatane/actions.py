import os.path
import sys
import weakref
import contextlib

# xxx:
_figure_pool = weakref.WeakKeyDictionary()


@contextlib.contextmanager
def show(style="ggplot", legend=True, **kwargs):
    import matplotlib.pyplot as plt
    if style:
        plt.style.use(style)

    yield plt

    # subplot's label is not supported, yet
    if legend and plt.gca().get_legend_handles_labels()[0]:
        plt.legend()
    plt.show()


@contextlib.contextmanager
def dump(*, style="ggplot", legend=True, filename="fig.svg", width=None, height=None, format=None, **kwargs):
    import matplotlib
    matplotlib.use("AGG")  # NOQA
    import matplotlib.pyplot as plt  # NOQA
    if style:
        plt.style.use(style)

    yield plt

    # subplot's label is not supported, yet
    if legend and plt.gca().get_legend_handles_labels()[0]:
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
