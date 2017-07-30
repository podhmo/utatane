import datetime as dt
import numpy as np
from utatane import as_command


@as_command
def render(plt):
    import matplotlib.dates as mdates

    ts = mdates.drange(dt.datetime(2016, 12, 20), dt.datetime(2017, 1, 2), dt.timedelta(hours=2))
    xs = np.random.normal(0, 1, ts.size).cumsum()
    ys = np.random.normal(0, 1, ts.size).cumsum()
    zs = np.random.normal(0, 1, ts.size).cumsum()
    bottom = min(xs.min(), ys.min(), zs.min())

    xs -= bottom
    ys -= bottom
    zs -= bottom

    plt.plot_date(ts, xs, "o-", label="x")
    plt.plot_date(ts, ys, "o-", label="y")
    plt.plot_date(ts, zs, "o-", label="z")

    plt.gcf().autofmt_xdate()
