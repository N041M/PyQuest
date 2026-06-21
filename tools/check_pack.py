"""Validate a community language pack before shipping it.

    python3 tools/check_pack.py            check every pack under lang/
    python3 tools/check_pack.py <code>     check just lang/<code>/

It runs the same load check the engine does on select (pack.json + strings.json
via engine.i18n.validate), then audits the optional content overrides under
lang/<code>/chapters/: every file there must mirror a real, translatable file
under chapters/. This catches the silent failure mode -- a mistyped folder or
filename that the engine simply never looks for, so the translation appears to
do nothing with no error. Exits non-zero if any pack has a problem.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from engine import i18n
from engine.config import CHAPTERS_DIR
from engine.content import LOCALIZED_CONTENT

LANG_DIR = i18n.LANG_DIR


def _content_issues(code):
    """Audit lang/<code>/chapters/: return (overrides_ok, problems). Each problem
    is (pack_relative_path, reason). An override is valid when the same relative
    path exists under chapters/ AND its filename is one the engine localizes."""
    base = os.path.join(LANG_DIR, code, "chapters")
    ok, problems = [], []
    if not os.path.isdir(base):
        return ok, problems                       # no content overrides -- fine
    for dirpath, _dirs, files in os.walk(base):
        for name in files:
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, base)     # e.g. 02_strings/01_x/brief.md
            shown = os.path.join("lang", code, "chapters", rel)
            real = os.path.join(CHAPTERS_DIR, rel)
            if name not in LOCALIZED_CONTENT:
                problems.append((shown, "%s is not a translatable file (%s)"
                                 % (name, ", ".join(LOCALIZED_CONTENT))))
            elif not os.path.isfile(real):
                problems.append((shown, "no puzzle file at chapters/%s -- check "
                                 "the path" % rel))
            else:
                ok.append(shown)
    return ok, problems


def check(code):
    """Validate one pack. Returns True when clean, printing a report either way."""
    load_ok, info = i18n.validate(code)
    print("Pack '%s'%s" % (code, "" if not load_ok else " (%s)" % info))
    if not load_ok:
        print("  load: FAIL -- %s" % info)
        return False
    print("  load: ok (pack.json, strings.json)")

    strings = i18n._load_json(os.path.join(LANG_DIR, code, "strings.json"))
    if isinstance(strings, dict):
        print("  strings.json: %d key(s) translated" % len(strings))

    ok, problems = _content_issues(code)
    if not ok and not problems:
        print("  content overrides: none")
    else:
        print("  content overrides: %d valid, %d problem(s)"
              % (len(ok), len(problems)))
    for path in sorted(ok):
        print("    + %s" % path)
    for path, reason in sorted(problems):
        print("    ! %s" % path)
        print("        %s" % reason)
    return not problems


def main(argv):
    if argv:
        codes = argv                              # explicit: check even _template
    else:
        codes = sorted(c for c in os.listdir(LANG_DIR)
                       if os.path.isdir(os.path.join(LANG_DIR, c))
                       and not i18n.is_scaffolding(c)) \
            if os.path.isdir(LANG_DIR) else []
        if not codes:
            print("No packs under lang/ -- nothing to check. (English is "
                  "built in, not a pack.)")
            return 0

    results = [check(c) for c in codes]
    print("")
    bad = results.count(False)
    if bad:
        print("%d of %d pack(s) have problems." % (bad, len(results)))
        return 1
    print("All %d pack(s) OK." % len(results))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
