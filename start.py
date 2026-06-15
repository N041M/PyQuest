#!/usr/bin/env python3
"""PyQuest, the one entry point.

    python3 start.py            set up the session shortcuts and open the menu
    python3 start.py <command>  run a single command (check, hint, next, ...)

With no arguments it checks your Python, turns on the short commands (check,
hint, map, ...) for this terminal session, and opens the main menu. Nothing is
installed permanently: when you close the session the shortcuts are gone.
(Persist them in every terminal later from the menu's shortcuts option, or
`start.py setup`.) Given a command, it runs that one command and exits, so the
shell shortcuts and the menu both drive it.

It works the same on macOS (zsh), Linux / Codespaces (bash), and Windows
(PowerShell): start.py detects the shell and hosts the session in it.
"""

import os
import sys
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
ENTRY = os.path.abspath(__file__)
MIN_PY = (3, 8)


def main():
    if sys.version_info < MIN_PY:
        sys.stderr.write(
            "PyQuest needs Python %d.%d or newer; this is Python %d.%d.\n"
            "Get a newer Python 3 from https://www.python.org/downloads/.\n"
            % (MIN_PY[0], MIN_PY[1], sys.version_info[0], sys.version_info[1]))
        return 1

    # A verb -- or being run from inside an already-set-up session -- means
    # "just run this command". Only a cold, bare `python3 start.py` sets up a
    # fresh session shell and opens the menu.
    if sys.argv[1:] or os.environ.get("PYQUEST_SHELL"):
        return dispatch()
    return launch_session()


def dispatch():
    """Run one command through the engine and exit (the puzzle loop)."""
    sys.path.insert(0, ROOT)
    from engine.app import main as run
    run()
    return 0


def launch_session():
    """Cold start: host a session shell with the shortcuts on, open the menu."""
    kind, exe = detect_shell()
    if kind is None:
        # No shell we can host the shortcuts in: just open the menu.
        print("Opening the menu. (Couldn't set up the short commands for this\n"
              "shell; you can still run `%s start.py <command>`.)" % _py())
        return subprocess.call([sys.executable, ENTRY, "begin"])

    print("Starting PyQuest with the short commands on for this session.")
    print("When you're done, type  exit  to leave the PyQuest session.\n")
    try:
        return launch(kind, exe)
    except OSError:
        # Spawning the shell failed for some reason; fall back to the menu.
        return subprocess.call([sys.executable, ENTRY, "begin"])


def _py():
    return os.path.basename(sys.executable) or "python3"


def detect_shell():
    """Return (kind, executable) for the shell to host the session in."""
    if os.name == "nt":
        for exe in ("pwsh", "powershell"):
            if _which(exe):
                return "powershell", exe
        return None, None
    shell = os.environ.get("SHELL", "")
    if shell.endswith("bash") and _which("bash"):
        return "bash", "bash"
    if _which("zsh"):
        return "zsh", "zsh"
    if _which("bash"):
        return "bash", "bash"
    return None, None


def _which(name):
    from shutil import which
    return which(name) is not None


def launch(kind, exe):
    py = sys.executable
    sh = os.path.join(ROOT, "shell")

    if kind == "powershell":
        ps1 = os.path.join(sh, "pyquest.ps1")
        cmd = ". '%s'; & '%s' '%s' begin" % (ps1, py, ENTRY)
        return subprocess.call([exe, "-NoExit", "-NoProfile", "-Command", cmd])

    # zsh / bash: a throwaway startup file that keeps the user's own
    # environment, loads the shortcuts, opens the menu, then stays interactive.
    import tempfile
    import shutil
    rc_src = os.path.join(sh, "pyquest.%s" % kind)
    tmp = tempfile.mkdtemp(prefix="pyquest_start_")
    try:
        if kind == "zsh":
            body = (
                '[ -f "$HOME/.zshenv" ] && source "$HOME/.zshenv"\n'
                '[ -f "$HOME/.zshrc" ] && source "$HOME/.zshrc"\n'
                'source "%s"\n'
                'export PYQUEST_SHELL=1\n'
                '"%s" "%s" begin\n' % (rc_src, py, ENTRY))
            with open(os.path.join(tmp, ".zshrc"), "w") as f:
                f.write(body)
            env = dict(os.environ, ZDOTDIR=tmp)
            return subprocess.call([exe, "-i"], env=env)
        # bash
        rc = os.path.join(tmp, "rc")
        body = (
            '[ -f "$HOME/.bashrc" ] && source "$HOME/.bashrc"\n'
            'source "%s"\n'
            'export PYQUEST_SHELL=1\n'
            '"%s" "%s" begin\n' % (rc_src, py, ENTRY))
        with open(rc, "w") as f:
            f.write(body)
        return subprocess.call([exe, "--rcfile", rc, "-i"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
