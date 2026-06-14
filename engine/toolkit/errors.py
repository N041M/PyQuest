"""The translated failure categories every check resolves into.

checker.py turns each one into a distinct, plain-language report screen
(ARCHITECTURE invariant #6) -- raise these, never a raw exception. Four are
behavioral (syntax / missing symbol / wrong result / crash); LessonNotUsedError
is the construct-check variant of WrongResultError -- the answer is right but
the lesson's tool was skipped -- and gets its own 'so close' screen.
"""


class PuzzleSyntaxError(Exception):
    def __init__(self, detail):
        self.detail = detail


class MissingSymbolError(Exception):
    def __init__(self, name):
        self.name = name


class WrongResultError(Exception):
    def __init__(self, expected, actual, because=""):
        self.expected = expected
        self.actual = actual
        self.because = because


class LessonNotUsedError(WrongResultError):
    """The output is correct, but the solution reached it without the
    construct the puzzle is teaching. A subclass of WrongResultError so every
    existing `except WrongResultError` still catches it; checker.py catches it
    FIRST to render a distinct 'right answer, wrong lesson' screen. Construct
    and line_* checks raise this -- and because behavior assertions run before
    them (the standing convention), reaching one means the answer already
    matched."""


class PuzzleCrashError(Exception):
    def __init__(self, detail, because=""):
        self.detail = detail
        self.because = because
