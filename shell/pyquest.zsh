# PyQuest shell shortcuts
# Lets you type `check`, `hint`, `solution`, etc. instead of
# `python3 start.py check`. Source this from your ~/.zshrc, or run it directly.
#
# To uninstall: delete the line that sources this file from ~/.zshrc
# (look for "PyQuest shell shortcuts"), then open a new terminal.

# Resolve this file's own location, so the PyQuest folder can be moved or
# cloned anywhere without editing this file. (%x is the path of the file being
# sourced; :A makes it absolute, and :h:h climbs from shell/pyquest.zsh up to
# the pyquest root.)
export PYQUEST_ROOT="${${(%):-%x}:A:h:h}"

# Internal: run start.py with the short-command display turned on.
_pyquest() { PYQUEST_SHELL=1 python3 "$PYQUEST_ROOT/start.py" "$@"; }

# Umbrella command: `start` (opens the menu), `start check`, `start reset`, etc.
start()    { _pyquest "$@"; }
pq()       { _pyquest "$@"; }   # short alias for `start`
pyquest()  { _pyquest "$@"; }

# Bare verbs, usable from any directory.
begin()    { _pyquest begin "$@"; }
menu()     { _pyquest menu "$@"; }   # back to the main menu from anywhere
back()     { _pyquest menu "$@"; }   # leave a puzzle, return to the menu

# `uninstall` removes the persistent line AND clears the shortcuts from THIS
# terminal -- a program can't unset functions in your shell, so we do it here.
uninstall() {
    _pyquest uninstall "$@"
    echo "  shortcuts cleared from this terminal too."
    unset -f start pq pyquest begin menu back status help setup lexicon ref \
        check hint solution map next goto load skip retry replay revert mode \
        theme user users reset _pyquest uninstall 2>/dev/null
}
status()   { _pyquest status "$@"; }
help()     { _pyquest help "$@"; }   # PyQuest's command list (overrides while sourced)
setup()    { _pyquest setup "$@"; }
lexicon()  { _pyquest lexicon "$@"; }   # syntax & tips; `lexicon all` for everything
ref()      { _pyquest lexicon "$@"; }
check()    { _pyquest check "$@"; }
hint()     { _pyquest hint "$@"; }
solution() { _pyquest solution "$@"; }
map()      { _pyquest map "$@"; }
next()     { _pyquest next "$@"; }
goto()     { _pyquest goto "$@"; }
load()     { _pyquest load "$@"; }
skip()     { _pyquest skip "$@"; }
retry()    { _pyquest retry "$@"; }
replay()   { _pyquest replay "$@"; }
revert()   { _pyquest revert "$@"; }
mode()     { _pyquest mode "$@"; }
theme()    { _pyquest theme "$@"; }
user()     { _pyquest user "$@"; }
users()    { _pyquest user "$@"; }

# `reset` is also a real macOS command that reinitializes the terminal. To make
# the bare word do the obvious thing without losing that, it is context-aware:
#   - inside the PyQuest folder, `reset` clears PyQuest progress (after a y/N
#     prompt, since it wipes your code and progress);
#   - anywhere else, it falls through to the normal terminal reset.
# You can always reach each one explicitly: `start reset` and `command reset`.
reset() {
  case "$PWD/" in
    "$PYQUEST_ROOT"/*)
      local ans
      read -r "ans?Wipe ALL PyQuest progress, saved code and workspaces? [y/N] "
      case "$ans" in
        [yY]*) _pyquest reset ;;
        *) echo "Cancelled.  (For the terminal reset instead: command reset)" ;;
      esac
      ;;
    *) command reset "$@" ;;
  esac
}
