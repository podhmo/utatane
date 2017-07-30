import matplotlib
matplotlib.use("Agg")  # NOQA
from matplotlib import pyplot as plt
from utatane import subplot
from collections import defaultdict


def defined_with(mro, name):
    owner = None
    for cls in mro:
        if not hasattr(cls, name):
            return owner
        owner = cls


with subplot(plt, ncols=1, nrows=1) as nth:
    with nth(1) as ax:
        print("hierarchy(mro)")
        print("")
        mro = [ax, *ax.__class__.mro()]
        for cls in mro:
            print("-", cls)

        d = defaultdict(list)
        for attr in sorted(dir(ax)):
            d[defined_with(mro, attr)].append(attr)

        for cls in mro:
            attrs = d[cls]
            print("")
            print(cls)
            print("")
            for attr in attrs:
                if callable(getattr(cls, attr)):
                    if not any(attr.startswith(x) for x in ("_", "get_", "set_", "add_", "update_")):
                        print("-", attr)
