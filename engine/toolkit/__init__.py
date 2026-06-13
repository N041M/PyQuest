"""The tester: the `T` object handed to each puzzle's tests.py `check(T)`.

It both runs the learner's code and raises *translated* failures, so a
missing function, a syntax error, a wrong result, and a crash each become a
different, friendly message.

The package is composed by concern; dependencies point down this list:

    errors.py      the four translated failure categories
    textutil.py    normalize / short_tb / fmt_args
    guard.py       ExecutionGuard -- the ONE place in-process learner code runs
    runners.py     script/import execution + the tape of recorded runs/calls
    asserts.py     behavior assertions (eq, approx, raises, ...)
    liveness.py    ablation engine: is a construct live? (consumes the tape)
    constructs.py  uses_* / print_* / assigns_* checks (judged by liveness)
    lines.py       prescribed-expression checks for fixed-output puzzles
    perf.py        bonus(T) timing helpers

`Toolkit` is a thin facade: it owns the shared state (path/mode, the guard,
the tape, the AST + liveness caches) and inherits each method group as a
mixin, so tests.py keeps the flat `T.eq(...)` / `T.uses_op(...)` surface.
The import path is unchanged: `from engine.toolkit import Toolkit, ...`.
"""

from ..config import TIMEOUT
from .errors import (PuzzleSyntaxError, MissingSymbolError,
                     WrongResultError, PuzzleCrashError)
from .textutil import normalize, short_tb, fmt_args
from .guard import ExecutionGuard, NO_STDIN_MSG, EXIT_MSG
from .runners import RunnersMixin
from .asserts import AssertsMixin
from .liveness import LivenessMixin
from .constructs import ConstructsMixin
from .lines import LinesMixin
from .perf import PerfMixin

__all__ = ["Toolkit", "load_module",
           "PuzzleSyntaxError", "MissingSymbolError",
           "WrongResultError", "PuzzleCrashError",
           "normalize", "short_tb", "fmt_args",
           "NO_STDIN_MSG", "EXIT_MSG"]


class Toolkit(RunnersMixin, AssertsMixin, LivenessMixin, ConstructsMixin,
              LinesMixin, PerfMixin):
    """One check's tester. Holds the state every mixin works against."""

    def __init__(self, path, mode, timeout=TIMEOUT):
        self.path = path
        self.mode = mode
        self.guard = ExecutionGuard(timeout)
        self._module = None         # import-mode module cache
        self._tree = None           # parsed AST cache
        # the tape: everything the tests fed the solution, for the liveness
        # re-runs (and for audit.py's replay attack)
        self._runs = []             # script mode: (stdin, files, stdout)
        self._calls = []            # import mode: (name, args, kwargs)
        self._live_base = None      # cached baseline behavior signature
        self._live_base_done = False

    # timeout and printed live on the guard; surfaced here so tests and the
    # engine self-test can keep saying T.timeout / T.printed.
    @property
    def timeout(self):
        return self.guard.timeout

    @timeout.setter
    def timeout(self, seconds):
        self.guard.timeout = seconds

    @property
    def printed(self):
        """Stdout captured from the last guarded load/call."""
        return self.guard.printed


def load_module(path):
    """Import a solution fresh, under the full execution guard.

    Kept as a module-level function for compatibility; it simply borrows a
    throwaway Toolkit's guard."""
    return Toolkit(path, "import").load()
