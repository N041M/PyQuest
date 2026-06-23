"""Profile portability: export a profile to a single portable JSON file, and
import one back. A profile is fully described by its progress.json +
answers.json (work.py is transient scratch, reseeded on demand), so export
bundles those two and import validates such a bundle back into a profile.

Import sanitizes against the *current* content -- it drops unknown puzzle ids
and recomputes the high-water mark -- so a stale or hand-edited bundle can
never unlock puzzles that don't exist or corrupt the gating. Composes state +
settings + render, like the other command modules.
"""

import os
import json

from ..config import now, write_json, ROOT, MODES, rel, set_setting
from ..state import (current_puzzle, archive_current, default_progress,
                     ensure_workspace, answers_path, progress_path, work_path,
                     list_users, current_user, ensure_user, valid_username)
from ..render import paint, cli, PAD, OK, NO, ARROW
from ..i18n import t, tp

EXPORT_FORMAT = "pyquest-progress"
EXPORT_VERSION = 1


def _bundle_summary(n_done, n_answers):
    """The shared 'N puzzles completed, M saved answers.' line. Each count is
    pluralized on its own (Czech and most languages decline the two nouns
    independently), then joined by a localizable template."""
    done_txt = tp("transfer.puzzles", n_done,
                  one="%d puzzle completed",
                  other="%d puzzles completed") % n_done
    ans_txt = tp("transfer.answers", n_answers,
                 one="%d saved answer",
                 other="%d saved answers") % n_answers
    return "  " + t("transfer.summary", "%s, %s.") % (done_txt, ans_txt)


# ---- export ---------------------------------------------------------------
def _export_dest(arg, user):
    """Resolve where to write. Default: pyquest-<user>-<date>.json at the repo
    root. An arg names a file, or a directory to drop the default name into."""
    name = "pyquest-%s-%s.json" % (user, now()[:10])
    if not arg:
        return os.path.join(ROOT, name)
    if os.path.isdir(arg) or arg.endswith(os.sep):
        return os.path.join(arg, name)
    return arg if arg.endswith(".json") else arg + ".json"


def cmd_export(puzzles, by_id, prog, arg=None):
    """Write this profile's progress + saved answers to a portable JSON file."""
    user = current_user()
    # capture the current draft so the export reflects the latest work
    answers = archive_current(prog, by_id, puzzles)
    bundle = {
        "format": EXPORT_FORMAT,
        "format_version": EXPORT_VERSION,
        "exported_at": now(),
        "user": user,
        "progress": prog,
        "answers": answers,
    }
    dest = _export_dest(arg, user)
    try:
        os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
        write_json(dest, bundle)
    except OSError as e:
        print(paint("  %s " % NO + t("transfer.write_fail",
                    "Couldn't write %s (%s).") % (dest, e.strerror), "red"))
        return
    where = rel(dest) if os.path.abspath(dest).startswith(ROOT) else dest
    print(paint("  %s " % OK + t("transfer.exported",
                "Exported profile '%s' to %s.") % (user, where),
                "green", "bold"))
    print(_bundle_summary(len(prog.get("completed", [])), len(answers)))
    print("  " + t("transfer.move_hint", "Move it to another machine, then:  %s")
          % cli("import " + where))


# ---- import ---------------------------------------------------------------
def _sanitize_progress(raw, by_id, puzzles):
    """Rebuild a trustworthy progress dict from imported (possibly stale or
    edited) data: drop unknown puzzle ids and recompute the high-water mark so
    gating always matches the content actually installed here."""
    raw = raw if isinstance(raw, dict) else {}
    out = default_progress(puzzles)
    mode = raw.get("mode")
    out["mode"] = mode if mode in MODES else "normal"
    seen, completed = set(), []
    for pid in raw.get("completed", []) or []:
        if pid in by_id and pid not in seen:
            seen.add(pid)
            completed.append(pid)
    out["completed"] = completed
    stats = {}
    for pid, s in (raw.get("stats") or {}).items():
        if pid in by_id and isinstance(s, dict):
            entry = {"attempts": int(s.get("attempts", 0) or 0),
                     "hints_used": int(s.get("hints_used", 0) or 0)}
            solved_on = s.get("solved_on")
            if isinstance(solved_on, str):       # keep the first-solve date
                entry["solved_on"] = solved_on
            stats[pid] = entry
    out["stats"] = stats
    cur = raw.get("current")
    out["current"] = cur if cur in by_id else (puzzles[0]["id"] if puzzles
                                               else None)
    # recompute, never trust an imported index: it gates forward jumps. The
    # learner is entitled to be at least as far as their furthest completed
    # puzzle and the one they're currently sitting on.
    reached = [by_id[pid]["index"] for pid in completed]
    if out["current"] in by_id:
        reached.append(by_id[out["current"]]["index"])
    out["highest"] = max(reached, default=0)
    out["active"] = bool(raw.get("active")) or bool(completed)
    created = raw.get("created_at")
    out["created_at"] = created if isinstance(created, str) else now()
    dropped = len(raw.get("completed", []) or []) - len(completed)
    return out, dropped


def _sanitize_answers(raw, by_id):
    out = {}
    for pid, entry in (raw if isinstance(raw, dict) else {}).items():
        if pid in by_id and isinstance(entry, dict):
            clean = {"solved": bool(entry.get("solved")),
                     "code": str(entry.get("code", ""))}
            note = entry.get("note")
            if isinstance(note, str) and note:       # carry the learner's note
                clean["note"] = note
            out[pid] = clean
    return out


def cmd_import(puzzles, by_id, prog, path=None, opt1=None, opt2=None):
    """Load a bundle written by `export` into a profile, then switch to it.

    Usage: import <file> [name] [force]
      name   target profile (default: the name stored in the file)
      force  overwrite an existing profile (otherwise import refuses)
    """
    if not path:
        print(PAD + paint(t("ui.usage", "usage:  ")
                          + cli("import <file> [name] [force]"), "yellow"))
        print(PAD + t("transfer.import_usage_hint",
              "Imports a profile exported with  %s.") % cli("export"))
        return prog
    # parse the optional [name] [force] tail in either order
    force = "force" in (opt1, opt2)
    target = next((o for o in (opt1, opt2) if o and o != "force"), None)

    if not os.path.isfile(path):
        print(paint("  %s " % NO + t("transfer.no_file", "No such file: %s")
                    % path, "red"))
        return prog
    try:
        with open(path) as f:
            bundle = json.load(f)
    except (OSError, ValueError):
        print(paint("  %s " % NO + t("transfer.read_fail",
                    "Couldn't read %s as a PyQuest export.") % path, "red"))
        return prog
    if not isinstance(bundle, dict) or bundle.get("format") != EXPORT_FORMAT:
        print(paint("  %s " % NO + t("transfer.not_export",
                    "%s isn't a PyQuest export file.") % path, "red"))
        return prog

    name = target or bundle.get("user") or "default"
    if not valid_username(name):
        print(PAD + paint(t("user.invalid_name", "'%s' can't be a profile name.")
                          % name, "yellow"))
        print(PAD + t("transfer.pass_name", "Pass a valid name:  %s")
              % cli("import %s <name>" % path))
        return prog
    if name in list_users() and not force:
        print(paint("  %s " % NO + t("user.exists", "Profile '%s' already "
                    "exists.") % name, "yellow"))
        print(PAD + t("transfer.exists_hint",
              "Import under a new name, or overwrite it:"))
        print(PAD + "  %s" % cli("import %s <other-name>" % path))
        print(PAD + "  %s" % cli("import %s %s force" % (path, name)))
        return prog

    newprog, dropped = _sanitize_progress(bundle.get("progress"), by_id, puzzles)
    answers = _sanitize_answers(bundle.get("answers"), by_id)

    archive_current(prog, by_id, puzzles)        # save the leaving profile's draft
    ensure_user(name)
    write_json(progress_path(name), newprog)
    write_json(answers_path(name), answers)
    set_setting("user", name)

    # reseed the shared workspace from the freshly imported profile
    wp = work_path()
    if os.path.exists(wp):
        os.remove(wp)
    ensure_workspace(current_puzzle(newprog, by_id, puzzles), answers,
                     newprog.get("active"))

    print(paint("  %s " % ARROW + t("transfer.imported",
                "Imported into profile '%s' (now active).") % name,
                "cyan", "bold"))
    print(_bundle_summary(len(newprog["completed"]), len(answers)))
    if dropped:
        print(PAD + paint(
            tp("transfer.dropped", dropped,
               one="note: %d completed id isn't in this version's content and "
                   "was dropped.",
               other="note: %d completed id(s) aren't in this version's content "
                     "and were dropped.") % dropped, "gray"))
    return newprog
