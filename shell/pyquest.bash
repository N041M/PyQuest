# PyQuest shell shortcuts (bash)
# Lets you type `check`, `hint`, `solution`, etc. instead of
# `python3 start.py check`. Source this from your ~/.bashrc, run it directly, or
# just use `python3 start.py`, which loads it for the session for you.
#
# To uninstall: delete the line that sources this file from ~/.bashrc
# (look for "PyQuest shell shortcuts"), then open a new terminal.

# Resolve this file's own location, so the PyQuest folder can be moved or
# cloned anywhere without editing this file.
PYQUEST_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Internal: run start.py with the short-command display turned on.
_pyquest() { PYQUEST_SHELL=1 python3 "$PYQUEST_ROOT/start.py" "$@"; }

# Umbrella command: `start` (opens the menu), `start check`, `start wipe profile`, etc.
start()    { _pyquest "$@"; }
pq()       { _pyquest "$@"; }   # short alias for `start`
pyquest()  { _pyquest "$@"; }

# Bare verbs, usable from any directory.
menu()     { _pyquest menu "$@"; }   # the main hub, from anywhere
back()     { _pyquest menu "$@"; }   # leave a puzzle, return to the menu

# `uninstall` removes the persistent line AND clears the shortcuts from THIS
# terminal -- a program can't unset functions in your shell, so we do it here.
uninstall() {
    _pyquest uninstall "$@"
    echo "  shortcuts cleared from this terminal too."
    unset -f start pq pyquest menu back status help setup textbook ref \
        check hint solution map stats score next goto load skip retry replay \
        restart mode theme user users wipe _pyquest uninstall 2>/dev/null
}
status()   { _pyquest status "$@"; }
help()     { _pyquest help "$@"; }   # PyQuest's command list (overrides while sourced)
setup()    { _pyquest setup "$@"; }
textbook()  { _pyquest textbook "$@"; }   # syntax & tips; `textbook all` for everything
ref()      { _pyquest textbook "$@"; }
check()    { _pyquest check "$@"; }
hint()     { _pyquest hint "$@"; }
solution() { _pyquest solution "$@"; }
map()      { _pyquest map "$@"; }
stats()    { _pyquest stats "$@"; }   # your attempts, hints, per-chapter progress
score()    { _pyquest stats "$@"; }
next()     { _pyquest next "$@"; }
goto()     { _pyquest goto "$@"; }
load()     { _pyquest load "$@"; }
skip()     { _pyquest skip "$@"; }
retry()    { _pyquest retry "$@"; }
replay()   { _pyquest replay "$@"; }
restart()  { _pyquest restart "$@"; }   # start the current puzzle over
mode()     { _pyquest mode "$@"; }
theme()    { _pyquest theme "$@"; }
user()     { _pyquest user "$@"; }
users()    { _pyquest user "$@"; }

# `wipe` erases the whole profile; it needs the explicit word to fire (`wipe
# profile`), so the bare verb is harmless. No clash with any system command, so
# unlike the old `reset` it needs no context-aware wrapper.
wipe()     { _pyquest wipe "$@"; }
