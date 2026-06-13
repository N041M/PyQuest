"""Running the learner's code -- and the tape of everything it was fed.

Script mode runs the file as a subprocess; import mode imports it and calls
functions/classes, always through the guard. Every run() and call() is
recorded on the tape (`_runs` / `_calls`): liveness (liveness.py) replays it
to judge whether a construct affects behavior, and audit.py's replay attack
reads it to build impostors.

Mixin contract -- provided by the Toolkit facade:
    self.path, self.mode      what to run and how
    self.guard                the ExecutionGuard
    self._module              import-mode module cache (starts None)
    self._runs, self._calls   the tape (start empty)
"""

import os
import copy
import subprocess
import importlib.util
import sys

from ..config import PY
from .errors import (PuzzleSyntaxError, MissingSymbolError,
                     WrongResultError, PuzzleCrashError)
from .textutil import normalize, short_tb, fmt_args


class RunnersMixin:

    # ---- the sandbox, surfaced for tests.py fixtures -----------------------
    def sandbox(self):
        return self.guard.sandbox()

    def put_file(self, name, content):
        """Create a fixture file the learner's code can open by name."""
        self.guard.put_file(name, content)

    def file(self, name, because=""):
        """The text of a file the learner's code wrote (translated failure
        if it never appeared)."""
        try:
            with open(os.path.join(self.sandbox(), name)) as f:
                return f.read()
        except OSError:
            raise WrongResultError("a file named %r to be written" % name,
                                   "it wasn't created", because)

    def _guarded(self, because, fn, *args, **kwargs):
        return self.guard.guarded(because, fn, *args, **kwargs)

    # ---- script mode --------------------------------------------------------
    def run(self, stdin="", files=None):
        """Run the solution as a script in the sandbox; return normalized
        stdout. `files` seeds fixture files into the sandbox first."""
        for name, content in (files or {}).items():
            self.put_file(name, content)
        try:
            proc = subprocess.run(
                [PY, self.path], input=stdin, capture_output=True,
                text=True, timeout=self.timeout, cwd=self.sandbox())
        except subprocess.TimeoutExpired:
            raise PuzzleCrashError(
                "Your program ran longer than %ds -- maybe an endless loop?"
                % self.timeout)
        if proc.returncode != 0:
            err = proc.stderr.strip()
            last = err.split("\n")[-1] if err else "unknown error"
            if "SyntaxError" in err or "IndentationError" in err:
                raise PuzzleSyntaxError(last)
            raise PuzzleCrashError(last)
        out = normalize(proc.stdout)
        self._runs.append((stdin, dict(files or {}), out))
        return out

    def source(self):
        """The raw text of the learner's work file.

        Behavior checks are the rule; this is the rare exception, for a puzzle
        whose lesson IS a specific piece of source (e.g. commenting a line out).
        """
        try:
            with open(self.path) as f:
                return f.read()
        except OSError:
            return ""

    # ---- import mode --------------------------------------------------------
    def load(self):
        if self._module is None:
            name = "pyquest_solution_under_test"
            sys.modules.pop(name, None)
            spec = importlib.util.spec_from_file_location(name, self.path)
            mod = importlib.util.module_from_spec(spec)
            try:
                self._guarded("while importing your file",
                              spec.loader.exec_module, mod)
            except PuzzleCrashError:
                raise
            except SyntaxError as e:
                raise PuzzleSyntaxError("line %s: %s" % (e.lineno, e.msg))
            except Exception:
                raise PuzzleCrashError(short_tb())
            self._module = mod
        return self._module

    def func(self, name):
        mod = self.load()
        fn = getattr(mod, name, None)
        if not callable(fn):
            raise MissingSymbolError(name)
        return fn

    def get(self, name):
        mod = self.load()
        if not hasattr(mod, name):
            raise MissingSymbolError(name)
        return getattr(mod, name)

    def _record_call(self, name, args, kwargs):
        """Remember what the tests fed the solution (args copied before the
        call -- the learner's code may mutate them)."""
        try:
            args, kwargs = copy.deepcopy(args), copy.deepcopy(kwargs)
        except Exception:
            pass                            # uncopyable: record as-is
        self._calls.append((name, args, kwargs))

    def call(self, name, *args, **kwargs):
        fn = self.func(name)
        self._record_call(name, args, kwargs)
        because = "while calling %s(%s)" % (name, fmt_args(args, kwargs))
        try:
            return self._guarded(because, fn, *args, **kwargs)
        except PuzzleCrashError:
            raise
        except Exception:
            raise PuzzleCrashError(short_tb(), because=because)

    # ---- classes & objects (for the OOP chapters) ----------------------------
    # NOTE: make/method aren't on the tape yet, so liveness degrades to the
    # plain AST check for puzzles validated only through objects. Extend the
    # tape (and the replay in liveness.py) when the OOP chapters land.
    def make(self, classname, *args, **kwargs):
        """Instantiate the learner's class; translated failures throughout."""
        cls = self.get(classname)
        if not isinstance(cls, type):
            raise MissingSymbolError(classname)
        because = "while creating %s(%s)" % (classname, fmt_args(args, kwargs))
        try:
            return self._guarded(because, cls, *args, **kwargs)
        except PuzzleCrashError:
            raise
        except Exception:
            raise PuzzleCrashError(short_tb(), because=because)

    def method(self, obj, name, *args, **kwargs):
        """Call a method on an instance made by make()."""
        m = getattr(obj, name, None)
        if not callable(m):
            raise MissingSymbolError(name)
        because = "while calling .%s(%s)" % (name, fmt_args(args, kwargs))
        try:
            return self._guarded(because, m, *args, **kwargs)
        except PuzzleCrashError:
            raise
        except Exception:
            raise PuzzleCrashError(short_tb(), because=because)

    def attr(self, obj, name):
        """An attribute of an instance, or a translated 'missing piece'."""
        if not hasattr(obj, name):
            raise MissingSymbolError(name)
        return getattr(obj, name)
