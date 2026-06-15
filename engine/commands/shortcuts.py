"""The shell-shortcuts installer: the only part of the engine that edits the
user's environment (a single source line in ~/.zshrc or ~/.bashrc, picking the
file that matches $SHELL). It never
makes surprise edits -- `setup` offers both ways, `setup persist` opts in,
`uninstall` removes the line. Self-contained: config + render only.
"""

import os
import sys

from ..config import ROOT
from ..render import paint, wordmark, header, PAD, OK, NO


def _shortcuts_paths():
    home = os.path.expanduser("~")
    shell = os.environ.get("SHELL", "")
    if shell.endswith("bash"):
        return os.path.join(ROOT, "shell", "pyquest.bash"), \
            os.path.join(home, ".bashrc")
    return os.path.join(ROOT, "shell", "pyquest.zsh"), \
        os.path.join(home, ".zshrc")


def _shortcuts_label():
    """The shortcut file as a repo-relative path, e.g. shell/pyquest.bash."""
    shortcuts, _ = _shortcuts_paths()
    return os.path.join("shell", os.path.basename(shortcuts))


def _local_source_cmd():
    shortcuts, _ = _shortcuts_paths()
    return 'source "%s"' % shortcuts


def _is_persistent():
    shortcuts, rc = _shortcuts_paths()
    if not os.path.isfile(rc):
        return False
    with open(rc) as f:
        return shortcuts in f.read()


def _install_persistent():
    shortcuts, rc = _shortcuts_paths()
    if not os.path.isfile(shortcuts):
        return "nofile", rc
    if _is_persistent():
        return "installed", rc
    with open(rc, "a") as f:
        f.write('\n# PyQuest shell shortcuts\n'
                '[ -f "%s" ] && source "%s"\n' % (shortcuts, shortcuts))
    return "added", rc


def _uninstall_persistent():
    shortcuts, rc = _shortcuts_paths()
    if not os.path.isfile(rc):
        return False, rc
    with open(rc) as f:
        lines = f.readlines()
    kept, removed = [], False
    for ln in lines:
        if ln.strip() == "# PyQuest shell shortcuts" or (
                "source" in ln and shortcuts in ln):
            removed = True
            continue
        kept.append(ln)
    if removed:
        with open(rc, "w") as f:
            f.writelines(kept)
    return removed, rc


def _disclaimer():
    print(PAD + paint("Shortcuts let you type  ", "gray")
          + paint("check", "green", "bold")
          + paint("  instead of  python3 play.py check.", "gray"))
    print(PAD + paint("They are shell functions defined in %s "
                      "(check, hint, start, …)." % _shortcuts_label(), "gray"))
    print(PAD + paint("Local = nothing outside this folder changes.  "
                      "Persistent = one line in your shell startup file.",
                      "gray"))


def cmd_setup():
    """Offer both ways to enable the short commands (no surprise edits)."""
    shortcuts, rc = _shortcuts_paths()
    pyver = "Python %d.%d.%d" % sys.version_info[:3]
    print(wordmark("cyan"))
    print("")
    print(header("setup", "cyan"))
    print("")
    print(PAD + paint("python", "cyan", "bold") + "    "
          + paint(pyver, "white", "bold"))
    print(PAD + paint("status", "cyan", "bold") + "    "
          + (paint(OK + " persistent shortcuts enabled in " + rc, "green")
             if _is_persistent()
             else paint("shortcuts not persistently installed", "gray")))
    print("")
    _disclaimer()
    print("")
    print(header("enable the short commands", "magenta"))
    print("")
    print(PAD + paint("A) this terminal only", "white", "bold")
          + paint("   run:  ", "gray") + paint(_local_source_cmd(), "yellow",
                                               "bold"))
    print(PAD + paint("B) every terminal", "white", "bold")
          + paint("      run:  ", "gray")
          + paint("python3 play.py setup persist", "yellow", "bold"))
    print("")
    print(PAD + paint("remove later with  python3 play.py uninstall", "gray"))
    print(PAD + paint("or skip shortcuts entirely -- python3 play.py … always "
                      "works.", "gray"))


def cmd_setup_persist():
    status, rc = _install_persistent()
    if status == "added":
        print(paint("  %s Shortcuts enabled in %s." % (OK, rc), "green", "bold"))
        print("  Activate now:  %s" % paint("source " + rc, "yellow", "bold"))
    elif status == "installed":
        print(paint("  %s Already enabled in %s." % (OK, rc), "green"))
    else:
        print(paint("  %s %s is missing -- can't install."
                    % (NO, _shortcuts_label()), "red"))


def cmd_uninstall():
    removed, rc = _uninstall_persistent()
    if removed:
        print(paint("  %s Removed PyQuest shortcuts from %s." % (OK, rc),
                    "green", "bold"))
    else:
        print(paint("  No persistent shortcuts in %s." % rc, "gray"))
    # Whether or not the rc line existed, the current shell may still hold the
    # functions; only the shell can clear those.
    print(PAD + paint("New terminals won't load the shortcuts. This terminal "
                      "keeps them until", "gray"))
    print(PAD + paint("you close it -- or run:  %s"
                      % paint("unset -f begin check start hint next …", "yellow"),
                      "gray"))
