import contextlib
from functools import partial
from ..actions import _figure_pool  # xxx


@contextlib.contextmanager
def _with_subplot(plt, nrows, ncols, i, **kwargs):
    yield plt.subplot(nrows, ncols, i, **kwargs)


@contextlib.contextmanager
def subplot(plt, nrows, ncols, **kwargs):
    yield partial(_with_subplot, plt, nrows, ncols, **kwargs)


@contextlib.contextmanager
def window(plt, i):
    if plt not in _figure_pool:
        _figure_pool[plt] = []
    fig = plt.figure(i)
    _figure_pool[plt].append(fig)
    yield fig
