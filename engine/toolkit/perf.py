"""Performance helpers for bonus(T) checks (advisory; wall-clock, so keep
budgets generous -- prefer scales() over absolute time).

Mixin contract -- needs RunnersMixin (func/_guarded).
"""

import time

from .errors import PuzzleCrashError, WrongResultError
from .textutil import short_tb


class PerfMixin:

    def time_call(self, name, *args, runs=5, **kwargs):
        """Best-of-`runs` wall-clock seconds for one call."""
        fn = self.func(name)
        because = "while timing %s" % name
        best = None
        for _ in range(max(1, runs)):
            t0 = time.perf_counter()
            try:
                self._guarded(because, fn, *args, **kwargs)
            except PuzzleCrashError:
                raise
            except Exception:
                raise PuzzleCrashError(short_tb(), because=because)
            dt = time.perf_counter() - t0
            best = dt if best is None else min(best, dt)
        return best

    def scales(self, name, make_input, n_small, n_big, slack=2.0, runs=5,
               because=""):
        """Doubling experiment: check the function grows ~linearly.

        Times the call on a small and a big input and compares the time ratio
        to the input-size ratio. An O(n) solution scales with the input; an
        O(n^2) one grows far faster and trips the `slack` threshold.
        """
        fn = self.func(name)
        guard_because = "while timing %s" % name

        def best(n):
            arg = make_input(n)
            b = None
            for _ in range(max(1, runs)):
                t0 = time.perf_counter()
                self._guarded(guard_because, fn, arg)
                dt = time.perf_counter() - t0
                b = dt if b is None else min(b, dt)
            return b

        t1, t2 = best(n_small), best(n_big)
        if t1 < 1e-5:           # too fast to measure reliably -- give the pass
            return
        size_ratio = float(n_big) / float(n_small)
        threshold = size_ratio * slack
        ratio = t2 / t1
        if ratio > threshold:
            raise WrongResultError(
                "~linear scaling (<=%.0fx slower for %.0fx input)"
                % (threshold, size_ratio),
                "%.0fx slower" % ratio,
                because or "looks slower than the target complexity")
