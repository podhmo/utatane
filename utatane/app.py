import contextlib
from functools import partial
from dictknife import loading
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


class Dispatcher:
    def __init__(self, fixtures):
        self.fixtures = fixtures

    def get_name(self, f):
        return f.__name__

    def dispatch_fixture(self, f, ctx, *, args):
        name = self.get_name(f)
        if getattr(args, name, None) is not None:
            return load_from_filename(name, getattr(args, name))
        return yieldfixture.dispatch_default(f, ctx)

    def dispatch_commandline_arguments(self, parser):
        parser = parser or get_parser()
        for f in self.fixtures:
            parser.add_argument("--{}".format(self.get_name(f), default=None))
        return parser.parse_args()


@contextlib.contextmanager
def load_from_filename(name, filename):
    yield {name: loading.loadfile(filename)}


class App:
    actions = {"show": actions.show, "dump": actions.dump}

    def __init__(self, actions=None):
        self.actions = actions or self.actions
        self.fixtures = []

    def yield_fixture(self, fixture):
        self.fixtures.append(fixture)
        return fixture

    @contextlib.contextmanager
    def run_fixture(self, parser=None, kwargs=None):
        dispatcher = Dispatcher(self.fixtures)
        args = dispatcher.dispatch_commandline_arguments(parser)
        fixture_manager = yieldfixture.App(dispatcher=partial(dispatcher.dispatch_fixture, args=args))

        for f in self.fixtures:
            fixture_manager.yield_fixture(f)

        with self.actions[args.action](**vars(args), **kwargs) as plt:
            with fixture_manager.run_fixture() as ctx:
                yield plt, ctx

    def run_with(self, fn=None, *, parser=None, **kwargs):
        if fn is None:
            return partial(self.run_with, parser=parser, **kwargs)
        else:
            with self.run_fixture(parser=parser, kwargs=kwargs) as (plt, ctx):
                return fn(plt, *ctx.args, **ctx.kwargs)
