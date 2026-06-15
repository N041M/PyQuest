#!/usr/bin/env python3
"""PyQuest, one-step start.

    python3 start.py

Checks your Python, turns on the short commands (check, hint, map, ...) for
this terminal session, and opens the main menu. Nothing is installed
permanently: when you close the session the shortcuts are gone. (Persist them
in every terminal later from the menu's shortcuts option, or `play.py setup`.)

It works the same on macOS (zsh), Linux / Codespaces (bash), and Windows
(PowerShell): start.py detects the shell and hosts the session in it.
"""

import os
import sys
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
MIN_PY = (3, 8)


def main():
    if sys.version_info < MIN_PY:
        sys.stderr.write(
            "PyQuest needs Python %d.%d or newer; this is Python %d.%d.\n"
            "Get a newer Python 3 from https://www.python.org/downloads/.\n"
            % (MIN_PY[0], MIN_PY[1], sys.version_info[0], sys.version_info[1]))
        return 1

    play = os.path.join(ROOT, "play.py")
    kind, exe = detect_shell()

    if kind is None:
        # No shell we can host the shortcuts in: just open the menu.
        print("Opening the menu. (Couldn't set up the short commands for this\n"
              "shell; you can still run `%s play.py <command>`.)" % _py())
        return subprocess.call([sys.executable, play, "begin"])

    print("Starting PyQuest with the short commands on for this session.")
    print("When you're done, type  exit  to leave the PyQuest session.\n")
    try:
        return launch(kind, exe, play)
    except OSError:
        # Spawning the shell failed for some reason; fall back to the menu.
        return subprocess.call([sys.executable, play, "begin"])


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


def launch(kind, exe, play):
    py = sys.executable
    sh = os.path.join(ROOT, "shell")

    if kind == "powershell":
        ps1 = os.path.join(sh, "pyquest.ps1")
        cmd = ". '%s'; & '%s' '%s' begin" % (ps1, py, play)
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
                '"%s" "%s" begin\n' % (rc_src, py, play))
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
            '"%s" "%s" begin\n' % (rc_src, py, play))
        with open(rc, "w") as f:
            f.write(body)
        return subprocess.call([exe, "--rcfile", rc, "-i"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
