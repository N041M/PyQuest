"""The four translated failure categories every check resolves into.

checker.py turns each one into a distinct, plain-language report screen
(ARCHITECTURE invariant #6) -- raise these, never a raw exception.
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


class PuzzleCrashError(Exception):
    def __init__(self, detail, because=""):
        self.detail = detail
        self.because = because
