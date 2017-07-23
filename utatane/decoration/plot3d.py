import contextlib


@contextlib.contextmanager
def plot3d(plt):
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = Axes3D(fig)
    yield ax
