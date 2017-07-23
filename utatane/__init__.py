import yieldfixture
from utatane.decoration import (  # NOQA
    subplot,
    window,
    plot3d,
)
from utatane.app import App

app = App()

# short cut
with_context = yieldfixture.with_context
yield_fixture = app.yield_fixture
as_command = app.run_with
