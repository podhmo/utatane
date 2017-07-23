import contextlib
import yieldfixture
from . import actions


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
    actions = {"show": actions.show, "dump": actions.dump}

    def __init__(self, actions=None):
        self.actions = actions or self.actions

        self._runner, self.yield_fixture = yieldfixture.create()

    @contextlib.contextmanager
    def run_fixture(self, parser=None):
        parser = parser or get_parser()
        args = parser.parse_args()
        with self.actions[args.action](**vars(args)) as plt:
            with self._runner.run_fixture() as ctx:
                yield plt, ctx

    def run_with(self, fn, *, parser=None):
        with self.run_fixture(parser=parser) as (plt, ctx):
            return fn(plt, *ctx.args, **ctx.kwargs)
