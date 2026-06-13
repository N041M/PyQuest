"""Prescribed-expression checks, for fixed-output puzzles.

A puzzle with no input can never be randomized, and liveness can't tell
`print(7*2)` from `print(2+3*4)` -- both compute. Where the lesson IS a
specific expression, these three pin the i-th print() call's argument
(straight-line scripts: print #i produces line i).

Mixin contract -- needs ConstructsMixin (_print_calls).
"""

import ast

from .errors import WrongResultError
from .constructs import OPS


class LinesMixin:

    def print_expr(self, i, because=""):
        calls = sorted(self._print_calls(),
                       key=lambda c: (c.lineno, c.col_offset))
        if len(calls) <= i:
            raise WrongResultError("at least %d separate print() calls"
                                   % (i + 1),
                                   "only %d found" % len(calls), because)
        if not calls[i].args:
            raise WrongResultError("a value inside print() #%d" % (i + 1),
                                   "that print shows nothing", because)
        return calls[i].args[0]

    def line_uses_op(self, i, op, because=""):
        """Print #i's expression itself computes with `op` -- the operator
        can't live in some other line or variable."""
        expr = self.print_expr(i, because)
        opcls = OPS[op]
        if not any(isinstance(n, ast.BinOp) and isinstance(n.op, opcls)
                   for n in ast.walk(expr)):
            raise WrongResultError(
                "print #%d computing with '%s'" % (i + 1, op),
                "that print doesn't use '%s'" % op, because)

    def line_shape(self, i, outer, inner, because=""):
        """Print #i contains `inner` evaluated before `outer`: a BinOp(outer)
        with a BinOp(inner) as a direct operand. `(2 + 3) * 4` is
        Mult(Add(2, 3), 4) -- a shape only parentheses can write."""
        expr = self.print_expr(i, because)
        o_cls, i_cls = OPS[outer], OPS[inner]
        for node in ast.walk(expr):
            if isinstance(node, ast.BinOp) and isinstance(node.op, o_cls):
                for side in (node.left, node.right):
                    if isinstance(side, ast.BinOp) \
                            and isinstance(side.op, i_cls):
                        return
        raise WrongResultError(
            "print #%d grouped so '%s' happens before '%s'"
            % (i + 1, inner, outer),
            "no such grouping in that print", because)

    def line_only_literals(self, i, allowed, because=""):
        """Print #i's expression is built only from the task's own literal
        values (type-strict) -- no other numbers, variables, or calls."""
        expr = self.print_expr(i, because)
        permitted = (ast.BinOp, ast.UnaryOp, ast.Constant,
                     ast.operator, ast.unaryop, ast.expr_context)
        lits = []
        for n in ast.walk(expr):
            if not isinstance(n, permitted):
                raise WrongResultError(
                    "print #%d built only from the task's values" % (i + 1),
                    "it takes a detour (a variable, call, ...)", because)
            if isinstance(n, ast.Constant):
                lits.append(n.value)
        shown = ", ".join(sorted(set(repr(a) for a in allowed)))
        if not lits:
            raise WrongResultError(
                "print #%d computing from %s" % (i + 1, shown),
                "no values found in it", because)
        for v in lits:
            if not any(type(v) is type(a) and v == a for a in allowed):
                raise WrongResultError(
                    "print #%d using only %s" % (i + 1, shown),
                    "it uses %r" % (v,), because)
