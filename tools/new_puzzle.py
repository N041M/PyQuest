"""Scaffold a new puzzle folder -- the six required files (plus reference.md /
dodges.py where they apply), filled with TODO templates in the house style.

    python3 tools/new_puzzle.py chapters/17_closures/01_scope \\
        --id 17.1 --title "Local vs global scope" --concept "names resolve ..."

    python3 tools/new_puzzle.py chapters/16_project_cart/05_thing \\
        --id 16.5 --title "..." --kind build        # a project step

A lesson puzzle gets `concept`/`why` + a reference.md; a project puzzle gets a
`kind` and omits both. The scaffold is a STARTING POINT: it will not pass the
audit until you fill it in (that is the point). After filling it, run
`python3 tools/audit.py --sidestep`. See docs/CONTRIBUTING.md for the workflow.
"""

import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED = ("brief.md", "starter.py", "tests.py", "hints.md", "solution.py",
            "meta.json")


def _chapter_display(chapter_dir):
    """The chapter's display name: borrow a sibling puzzle's `chapter`, else
    humanize the folder name (06_functions -> Functions)."""
    if os.path.isdir(chapter_dir):
        for pz in sorted(os.listdir(chapter_dir)):
            meta = os.path.join(chapter_dir, pz, "meta.json")
            if os.path.isfile(meta):
                try:
                    name = json.load(open(meta, encoding="utf-8")).get("chapter")
                except (ValueError, OSError):
                    name = None
                if name:
                    return name
    base = os.path.basename(chapter_dir.rstrip(os.sep))
    return base.split("_", 1)[-1].replace("_", " ").title()


def _brief(pid, title, kind):
    if kind:
        return ("# %s -- %s\n\n"
                "TODO: a short step brief (sparser than a lesson). State what to\n"
                "build and what \"done\" looks like.\n\n"
                "## Done when\n\n- TODO: an observable outcome.\n"
                "- TODO: an edge case.\n" % (pid, title))
    return ("# %s -- %s\n\n"
            "## Concept\n\nTODO: explain the idea from scratch.\n\n"
            "## Example\n\n```python\nTODO\n```\n\n"
            "## Your task\n\nTODO: state the task.\n\n"
            "## Done when\n\n- TODO: an observable outcome.\n"
            "- TODO: an edge case (empty / zero / negative / absent).\n"
            % (pid, title))


def _tests(kind):
    head = "from engine.inputs import random_int  # adjust to what you need\n\n\n"
    body = (
        "def check(T):\n"
        "    # 1. Behaviour first -- randomize inputs, cover an edge case:\n"
        "    #    T.eq(T.call(\"fn\", ...), expected, because=\"...\")\n"
        "    #    (script mode: T.eq(T.run(stdin=...), \"...\"))\n")
    if not kind:
        body += (
            "    # 2. Then pin the lesson with the NARROWEST construct check:\n"
            "    #    T.uses_call(\"...\", because=\"...\")  /  T.uses_* / line_*\n")
    body += ("    raise NotImplementedError(\"fill in tests.py, then delete this\")\n")
    return head + body


def _hints():
    return ("TODO hint 1 -- a gentle nudge.\n\n---\n\n"
            "TODO hint 2 -- more specific.\n\n---\n\n"
            "TODO hint 3 -- almost the answer.\n")


def _starter(kind):
    if kind == "debug":
        return ("# This starter ships BROKEN code the learner fixes.\n"
                "# The audit REQUIRES it to FAIL tests.py -- put a real bug here.\n")
    return "# Your code goes here.\n"


def _dodges():
    return ("# Known sidesteps that must FAIL this puzzle's tests, forever\n"
            "# (see tools/audit.py). When --sidestep (or a hand attack) finds an\n"
            "# impostor that passes, tighten the check and pin the exact dodge:\n"
            "DODGES = [\n"
            "    # (\"what the dodge does\", \"the dodge's source\\n\"),\n"
            "]\n")


def scaffold(target_dir, pid, title, mode="import", concept=None, why=None,
             kind=None):
    """Create the puzzle folder and its files. Returns the created paths.
    Raises FileExistsError if the folder already exists (never clobbers)."""
    if os.path.exists(target_dir):
        raise FileExistsError(target_dir)
    chapter = _chapter_display(os.path.dirname(target_dir.rstrip(os.sep)))
    meta = {"id": pid, "title": title, "chapter": chapter, "mode": mode}
    if kind:
        meta["kind"] = kind
    elif concept:
        meta["concept"] = concept
        meta["why"] = why or "TODO: why this matters."

    files = {
        "brief.md": _brief(pid, title, kind),
        "starter.py": _starter(kind),
        "tests.py": _tests(kind),
        "hints.md": _hints(),
        "solution.py": "# TODO: the reference solution; it must pass tests.py.\n",
        "meta.json": json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
        "dodges.py": _dodges(),
    }
    if not kind:                                   # a concept puzzle needs a
        files["reference.md"] = ("# %s\n\nTODO: the textbook entry -- the "
                                 "technical reference for this concept.\n" % title)

    os.makedirs(target_dir)
    created = []
    for name, content in files.items():
        path = os.path.join(target_dir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        created.append(path)
    return created


def main(argv):
    ap = argparse.ArgumentParser(description="Scaffold a new PyQuest puzzle.")
    ap.add_argument("target", help="chapters/NN_chapter/MM_slug")
    ap.add_argument("--id", required=True, help="puzzle id, e.g. 17.1")
    ap.add_argument("--title", required=True)
    ap.add_argument("--mode", choices=("import", "script"), default="import")
    ap.add_argument("--concept", help="lesson puzzles: what it teaches")
    ap.add_argument("--why", help="lesson puzzles: why it matters")
    ap.add_argument("--kind", choices=("build", "debug", "capstone"),
                    help="project puzzles (omits concept/why)")
    args = ap.parse_args(argv)
    try:
        created = scaffold(args.target, getattr(args, "id"), args.title,
                           mode=args.mode, concept=args.concept, why=args.why,
                           kind=args.kind)
    except FileExistsError as e:
        print("refusing to overwrite existing folder: %s" % e)
        return 1
    rel = os.path.relpath(args.target, ROOT)
    print("scaffolded %s (%d files)" % (rel, len(created)))
    print("  fill in the TODOs, then: python3 tools/audit.py --sidestep")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
