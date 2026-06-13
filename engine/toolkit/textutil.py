"""Small text utilities shared across the tester."""

import traceback


def normalize(s):
    """Strip trailing whitespace per line and trailing blank lines."""
    if s is None:
        return ""
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in s.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def short_tb():
    tb = traceback.format_exc().strip().split("\n")
    return "\n".join(tb[-3:])


def fmt_args(args, kwargs):
    parts = [repr(a) for a in args]
    parts += ["%s=%r" % (k, v) for k, v in kwargs.items()]
    return ", ".join(parts)
