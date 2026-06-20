"""The execution guard: the ONE place in-process learner code runs.

Every execution -- importing the file, calling a function, timing it, a
liveness re-run -- goes through `ExecutionGuard.guarded`, which

  - feeds stdin (blank by default, so a stray input() fails fast instead of
    hanging; liveness passes recorded stdin via `_stdin=`),
  - captures stdout into `.printed` (assertable, and off the report screen),
  - enforces a wall-clock timeout (an infinite loop fails, not hangs) on the
    POSIX main thread; off it (Windows, a worker thread) the in-process alarm
    silently no-ops -- see the timeout note below,
  - translates exit()/sys.exit() (learner code cannot kill the checker),
  - moves the working directory into a throwaway sandbox so RELATIVE-path
    file I/O lands there, not in the project; file puzzles get fixtures via
    put_file.

This is a convenience boundary, not a security one. The sandbox is a chdir:
it contains honest mistakes (a stray open("out.txt", "w")), NOT a determined
absolute-path write (open("/etc/...")), os.system, or shutil.rmtree. The
threat model is a learner's accident on their own machine, not malice; do not
rely on it to run untrusted code. The timeout likewise covers script mode
cross-platform (subprocess) but in-process import/liveness runs only on the
POSIX main thread. guarded() also mutates global process state (os.chdir,
sys.stdin/stdout), so it is correct only single-threaded -- a threaded
tests.py would corrupt it.

Script mode gets stronger isolation from its subprocess (cross-platform
timeout + sandbox cwd) -- see runners.py. Never invoke learner code outside
this guard; `python3 tools/audit.py --engine` pins these guarantees.
"""

import io
import os
import sys
import signal
import tempfile

from .errors import PuzzleCrashError


NO_STDIN_MSG = (
    "input() was called, but import-mode puzzles get their values as function\n"
    "arguments -- the checker calls your function directly, so there is no\n"
    "keyboard to read. Remove the input() and use the parameters instead.")

EXIT_MSG = (
    "your code called exit()/sys.exit(), which tries to stop the whole\n"
    "program. A puzzle should finish by returning (or just ending) -- remove\n"
    "the exit call.")


class _Timeout(BaseException):
    """Raised by the alarm inside learner code. BaseException on purpose:
    a learner's `except Exception:` must not be able to swallow it."""


class ExecutionGuard:
    """Owns the sandbox cwd, the wall-clock alarm, and the stdout capture."""

    def __init__(self, timeout):
        self.timeout = timeout
        self.printed = ""           # stdout captured from the last guarded run
        self._sandbox = None

    def sandbox(self):
        """The temp directory all learner code runs in. Shared across the
        runs/calls of one check, so a file written by one run is visible to
        the next (which file puzzles may rely on)."""
        if self._sandbox is None:
            self._sandbox = tempfile.mkdtemp(prefix="pyquest_sandbox_")
        return self._sandbox

    def put_file(self, name, content):
        """Create a fixture file the learner's code can open by name."""
        with open(os.path.join(self.sandbox(), name), "w", encoding="utf-8") as f:
            f.write(content)

    def guarded(self, because, fn, *args, **kwargs):
        """Run learner code with every protection on. Infrastructure failures
        (hang, exit, stray input) become PuzzleCrashError; the learner's own
        exceptions pass through untouched for the caller to interpret.

        `_stdin` (popped, never passed to fn) feeds text to input() -- used by
        the liveness re-runs, which replay recorded stdin in-process."""
        stdin_text = kwargs.pop("_stdin", "")
        old_stdin, old_stdout = sys.stdin, sys.stdout
        sys.stdin = io.StringIO(stdin_text)
        buf = sys.stdout = io.StringIO()
        try:
            old_cwd = os.getcwd()
        except OSError:
            old_cwd = None
        os.chdir(self.sandbox())
        def on_alarm(signum, frame):
            raise _Timeout()

        alarmed = False
        try:                        # SIGALRM: main thread on Unix; else skip
            old_handler = signal.signal(signal.SIGALRM, on_alarm)
            signal.alarm(self.timeout)
            alarmed = True
        except (ValueError, AttributeError):
            pass
        try:
            return fn(*args, **kwargs)
        except _Timeout:
            raise PuzzleCrashError(
                "Your code ran longer than %ds -- maybe an endless loop?"
                % self.timeout, because=because)
        except EOFError:
            raise PuzzleCrashError(NO_STDIN_MSG, because=because)
        except SystemExit:
            raise PuzzleCrashError(EXIT_MSG, because=because)
        finally:
            if alarmed:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old_handler)
            sys.stdin, sys.stdout = old_stdin, old_stdout
            if old_cwd is not None:
                os.chdir(old_cwd)
            self.printed = buf.getvalue()
