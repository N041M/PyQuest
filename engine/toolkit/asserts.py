"""Behavior assertions: compare what the code DID against what was expected.

These are the default way to validate a puzzle (ARCHITECTURE invariant #1);
construct checks (constructs.py) are the sanctioned exception.

Mixin contract -- needs RunnersMixin (func/call/_record_call/_guarded).
"""

import copy

from .errors import WrongResultError, PuzzleCrashError
from .textutil import normalize, fmt_args


class AssertsMixin:

    def eq(self, actual, expected, because="", match_case=True):
        """Equal. String outputs are compared case-SENSITIVELY by default --
        this is a Python course and capitalisation is part of the answer.
        Pass match_case=False for the rare puzzle where any casing is fine."""
        a, e = actual, expected
        if isinstance(a, str) and isinstance(e, str):
            na, ne = normalize(a), normalize(e)
            if not match_case:
                na, ne = na.casefold(), ne.casefold()
            ok = na == ne
        else:
            ok = a == e
        if not ok:
            raise WrongResultError(expected, actual, because)

    def true(self, cond, because=""):
        if not cond:
            raise WrongResultError("a true condition", cond, because)

    def is_a(self, value, typ, because=""):
        if not isinstance(value, typ):
            raise WrongResultError(typ.__name__, type(value).__name__, because)

    def raises(self, exc, name, *args, **kwargs):
        fn = self.func(name)
        self._record_call(name, args, kwargs)
        because = "while calling %s(%s)" % (name, fmt_args(args, kwargs))
        try:
            self._guarded(because, fn, *args, **kwargs)
        except exc:
            return
        except PuzzleCrashError:
            raise                   # hang/exit/input -- a real defect, surface it
        except Exception as e:
            raise WrongResultError(
                "%s to be raised" % exc.__name__, type(e).__name__,
                "A different error was raised.")
        raise WrongResultError(
            "%s to be raised" % exc.__name__, "no error raised", "")

    def _approx_eq(self, a, e, tol):
        """Numbers within tol; lists/tuples/dicts compared recursively so
        float-bearing structures can be asserted in one call."""
        if isinstance(e, bool):
            return a == e
        if isinstance(e, (int, float)):
            try:
                return abs(a - e) <= tol
            except TypeError:
                return False
        if isinstance(e, (list, tuple)):
            return (isinstance(a, (list, tuple)) and len(a) == len(e)
                    and all(self._approx_eq(x, y, tol) for x, y in zip(a, e)))
        if isinstance(e, dict):
            return (isinstance(a, dict) and set(a) == set(e)
                    and all(self._approx_eq(a[k], e[k], tol) for k in e))
        return a == e

    def approx(self, actual, expected, tol=1e-9, because=""):
        """Equal within a tolerance (floats) -- works inside lists, tuples,
        and dicts too."""
        if not self._approx_eq(actual, expected, tol):
            raise WrongResultError("%r (within %g)" % (expected, tol),
                                   actual, because)

    def any_of(self, actual, options, because="", match_case=True):
        """Accept any one of several valid answers (case-sensitive strings by
        default, like eq; pass match_case=False to ignore capitalisation)."""
        def norm(v):
            if isinstance(v, str):
                v = normalize(v)
                return v if match_case else v.casefold()
            return v
        a = norm(actual)
        if not any(a == norm(o) for o in options):
            raise WrongResultError("one of %r" % (list(options),),
                                   actual, because)

    def unordered(self, actual, expected, because=""):
        """Equal ignoring order (lists/tuples of sortable items)."""
        try:
            ok = sorted(actual) == sorted(expected)
        except TypeError:
            ok = list(actual) == list(expected)
        if not ok:
            raise WrongResultError("%r (in any order)" % (expected,),
                                   actual, because)

    def does_not_mutate(self, name, *args, **kwargs):
        """Call name(*args) and require the arguments to come back unchanged --
        for puzzles whose lesson is returning a NEW value (sorted vs .sort).
        Returns the call's result so the value can be asserted too."""
        because = kwargs.pop("because", "")
        try:
            before = copy.deepcopy(args)
        except Exception:
            # Never silently waive the lesson: if the args can't be snapshotted
            # we cannot prove non-mutation, so this is an authoring error, not a
            # pass. Use copyable inputs (lists/dicts/tuples of plain values).
            raise RuntimeError(
                "does_not_mutate needs deep-copyable arguments to verify "
                "non-mutation, but %s(...) was given an uncopyable one. "
                "Pass copyable inputs or assert the result directly." % name)
        result = self.call(name, *args, **kwargs)
        for arg, prior in zip(args, before):
            if arg != prior:
                raise WrongResultError(
                    "the input left unchanged (%r)" % (prior,),
                    "your function changed it to %r" % (arg,),
                    because or "return a new value instead of modifying "
                               "the argument")
        return result
