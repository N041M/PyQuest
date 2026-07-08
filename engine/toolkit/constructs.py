"""Construct checks: confirm the LESSON was used, not just the answer.

Behavior checks (asserts.py) are the default; reach for these only where a
puzzle can be trivially gamed by typing the answer instead of computing it.
Each check finds its candidate AST nodes, then requires at least one of them
to be LIVE (liveness.py): decorative code that never affects the output
cannot satisfy a construct check. Require the *kind* of construct, not one
exact spelling, so legitimate variations still pass.

Mixin contract -- needs LivenessMixin (_find/_node/_require_live/
_live_filter/DECORATIVE/tree) which in turn needs the RunnersMixin tape.
"""

import ast

from .errors import LessonNotUsedError


# Arithmetic operator spellings -> AST classes (shared with lines.py).
OPS = {"+": ast.Add, "-": ast.Sub, "*": ast.Mult,
       "/": ast.Div, "//": ast.FloorDiv, "%": ast.Mod}


class ConstructsMixin:

    _OPS = OPS

    # ---- print-shaped helpers ------------------------------------------------
    def _print_call_idxs(self):
        return self._find(lambda n: isinstance(n, ast.Call)
                          and isinstance(n.func, ast.Name)
                          and n.func.id == "print")

    def _print_calls(self):
        return [self._node(i) for i in self._print_call_idxs()]

    def prints_computed(self, min_calls=1, because=""):
        """Every print() must show a computed value, not a typed-in literal --
        and there must be a print() at all (no sys.stdout.write end-runs).
        min_calls requires that many separate LIVE print() statements, for
        puzzles whose lesson is reuse (one print of a multi-line string, or a
        silenced decoy print, dodges it)."""
        idxs = self._print_call_idxs()
        if not idxs:
            raise LessonNotUsedError("a print() that shows a computed value",
                                   "print() wasn't used", because)
        for c in self._print_calls():
            if not c.args or all(isinstance(a, ast.Constant) for a in c.args):
                raise LessonNotUsedError(
                    "a computed value in print(...)",
                    "the answer typed in as a literal", because)
        self._require_live("%d separate print() calls" % min_calls,
                           "only %d print() call(s)" % len(idxs),
                           idxs, "expr", because, min_count=min_calls)

    def prints_name(self, min_calls=2, same=True, because=""):
        """At least `min_calls` live print() calls that show a VARIABLE.
        With same=True they must all show the same one -- the store-once,
        reuse-many-times pattern."""
        idxs, names = [], {}
        for i in self._print_call_idxs():
            c = self._node(i)
            got = set(n.id for a in c.args for n in ast.walk(a)
                      if isinstance(n, ast.Name))
            if got:
                idxs.append(i)
                names[i] = got
        want = "%d separate print() calls showing a variable" % min_calls
        if len(idxs) < min_calls:
            raise LessonNotUsedError(want, "only %d found" % len(idxs), because)
        live = self._live_filter(idxs, "expr", min_count=len(idxs))
        if len(live) < min_calls:
            raise LessonNotUsedError(want, self.DECORATIVE, because)
        if same:
            counts = {}
            for i in live:
                for n in names[i]:
                    counts[n] = counts.get(n, 0) + 1
            if not any(v >= min_calls for v in counts.values()):
                raise LessonNotUsedError(
                    "the SAME variable printed %d times" % min_calls,
                    "different variables were printed", because)

    def print_uses_keyword(self, kw, because=""):
        """A print() whose `kw=` keyword actually shapes the output --
        dropping the keyword must change what gets printed."""
        found = self._find(lambda n: isinstance(n, ast.Call)
                           and isinstance(n.func, ast.Name)
                           and n.func.id == "print"
                           and any(k.arg == kw for k in n.keywords))
        self._require_live("print(..., %s=...)" % kw, "no %s= used" % kw,
                           found, "kw:" + kw, because)

    def print_has_min_args(self, n, because=""):
        """One print() given n+ separate values that all matter -- trimming
        the extras must change the output (no silent padding values)."""
        found = self._find(lambda c: isinstance(c, ast.Call)
                           and isinstance(c.func, ast.Name)
                           and c.func.id == "print" and len(c.args) >= n)
        self._require_live("one print with %d+ separate values" % n,
                           "too few values passed to a single print",
                           found, "trim", because)

    # ---- "did you use the construct this puzzle teaches?" --------------------
    def _has(self, *types):
        return any(isinstance(n, types) for n in ast.walk(self.tree()))

    def uses_print(self, because=""):
        self._require_live("a print() call", "print() wasn't used",
                           self._print_call_idxs(), "expr", because)

    def uses_if(self, because=""):
        self._require_live("an if statement",
                           "no if was used (a trick avoided it)",
                           self._find(lambda n: isinstance(n, ast.If)),
                           "stmt", because)

    def uses_nested_if(self, because=""):
        """An if nested inside the BODY of another if -- the 'inner check runs
        only when the outer is true' lesson. An elif chain doesn't count: an
        `elif` is AST-identical to `else: if`, so its inner if lives in the
        orelse, not the body. Requires the inner if to be live."""
        def inner(n):
            if not isinstance(n, ast.If):
                return False
            return any(isinstance(p, ast.If) and n in p.body
                       for p in ast.walk(self.tree()))
        self._require_live("an if nested inside another if's body",
                           "no nested if (an elif chain isn't nesting)",
                           self._find(inner), "stmt", because)

    def uses_while(self, because=""):
        self._require_live("a while loop", "no while loop was used",
                           self._find(lambda n: isinstance(n, ast.While)),
                           "stmt", because)

    def uses_for(self, because=""):
        self._require_live("a for loop", "no for loop was used",
                           self._find(lambda n: isinstance(n, ast.For)),
                           "stmt", because)

    def uses_loop(self, because=""):
        self._require_live("a loop (for or while)", "no loop was used",
                           self._find(lambda n: isinstance(n, (ast.For,
                                                               ast.While))),
                           "stmt", because)

    def uses_break(self, because=""):
        self._require_live("break", "break wasn't used",
                           self._find(lambda n: isinstance(n, ast.Break)),
                           "stmt", because)

    def uses_continue(self, because=""):
        self._require_live("continue", "continue wasn't used",
                           self._find(lambda n: isinstance(n, ast.Continue)),
                           "stmt", because)

    def uses_fstring(self, because=""):
        self._require_live("an f-string", "no f-string was used",
                           self._find(lambda n: isinstance(n, ast.JoinedStr)),
                           "expr", because)

    @staticmethod
    def _index_of(sub):
        idx = sub.slice
        if hasattr(ast, "Index") and isinstance(idx, ast.Index):  # py<3.9
            idx = idx.value
        return idx

    def _sub_idxs(self, want_slice):
        """Subscripts being READ (Store-targets can't be ablated)."""
        return self._find(lambda n: isinstance(n, ast.Subscript)
                          and isinstance(n.slice, ast.Slice) == want_slice
                          and isinstance(getattr(n, "ctx", None), ast.Load))

    def uses_index(self, because=""):
        """A plain index s[i] (not a slice)."""
        self._require_live("indexing like s[0]", "no indexing was used",
                           self._sub_idxs(want_slice=False), "expr", because)

    def uses_negative_index(self, because=""):
        """A negative index s[-1] (UnaryOp '-' or a negative literal)."""
        def neg(n):
            if not isinstance(n, ast.Subscript) \
                    or isinstance(n.slice, ast.Slice) \
                    or not isinstance(getattr(n, "ctx", None), ast.Load):
                return False
            idx = self._index_of(n)
            if isinstance(idx, ast.UnaryOp) and isinstance(idx.op, ast.USub):
                return True
            return (isinstance(idx, ast.Constant)
                    and isinstance(idx.value, int) and idx.value < 0)
        self._require_live("a negative index like s[-1]",
                           "no negative index was used",
                           self._find(neg), "expr", because)

    def uses_slice(self, step=False, because=""):
        def ok(n):
            return (isinstance(n, ast.Subscript)
                    and isinstance(n.slice, ast.Slice)
                    and isinstance(getattr(n, "ctx", None), ast.Load)
                    and (not step or n.slice.step is not None))
        what = "a slice with a step (s[::-1])" if step else "a slice (s[a:b])"
        self._require_live(what, "no such slice was used",
                           self._find(ok), "expr", because)

    def uses_call(self, name, because=""):
        """A call to a function or method `name` (e.g. append, split, items)."""
        def ok(n):
            if not isinstance(n, ast.Call):
                return False
            f = n.func
            return ((isinstance(f, ast.Attribute) and f.attr == name)
                    or (isinstance(f, ast.Name) and f.id == name))
        self._require_live("a call to %s()" % name,
                           "%s() wasn't used" % name,
                           self._find(ok), "expr", because)

    # ---- higher-order-function checks (anchor the call to the INPUT) ---------
    # The bare uses_call(name) is satisfied by ANY live call to name -- even a
    # decorative one wrapped around a precomputed answer (map(lambda v: v,
    # [x * x for x in nums]) reads the squares off a comprehension, so map does
    # nothing). These pin the HOF to its lesson role: it must work over the
    # function's input, or carry the lesson's lambda in the right slot.
    _REPACKAGING = (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp,
                    ast.List, ast.Tuple, ast.Set, ast.Dict)

    def _param_names(self):
        """Every def/lambda's parameter names -- the inputs a HOF should
        consume."""
        names = set()
        for f in ast.walk(self.tree()):
            if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef)):
                a = f.args
                for grp in (a.posonlyargs, a.args, a.kwonlyargs):
                    names.update(x.arg for x in grp)
        return names

    @staticmethod
    def _call_named(n, name):
        return (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                and n.func.id == name)

    def _refs_param(self, node, params):
        return any(isinstance(x, ast.Name) and x.id in params
                   for x in ast.walk(node))

    def uses_call_over_param(self, name, because=""):
        """A live call to `name` whose iterable argument IS the function's input
        -- the parameter, or an expression derived from it (list(nums),
        reversed(nums)) -- and NOT a comprehension or display literal that
        already did the lesson's work. Closes the 'wrap a comprehension in a
        live HOF' dodge for map/filter/reduce: the HOF must do the transform /
        selection / fold over the input itself."""
        params = self._param_names()

        def ok(n):
            if not self._call_named(n, name):
                return False
            return any(not isinstance(a, self._REPACKAGING)
                       and self._refs_param(a, params) for a in n.args)

        self._require_live(
            "%s(...) applied to the input itself" % name,
            "%s must work over the input, not wrap a comprehension or literal "
            "that already computed the answer" % name,
            self._find(ok), "expr", because)

    def uses_call_on_collection(self, name, because=""):
        """A live call to `name` whose argument is a real collection -- a
        variable, a comprehension, or a derived call -- NOT a freshly built
        display literal holding a precomputed answer. Closes the wrapper dodge
        sum([total]) / min([lo]) / max([hi]), where an accumulator loop did the
        work and the builtin is a live no-op around a one-element list. Unlike
        uses_call_over_param this needs no parameter, so it fits script-mode
        puzzles (the input arrives on stdin, not as an argument)."""
        displays = (ast.List, ast.Tuple, ast.Set, ast.Dict)

        def ok(n):
            return (self._call_named(n, name) and n.args
                    and not isinstance(n.args[0], displays))

        self._require_live(
            "%s(...) over a real collection" % name,
            "%s must run over the input collection, not a literal holding an "
            "answer a loop already computed" % name,
            self._find(ok), "expr", because)

    def uses_predicate_over_param(self, name, because=""):
        """A live call to `name` (any/all) fed a comprehension/generator
        expression that iterates the function's input -- the taught
        any(<test> for <item> in nums) pattern. Rejects any([flag]) and
        any(flag for _ in [0]): neither iterates the input, so the answer came
        from a loop-with-a-flag, not from any/all over the items."""
        params = self._param_names()
        comps = (ast.GeneratorExp, ast.ListComp, ast.SetComp)

        def ok(n):
            if not (self._call_named(n, name) and n.args):
                return False
            a = n.args[0]
            return (isinstance(a, comps) and a.generators
                    and self._refs_param(a.generators[0].iter, params))

        self._require_live(
            "%s(<test> for <item> in input)" % name,
            "hand the per-item tests to %s() as a comprehension over the input, "
            "not a flag a loop precomputed" % name,
            self._find(ok), "expr", because)

    def uses_lambda_arg(self, name, keyword=None, pos=0, because=""):
        """A live call to `name` carrying a lambda in a specific slot -- the
        sort key (keyword="key"), the filter predicate or map function (pos=0).
        Anchors the lambda to its role, so a decoy lambda elsewhere (which
        satisfies the bare uses_lambda) plus a named function in the slot no
        longer passes."""
        slot = "key=" if keyword else "argument %d" % pos

        def ok(n):
            if not self._call_named(n, name):
                return False
            if keyword is not None:
                return any(k.arg == keyword and isinstance(k.value, ast.Lambda)
                           for k in n.keywords)
            return len(n.args) > pos and isinstance(n.args[pos], ast.Lambda)

        self._require_live(
            "a lambda as the %s of %s(...)" % (slot, name),
            "the %s of %s must be an inline lambda, not a named function with a "
            "decoy lambda elsewhere" % (slot, name),
            self._find(ok), "expr", because)

    def uses_dict(self, because=""):
        """A dict literal {...} or dict()."""
        def ok(n):
            return isinstance(n, ast.Dict) or (
                isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                and n.func.id == "dict")
        self._require_live("a dict ({} or dict())", "no dict was used",
                           self._find(ok), "container", because)

    def uses_set(self, because=""):
        """A set literal {a, b} or set()."""
        def ok(n):
            return isinstance(n, ast.Set) or (
                isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                and n.func.id == "set")
        self._require_live("a set ({...} or set())", "no set was used",
                           self._find(ok), "container", because)

    def uses_try(self, because=""):
        """A try/except statement -- for puzzles whose lesson IS handling the
        error (an if-guard would behave the same but dodge the concept)."""
        self._require_live("a try/except block", "no try/except was used",
                           self._find(lambda n: isinstance(n, ast.Try)),
                           "stmt", because)

    def uses_raise(self, because=""):
        """A raise statement."""
        self._require_live("a raise statement", "raise wasn't used",
                           self._find(lambda n: isinstance(n, ast.Raise)),
                           "stmt", because)

    def uses_in(self, because=""):
        """The membership operator: `x in s` or `x not in s` in a condition."""
        def ok(n):
            return isinstance(n, ast.Compare) and any(
                isinstance(op, (ast.In, ast.NotIn)) for op in n.ops)
        self._require_live("the `in` operator", "`in` wasn't used",
                           self._find(ok), "bool", because)

    def uses_boolop(self, op=None, because=""):
        """A boolean operator: `and` / `or` -- for puzzles whose lesson is
        COMBINING conditions, where a single arithmetic trick (n % 6 == 0 for
        `divisible by 2 and 3`) would behave the same but dodge the concept.
        `op` pins one operator; left None, either counts (so an `or`+`not`
        De Morgan rewrite of an `and` still passes)."""
        names = {"and": ast.And, "or": ast.Or}
        def ok(n):
            return isinstance(n, ast.BoolOp) and (
                op is None or isinstance(n.op, names[op]))
        what = ("the `%s` operator" % op if op
                else "a boolean operator (and / or)")
        self._require_live(what, "%s wasn't used" % (op or "and / or"),
                           self._find(ok), "bool", because)

    def uses_comprehension(self, with_if=False, because=""):
        """A comprehension (list/set/dict or generator expression). Pass
        with_if=True to require a filtering `if` clause inside it."""
        def ok(n):
            if not isinstance(n, (ast.ListComp, ast.SetComp, ast.DictComp,
                                  ast.GeneratorExp)):
                return False
            return not with_if or any(g.ifs for g in n.generators)
        if with_if:
            what = "a comprehension with an if  ([x for x in ... if ...])"
        else:
            what = "a comprehension like [x for x in ...]"
        self._require_live(what, "no comprehension was used",
                           self._find(ok), "expr", because)

    # ---- construct checks staged for the upcoming chapters -------------------
    def uses_with(self, because=""):
        """A with statement (any context manager). For the files chapter use
        uses_with_open: this plain check is satisfied by ANY live with -- even a
        `with io.StringIO() as s:` wrapping a print -- so it does NOT prove the
        FILE was opened with a with (the file could still be read/written bare).
        """
        self._require_live("a with statement (with ... as ...:)",
                           "no with statement was used",
                           self._find(lambda n: isinstance(n, ast.With)),
                           "stmt", because)

    def uses_with_open(self, because=""):
        """A `with open(...) as f:` -- the file itself must be opened by a with
        block. The with's context expression has to be an open() call, so an
        unrelated `with io.StringIO()` (which satisfies the generic uses_with)
        won't pass while the file is opened bare. Still liveness-checked: a dead
        `with open(...) as f: pass` decoy doesn't count, so the with-open must
        be the one actually doing the file I/O the output depends on."""
        def ok(n):
            if not isinstance(n, ast.With):
                return False
            return any(isinstance(it.context_expr, ast.Call)
                       and isinstance(it.context_expr.func, ast.Name)
                       and it.context_expr.func.id == "open"
                       for it in n.items)
        self._require_live("a `with open(...) as f:` block",
                           "the file wasn't opened with a with statement "
                           "(a with on something other than open() doesn't "
                           "count)",
                           self._find(ok), "stmt", because)

    def uses_import(self, module=None, because=""):
        """An import -- optionally of one specific module."""
        def ok(n):
            if isinstance(n, ast.Import):
                return module is None or any(
                    a.name == module or a.name.startswith(module + ".")
                    for a in n.names)
            if isinstance(n, ast.ImportFrom):
                if module is None:
                    return True
                mod = n.module or ""
                return mod == module or mod.startswith(module + ".")
            return False
        what = ("an import of %s" % module) if module else "an import statement"
        self._require_live(what, "no such import was found",
                           self._find(ok), "stmt", because)

    def uses_class(self, name=None, because=""):
        """A class definition; with `name`, specifically `class <name>:`.

        Object puzzles can't use liveness (make/method aren't on the tape), so
        this degrades to an AST presence check -- which a decoy `class X: pass`
        beside a namedtuple/type()/function would satisfy. Passing the name the
        tests instantiate ties the check to that symbol, so the lesson's class
        must really be written with `class`."""
        def ok(n):
            return isinstance(n, ast.ClassDef) and (name is None
                                                    or n.name == name)
        what = ("a class named %s (class %s:)" % (name, name) if name
                else "a class definition (class Name:)")
        self._require_live(what, "no such class was defined",
                           self._find(ok), "stmt", because)

    # The comprehension forms that are "a generator expression in disguise":
    # `yield from (g for g in ...)` (or a list/set/dict comp) just re-emits a
    # comprehension the briefs forbid, so it must NOT satisfy uses_yield(name).
    _COMPREHENSIONS = (ast.GeneratorExp, ast.ListComp, ast.SetComp, ast.DictComp)

    @classmethod
    def _yields_directly(cls, fnode):
        """True if `fnode`'s OWN body contains a real yield / yield from -- not
        one buried in a nested def/lambda (a different scope), and not a generator
        expression (its own scope, no ast.Yield at all). A `yield from` that only
        delegates to a comprehension/generator expression does NOT count: that is
        the forbidden genexpr wrapped in `yield from`, not the function producing
        the stream itself (cf. each Ch10 dodges.py)."""
        stack = list(ast.iter_child_nodes(fnode))
        while stack:
            node = stack.pop()
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef,
                                 ast.Lambda)):
                continue                 # a different scope -- not fnode's yields
            if isinstance(node, ast.Yield):
                return True
            if isinstance(node, ast.YieldFrom):
                if not isinstance(node.value, cls._COMPREHENSIONS):
                    return True
                continue                 # disguised genexpr -- not the lesson
            stack.extend(ast.iter_child_nodes(node))
        return False

    def uses_yield(self, name=None, because=""):
        """yield / yield from (the generators chapter). AST-only: substituting
        a yield flips the function's generator-ness, which crashes callers and
        would make a LEGIT yield look dead under the clean-run rule.

        Bare `uses_yield()` asks only that SOME function yields. Because that is
        file-level, a genexpr-returning solution (which still passes
        is_generator) can satisfy it with a decoy yield parked in an unrelated
        function. So for a generator puzzle, pin yield to the lesson's role:
        `uses_yield("fn")` requires `fn`'s OWN body to yield -- a genexpr or a
        yield stashed elsewhere no longer counts (mirrors uses_class(name) /
        uses_default_param(name)). A `yield from` over a comprehension/generator
        expression also no longer counts: that is the forbidden genexpr in
        disguise, not `fn` producing the stream itself."""
        if name is None:
            if not self._has(ast.Yield, ast.YieldFrom):
                raise LessonNotUsedError("a yield statement",
                                       "yield wasn't used", because)
            return
        defs = [n for n in ast.walk(self.tree())
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                and n.name == name]
        if not any(self._yields_directly(d) for d in defs):
            raise LessonNotUsedError(
                "a yield inside %s itself" % name,
                "%s reaches its result without yield in its own body (a "
                "generator expression, or a yield parked in another function, "
                "isn't the lesson)" % name, because)

    def uses_lambda(self, because=""):
        """A lambda expression. AST-only: a lambda's sentinel stand-in is not
        callable, so every ablation crashes and liveness can't judge it."""
        if not self._has(ast.Lambda):
            raise LessonNotUsedError("a lambda expression",
                                   "no lambda was used", because)

    def uses_default_param(self, name=None, because=""):
        """A function defined with a default-valued parameter: def f(x, y=...).
        AST-only (like uses_lambda): ablating a default is awkward, and a real
        default may go unexercised on the calls that supply it. `name` pins one
        function. Defeats reaching the same behavior with *args/**kwargs."""
        def ok(n):
            if not isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                return False
            if name is not None and n.name != name:
                return False
            a = n.args
            return bool(a.defaults) or any(d is not None for d in a.kw_defaults)
        if not any(ok(n) for n in ast.walk(self.tree())):
            raise LessonNotUsedError(
                "a default parameter (def %s(..., x=value))" % (name or "f"),
                "no default-valued parameter was defined", because)

    def uses_unpacking(self, because=""):
        """Tuple/list unpacking, e.g. a, b = b, a  or  for a, b in pairs."""
        def ok(n):
            if isinstance(n, ast.Assign):
                return any(isinstance(t, (ast.Tuple, ast.List))
                           for t in n.targets)
            return isinstance(n, ast.For) and isinstance(n.target,
                                                         (ast.Tuple, ast.List))
        self._require_live("unpacking (a, b = ...)", "no unpacking was used",
                           self._find(ok), "stmt", because)

    # ---- assignments ----------------------------------------------------------
    def assigns_a_variable(self, value=None, because=""):
        """A live variable assignment; with `value`, one that stores that
        exact literal (type-strict: 42 is not \"42\")."""
        def ok(n):
            if not isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                return False
            if value is None:
                return True
            v = getattr(n, "value", None)
            return (isinstance(n, ast.Assign) and isinstance(v, ast.Constant)
                    and type(v.value) is type(value) and v.value == value)
        what = ("a variable storing %r" % (value,) if value is not None
                else "a variable assignment")
        self._require_live(what, "no variable used",
                           self._find(ok), "stmt", because)

    def reassigns_a_variable(self, values=None, because=""):
        """The same variable assigned twice, where the REASSIGNMENT is live
        (removing it must change the output). With `values`, the first
        assignments must store exactly those literals, in order."""
        seq = {}
        for i, n in enumerate(ast.walk(self.tree())):
            if isinstance(n, ast.Assign):
                for t in n.targets:
                    if isinstance(t, ast.Name):
                        seq.setdefault(t.id, []).append((n.lineno, i, n))
            elif (isinstance(n, ast.AugAssign)
                  and isinstance(n.target, ast.Name)):
                seq.setdefault(n.target.id, []).append((n.lineno, i, n))
        candidates = []
        for name in seq:
            assigns = sorted(seq[name], key=lambda t: t[:2])
            if len(assigns) < 2:
                continue
            if values is not None:
                if len(assigns) < len(values):
                    continue
                bad = False
                for (_, _, node), want in zip(assigns, values):
                    v = getattr(node, "value", None)
                    if not (isinstance(node, ast.Assign)
                            and isinstance(v, ast.Constant)
                            and type(v.value) is type(want)
                            and v.value == want):
                        bad = True
                        break
                if bad:
                    continue
            candidates.append(assigns[1][1])     # the reassignment statement
        what = "the same variable assigned twice"
        if values is not None:
            what += " (%s)" % " then ".join(repr(v) for v in values)
        self._require_live(what, "no single variable was reassigned",
                           candidates, "stmt", because)

    def uses_op(self, op, min_count=1, because=""):
        """Require the solution to actually compute with operator `op`.

        Counts live uses of that arithmetic operator. Defeats typing the
        answer (`print(14)`), stashing it in a variable first
        (`x = 14; print(x)`), and parking the operator in code that never
        affects the output (`q = 1 * 1`)."""
        opcls = OPS[op]
        found = self._find(lambda n: isinstance(n, ast.BinOp)
                           and isinstance(n.op, opcls))
        want = ("'%s' at least %d times" % (op, min_count)
                if min_count > 1 else "the '%s' operation" % op)
        self._require_live(want, "it wasn't used", found, "expr", because,
                           min_count=min_count)
