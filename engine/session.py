"""Hosting a PyQuest session: detect the shell, load the short commands for
this terminal only, and open the menu. This is the one place that spawns a
shell; nothing is installed permanently (close the session and the shortcuts
are gone). `start.py` calls `launch_session()` for a cold, bare launch.

It works the same on macOS (zsh), Linux / Codespaces (bash), and Windows
(PowerShell): the shell is detected and the session is hosted inside it.
"""

import os
import sys
import subprocess

from .config import ROOT

ENTRY = os.path.join(ROOT, "start.py")     # the verb the spawned shell runs


def launch_session():
    """Cold start: host a session shell with the shortcuts on, open the menu."""
    kind, exe = detect_shell()
    if kind is None:
        # No shell we can host the shortcuts in: just open the menu.
        print("Opening the menu. (Couldn't set up the short commands for this\n"
              "shell; you can still run `%s start.py <command>`.)" % _py())
        return subprocess.call([sys.executable, ENTRY, "menu"])

    print("Starting PyQuest with the short commands on for this session.")
    print("When you're done, type  exit  to leave the PyQuest session.\n")
    try:
        return _launch(kind, exe)
    except OSError:
        # Spawning the shell failed for some reason; fall back to the menu.
        return subprocess.call([sys.executable, ENTRY, "menu"])


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


def _launch(kind, exe):
    py = sys.executable
    sh = os.path.join(ROOT, "shell")

    if kind == "powershell":
        ps1 = os.path.join(sh, "pyquest.ps1")
        cmd = ". '%s'; & '%s' '%s' menu" % (ps1, py, ENTRY)
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
                '"%s" "%s" menu\n' % (rc_src, py, ENTRY))
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
            '"%s" "%s" menu\n' % (rc_src, py, ENTRY))
        with open(rc, "w") as f:
            f.write(body)
        return subprocess.call([exe, "--rcfile", rc, "-i"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
