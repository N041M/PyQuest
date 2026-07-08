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
                     WrongResultError, LessonNotUsedError, PuzzleCrashError)
from .textutil import normalize, short_tb, fmt_args
from .guard import ExecutionGuard
from .runners import RunnersMixin
from .asserts import AssertsMixin
from .liveness import LivenessMixin
from .constructs import ConstructsMixin
from .lines import LinesMixin
from .perf import PerfMixin

__all__ = ["Toolkit",
           "PuzzleSyntaxError", "MissingSymbolError",
           "WrongResultError", "LessonNotUsedError", "PuzzleCrashError",
           "normalize", "short_tb", "fmt_args"]


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
        # the OBJECT tape: ordered make/method/attr ops for the OOP chapters, so
        # liveness can replay class/method usage (object helpers used to be off
        # the tape, degrading those puzzles to plain AST presence).
        self._ops = []              # (kind, ...) in call order; see runners.py
        self._obj_index = {}        # id(obj) -> its sequential index on the tape
        self._obj_seq = 0           # next index to hand out (make/method result)
        self._ops_replayable = True # a touched object the tape never made -> off
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
