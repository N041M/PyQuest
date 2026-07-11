# PyQuest translations -- language 'example' -- pack name + UI strings.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply example

TRANSLATIONS = {

"name": "Čeština",

"ui app.lang_nudge": "PyQuest also speaks %s -- type  language %s  in the menu.",

"ui app.no_loaded_menu": "No puzzle loaded yet -- here's the menu.",

"ui app.no_puzzles": "No puzzles found under %s",

"ui app.open_menu_status": r"""Open the menu to set up and pick a level:  %s
""",

"ui app.run_full_list": "run  %s  for the full list.",

"ui app.setup_below": r"""Set up and pick a level from the menu below.
""",

"ui app.unknown": "Unknown command '%s'.",

"ui app.unknown_suggest": "Unknown command '%s'. Did you mean  %s ?",

"ui app.wb_where": "You were on %s · %s.",

"ui app.welcome": "Welcome to PyQuest!",

"ui app.welcome_back.few": "Welcome back -- it's been %d days.",

"ui app.welcome_back.one": "Welcome back -- it's been %d day.",

"ui app.welcome_back.other": "Welcome back -- it's been %d days.",

"ui brief.none": "No brief for this puzzle.",

"ui brief.title": "brief · %s · %s",

"ui card.chapter": "chapter %d · %s",

"ui card.f_edit": "edit",

"ui card.f_read": "read",

"ui card.hint_lead": "hint",

"ui card.locked": "locked",

"ui card.note_lead": "note",

"ui card.save_before": "(save before checking)",

"ui card.solved": "solved",

"ui chapter.intro": "chapter %d · %s",

"ui chapter.puzzles.few": "%d puzzles",

"ui chapter.puzzles.one": "%d puzzle",

"ui chapter.puzzles.other": "%d puzzles",

"ui check.banner_not_yet": "not yet",

"ui check.banner_so_close": "so close",

"ui check.banner_solved": "solved",

"ui check.bonus_default": "this works, but could be more efficient",

"ui check.bonus_no": "bonus: not optimal yet — %s",

"ui check.bonus_yes": "bonus: optimal — efficient solution",

"ui check.chapter_done": "chapter %d complete -- %d/%d",

"ui check.code_saved": "your code is saved.",

"ui check.course_done": "COURSE COMPLETE -- every puzzle solved!",

"ui check.crash_body": r"""Python raised an error%s:

%s

Read the error name: it points at what went wrong.

%s
""",

"ui check.crash_title": "Crash -- your code started but hit an error",

"ui check.crash_title2": "Crash -- your code hit an error",

"ui check.expected": "Expected:",

"ui check.first_diff": "%s marks line %d -- the first line that differs.",

"ui check.got": "Got:",

"ui check.lesson_body": r"""Your output is correct -- but this puzzle isn't really about the answer.
It's teaching a specific tool, and your solution reached the result
another way, so the lesson got skipped.
""",

"ui check.lesson_rework": "Rework it to use what the puzzle teaches, then check again.",

"ui check.lesson_title": "Correct answer -- but not this puzzle's lesson",

"ui check.lesson_wants": "This puzzle wants:",

"ui check.missing_body": r"""Your file doesn't define `%s`.

Check the spelling, or add it. For a function the brief asks for
`%s`, define it with:  def %s(...):
""",

"ui check.missing_title": "Missing piece -- something isn't defined yet",

"ui check.next": "next",

"ui check.no_loaded": "No puzzle loaded.",

"ui check.nudge_hard": "Hard mode: hints unlock after 3 attempts (%d so far).",

"ui check.nudge_hints": "Hints are now available:  %s",

"ui check.nudge_stuck": "Stuck?  %s",

"ui check.retry": "retry",

"ui check.retry_hint": "to clear it and solve again from scratch",

"ui check.save_tip": r"""Did you save work.py in your editor? Unsaved edits are the #1 cause
of a check that 'should' pass but doesn't.
""",

"ui check.start_first": "Start one first:",

"ui check.streak.few": "%d-day streak",

"ui check.streak.one": "%d-day streak",

"ui check.streak.other": "%d-day streak",

"ui check.syntax_body": r"""Python stopped at %s

This usually means a typo: a missing quote, parenthesis, colon,
or wrong indentation. Open work.py and check that line.
""",

"ui check.syntax_title": "Syntax error -- Python could not read your file",

"ui check.tests_unloadable": r"""Internal: could not load this puzzle's tests.
""",

"ui check.tip_attributeerror": "AttributeError: that value has no such method or attribute -- check what type you are calling it on.",

"ui check.tip_indexerror": "IndexError: that position doesn't exist -- positions start at 0, and the last one is len(...) - 1.",

"ui check.tip_keyerror": "KeyError: that key isn't in the dictionary -- check the exact spelling, or read with .get(key).",

"ui check.tip_nameerror": "NameError: that name isn't defined yet -- check the spelling, or define it above the line that uses it.",

"ui check.tip_typeerror": "TypeError: the values' types don't fit the operation -- like adding text to a number; convert first with str() or int().",

"ui check.tip_unbound": "UnboundLocalError: the variable is read before it gets a value on this path -- give it a starting value first.",

"ui check.tip_valueerror": "ValueError: the type is right but the value doesn't work -- like int('abc').",

"ui check.tip_zerodivision": "ZeroDivisionError: division by zero -- make sure the denominator can't be 0 before dividing.",

"ui check.today.few": "%d solved today",

"ui check.today.one": "%d solved today",

"ui check.today.other": "%d solved today",

"ui check.unchanged": "work.py is byte-for-byte identical to your last attempt -- did you save it in your editor?",

"ui check.was_last": "that was the last puzzle in the course.",

"ui check.wrong_title": "Wrong result -- the code runs but the answer is off",

"ui check.your_code": "Your code:",

"ui cockpit.footer": "arrows move · Enter runs it · type a verb · Esc to the shell",

"ui date.days_ago.few": "%d days ago",

"ui date.days_ago.one": "%d day ago",

"ui date.days_ago.other": "%d days ago",

"ui date.today": "today",

"ui date.yesterday": "yesterday",

"ui doctor.color_off": "no color",

"ui doctor.color_on": "color",

"ui doctor.cols": "columns",

"ui doctor.keys_off": "typed input",

"ui doctor.keys_on": "arrow keys",

"ui doctor.paste_hint": "paste this block into a bug report.",

"ui doctor.persistent": "shortcuts persistent: %s",

"ui doctor.profiles": "profiles",

"ui doctor.puzzles.few": "%d puzzles",

"ui doctor.puzzles.one": "%d puzzle",

"ui doctor.puzzles.other": "%d puzzles",

"ui doctor.title": "doctor",

"ui goto.footer": "run  %s   e.g.  %s   (a bare chapter number works too: %s)",

"ui goto.no_match": "There is no puzzle '%s'. Pick one of these:",

"ui goto.prompt": "id (blank = cancel) >",

"ui goto.title": "goto · choose a puzzle",

"ui help.available_now": "available now",

"ui help.desc.brief": "read the current puzzle's brief here in the terminal",

"ui help.desc.check": "validate your work.py",

"ui help.desc.doctor": "environment report: versions, terminal, profile -- paste into bug reports",

"ui help.desc.export": "save this profile's progress to a portable file",

"ui help.desc.goto": "jump to a puzzle (goto 2.4, or goto 2 for chapter 2; bare opens a picker)",

"ui help.desc.help": "show this command list",

"ui help.desc.hint": "reveal the next hint",

"ui help.desc.import": "load a profile from an exported file",

"ui help.desc.map": "show the chapter/puzzle tree (map all expands solved chapters)",

"ui help.desc.menu": "open the main menu (start here, or back out of a puzzle)",

"ui help.desc.mode": "set difficulty: easy | normal | hard",

"ui help.desc.next": "move on once this puzzle is solved",

"ui help.desc.note": "jot a personal note on this puzzle (bare note shows it, note clear removes it)",

"ui help.desc.restart": "start this puzzle over: blank code + clear its progress (retry keeps it solved)",

"ui help.desc.resume": "jump to the first puzzle you haven't solved",

"ui help.desc.retry": "blank the workspace to practice again (stays solved)",

"ui help.desc.search": "find a puzzle by a word in its title or concept",

"ui help.desc.setup": "set up the short commands (offers local or persistent)",

"ui help.desc.skip": "give up and move on without solving (not in hard mode)",

"ui help.desc.solution": "show the reference solution",

"ui help.desc.stats": "your numbers: attempts, hints, per-chapter completion",

"ui help.desc.status": "show progress and the current puzzle",

"ui help.desc.textbook": "syntax & tips you've reached (textbook all: everything · textbook <chapter|word>: one slice)",

"ui help.desc.theme": "switch colour theme (neon, amber, forest, mono, or a themes/ preset)",

"ui help.desc.uninstall": "remove the persistent shortcuts",

"ui help.desc.user": "switch or create a profile",

"ui help.desc.wipe": "erase progress: this profile (wipe profile), or every profile + settings (wipe everything, asks you to type ERASE)",

"ui help.footer": "%s available now   %s needs a puzzle loaded",

"ui help.group_always": "anywhere",

"ui help.group_puzzle": "while solving a puzzle",

"ui help.in_puzzle": "in puzzle %s",

"ui help.load_first": "load a puzzle first (%s)",

"ui help.no_loaded": "no puzzle loaded",

"ui help.title": "command reference",

"ui hint.hard_locked": "Hard mode: hints unlock after 3 attempts (%d so far).",

"ui hint.more": "run hint again for more",

"ui hint.no_more": "No more hints. Try:  %s",

"ui hint.none": "No hints for this puzzle.",

"ui hint.title": "hint  %d / %d · %s",

"ui jump.locked": "'%s' is locked.",

"ui jump.locked_2": "In %s mode you can only revisit unlocked puzzles.",

"ui jump.locked_3": "Use %s to advance one, or switch to easy mode.",

"ui jump.now_on": "Now on %s -- %s%s",

"ui jump.restored": "  (your saved code was restored)",

"ui keys.arrows": "arrows move",

"ui keys.enter": "Enter select",

"ui keys.esc": "Esc back",

"ui keys.filter": "type to filter",

"ui keys.filter_matches": "%d of %d match · Enter picks",

"ui keys.no_filter_match": "no match -- Backspace edits, Enter submits the text, Esc backs out",

"ui keys.position": "%d of %d",

"ui keys.type": "type to enter one",

"ui lang.picker_title": "language",

"ui lang.prompt": "language code  (0 = back) >",

"ui lang.set": "language set to %s.",

"ui map.folded": "all %d solved -- expand with  %s",

"ui map.title": "map",

"ui menu.footer_compact": "arrows select · Enter runs it · type a verb",

"ui menu.footer_full": "arrows move · Enter chooses · type a verb · help",

"ui menu.learn": "učit se",

"ui menu.level_prompt": "id  (0 = back) >",

"ui menu.level_title": "select level",

"ui menu.main_title": "main menu",

"ui menu.note.map": "the chapter / puzzle tree",

"ui menu.note.select": "jump to any puzzle",

"ui menu.note.settings": "theme · mode · profiles · shortcuts",

"ui menu.note.stats": "attempts · hints · pace",

"ui menu.note.textbook": "syntax & tips so far",

"ui menu.note.textbook_sealed": "sealed in hard mode",

"ui menu.play": "hrát",

"ui menu.see_you": "see you in the terminal -- solve with",

"ui menu.setup": "nastavit",

"ui menu.tty_only": "(run this in a terminal to choose)",

"ui menu.type_number": "type a number 0-6, or a command.",

"ui menu.verb_needs_puzzle": "'%s' runs in your terminal, once a puzzle is open.",

"ui menu.verb_needs_puzzle_2": "Pick %s to start, then save work.py and run  %s",

"ui menu.verb_terminal": "'%s' is a terminal command, not a menu option.",

"ui menu.verb_terminal_2": "Leave the menu (%s) and run  %s",

"ui mode.current": "Current mode: %s",

"ui mode.desc_easy": "Pointers shown, hints/solution always available, free jumps.",

"ui mode.desc_hard": "No skips; hints after 3 tries; solution after solving; textbook sealed.",

"ui mode.desc_normal": "Hints on demand, skip forward allowed.",

"ui mode.picker_title": "difficulty",

"ui mode.prompt": "easy / normal / hard  (0 = back) >",

"ui mode.set": "Mode set to '%s'.",

"ui mode.usage": "Usage: %s",

"ui nav.hard_skip": "Switch to an easier mode to skip:  %s",

"ui nav.hard_solve": "Hard mode: you must solve %s before moving on.",

"ui nav.last_puzzle": "That was the last puzzle in the course.",

"ui nav.moved_on": "Moved on from",

"ui nav.not_solved": "%s isn't solved yet.",

"ui nav.not_solved_2": "Run %s until it passes, or %s to move on without solving.",

"ui nav.skipped": "Skipped (not solved)",

"ui note.add_one": "add one with",

"ui note.cleared": "Note cleared on %s.",

"ui note.header": "note on %s:",

"ui note.none_clear": "no note on %s to clear.",

"ui note.none_yet": "no note on %s yet.",

"ui note.saved": "Noted on %s.",

"ui profiles.arrow_hint": "arrow to a name to switch · '+ new profile' to create · or type 'rename a b' / 'delete a'",

"ui profiles.new_entry": "+ new profile",

"ui profiles.new_prompt": "new profile name  (blank = cancel) >",

"ui profiles.prompt": "name to switch/create · 'rename a b' · 'delete a'  (0 = back) >",

"ui profiles.title": "profiles",

"ui restart.done": "Restarted %s -- blank workspace, progress cleared.",

"ui resume.all_solved": "Every puzzle is solved -- nothing to resume.",

"ui resume.at": "Resuming at %s.",

"ui resume.revisit": "revisit any with",

"ui retry.reload": "if your editor still shows old code, reload work.py -- its on-disk copy is now blank.",

"ui retry.reset": "Reset %s to a blank workspace -- give it another go.",

"ui retry.stays_solved": "(it stays marked solved; this is just practice)",

"ui search.broaden": "try a broader word, or browse the",

"ui search.matches.few": "%d matches -- open one with  %s",

"ui search.matches.one": "%d match -- open one with  %s",

"ui search.matches.other": "%d matches -- open one with  %s",

"ui search.no_match": "no puzzle matches '%s'.",

"ui search.title": "search · %s",

"ui search.usage": "usage:",

"ui search.usage_hint": "Find a puzzle by a word in its title or concept.",

"ui session.no_shell": r"""Opening the menu. (Couldn't set up the short commands for this
shell; you can still run `%s start.py <command>`.)
""",

"ui session.starting": "Starting PyQuest with the short commands on for this session.",

"ui session.when_done": r"""When you're done, type  exit  to leave the PyQuest session.
""",

"ui settings.persistent": "persistent: %s",

"ui settings.title": "settings",

"ui settings.type_hint": "type theme / mode / profiles / shortcuts / language, or Esc.",

"ui settings.type_number": "type 1-5, or 0 to go back.",

"ui setup.activate_now": "Activate now:  %s",

"ui setup.already": "Already enabled in %s.",

"ui setup.enable_title": "enable the short commands",

"ui setup.enabled": "Shortcuts enabled in %s.",

"ui setup.f_python": "python",

"ui setup.f_status": "status",

"ui setup.missing": "%s is missing -- can't install.",

"ui setup.none": "No persistent shortcuts in %s.",

"ui setup.opt_a": "A) this terminal only",

"ui setup.opt_b": "B) every terminal",

"ui setup.persist_off": "shortcuts not persistently installed",

"ui setup.persist_on": "persistent shortcuts enabled in %s",

"ui setup.remove_later": "remove later with  python3 start.py uninstall",

"ui setup.removed": "Removed PyQuest shortcuts from %s.",

"ui setup.run": "run:",

"ui setup.skip": "or skip shortcuts entirely -- python3 start.py … always works.",

"ui setup.title": "setup",

"ui setup.uninstall_note": "New terminals won't load the shortcuts. This terminal keeps them until",

"ui setup.uninstall_note_2": "you close it -- or run:  %s",

"ui shortcuts.disc_funcs": "They are shell functions defined in %s (check, hint, start, …).",

"ui shortcuts.disc_local": "Local = nothing outside this folder changes.  Persistent = one line in your shell startup file.",

"ui shortcuts.disc_post": "  instead of  python3 start.py check.",

"ui shortcuts.disc_pre": "Shortcuts let you type",

"ui shortcuts.opt_local": "enable for THIS terminal (local, nothing saved)",

"ui shortcuts.opt_persist": "install persistently (one line in your startup file)",

"ui shortcuts.opt_uninstall": "uninstall (remove the persistent line)",

"ui shortcuts.run_yourself": "Run this yourself (a program can't source into your shell):",

"ui shortcuts.title": "shortcuts",

"ui solution.hard_locked": "Hard mode: the solution unlocks only after you solve it.",

"ui solution.none": "No solution file for this puzzle.",

"ui solution.title": "solution · %s · %s",

"ui solution.why": "why it works",

"ui stats.all_solved.few": "all %d puzzles solved -- %d on the first try, no hints.",

"ui stats.all_solved.one": "all %d puzzle solved -- %d on the first try, no hints.",

"ui stats.all_solved.other": "all %d puzzles solved -- %d on the first try, no hints.",

"ui stats.by_chapter": "by chapter",

"ui stats.clean_tail": "solved first try, no hints",

"ui stats.course_complete": "course complete",

"ui stats.f_active": "active",

"ui stats.f_clean": "clean",

"ui stats.f_hints": "hints",

"ui stats.f_pace": "pace",

"ui stats.f_since": "since",

"ui stats.f_solved": "solved",

"ui stats.f_streak": "streak",

"ui stats.f_today": "today",

"ui stats.f_tries": "tries",

"ui stats.hints_tail": "hints revealed",

"ui stats.in_a_row": "in a row",

"ui stats.last_14": "solves, last 14 days",

"ui stats.streak.few": "%d days",

"ui stats.streak.one": "%d day",

"ui stats.streak.other": "%d days",

"ui stats.title": "stats · %s",

"ui stats.today_tail": "solved today",

"ui stats.tries_tail": "check runs across all puzzles",

"ui stats.x_of_y": "%d of %d",

"ui status.all_complete.few": "%s  All %d puzzles complete.",

"ui status.all_complete.one": "%s  All %d puzzle complete.",

"ui status.all_complete.other": "%s  All %d puzzles complete.",

"ui status.no_current": "No current puzzle.",

"ui status.no_loaded": "No puzzle loaded.",

"ui status.open_menu": "Open the menu to pick a level and start:",

"ui status.revisit_goto": "revisit any with  goto <id>",

"ui textbook.f_read": "read",

"ui textbook.hard_sealed": "Hard mode: the textbook is sealed -- work from the brief.",

"ui textbook.md_chapter": "Chapter %d · %s",

"ui textbook.md_empty": "Nothing covered yet -- work through a few topics, or run `textbook all` to preview the whole language.",

"ui textbook.md_full_1": "The whole language PyQuest covers -- every chapter, all %d topics.",

"ui textbook.md_full_2": "Run `textbook` to come back to just the chapters you've reached.",

"ui textbook.md_reached_1": "A technical reference for what you've reached -- %d of %d topics.",

"ui textbook.md_reached_2": "Run `textbook all` for the whole language; `textbook` brings you back here.",

"ui textbook.md_title": "PyQuest Textbook",

"ui textbook.md_topic": "Just %s. Run `textbook` for everything you've reached, `textbook all` for the whole language.",

"ui textbook.no_topic": "no chapter or topic matches '%s'.",

"ui textbook.open_it": "open it in your editor",

"ui textbook.ready": "Textbook ready: %s.",

"ui textbook.revert": "revert to just what you've reached:",

"ui textbook.scope_chapter": "chapter %s",

"ui textbook.see_all": "see the whole language:",

"ui textbook.topic_hint": "try a chapter number or a word:",

"ui textbook.where_full": "the full reference",

"ui textbook.where_none": "nothing reached yet",

"ui textbook.where_reached": "what you've reached -- %d of %d",

"ui textbook.where_topic.few": "%s -- %d topics",

"ui textbook.where_topic.one": "%s -- %d topic",

"ui textbook.where_topic.other": "%s -- %d topics",

"ui theme.add_own": "add your own: drop a JSON file in themes/ (see themes/README.md)",

"ui theme.list_title": "themes",

"ui theme.picker_title": "theme",

"ui theme.prompt": "theme name  (0 = back) >",

"ui theme.set": "theme set to '%s'.",

"ui theme.set_with": "set with",

"ui theme.unknown": "unknown theme '%s'. options: %s",

"ui transfer.answers.few": "%d saved answers",

"ui transfer.answers.one": "%d saved answer",

"ui transfer.answers.other": "%d saved answers",

"ui transfer.dropped.few": "note: %d completed id(s) aren't in this version's content and were dropped.",

"ui transfer.dropped.one": "note: %d completed id isn't in this version's content and was dropped.",

"ui transfer.dropped.other": "note: %d completed id(s) aren't in this version's content and were dropped.",

"ui transfer.exists_hint": "Import under a new name, or overwrite it:",

"ui transfer.exported": "Exported profile '%s' to %s.",

"ui transfer.import_usage_hint": "Imports a profile exported with  %s.",

"ui transfer.imported": "Imported into profile '%s' (now active).",

"ui transfer.move_hint": "Move it to another machine, then:  %s",

"ui transfer.no_file": "No such file: %s",

"ui transfer.not_export": "%s isn't a PyQuest export file.",

"ui transfer.pass_name": "Pass a valid name:  %s",

"ui transfer.puzzles.few": "%d puzzles completed",

"ui transfer.puzzles.one": "%d puzzle completed",

"ui transfer.puzzles.other": "%d puzzles completed",

"ui transfer.read_fail": "Couldn't read %s as a PyQuest export.",

"ui transfer.summary": "%s, %s.",

"ui transfer.write_fail": "Couldn't write %s (%s).",

"ui ui.back": "back",

"ui ui.legend": "%s done   %s here   %s to do",

"ui ui.mode": "mode",

"ui ui.no_current": "No current puzzle.",

"ui ui.no_puzzle": "no puzzle '%s'.",

"ui ui.off": "off",

"ui ui.on": "on",

"ui ui.usage": "usage:",

"ui user.already_on": "already on '%s'.",

"ui user.created_switched": "created and switched to",

"ui user.deleted": "Deleted profile '%s' and all its progress.",

"ui user.exists": "Profile '%s' already exists.",

"ui user.invalid_name": "'%s' can't be a profile name.",

"ui user.is_active": "'%s' is the active profile.",

"ui user.list_title": "users",

"ui user.manage": "rename  %s      delete  %s",

"ui user.manage_hint": "To manage profiles:  %s  ·  %s",

"ui user.name_rules": "Use only letters, digits, dashes, or underscores (up to 32 characters).",

"ui user.name_rules_1": "Names become folders under users/, so use only letters,",

"ui user.name_rules_2": "digits, dashes, or underscores (up to 32 characters).",

"ui user.no_profile": "No profile '%s'.",

"ui user.no_spaces": "'%s' can't be a profile name (no spaces).",

"ui user.renamed": "Renamed '%s' to '%s'.",

"ui user.same_name": "'%s' is already its name.",

"ui user.switch_create": "switch or create with",

"ui user.switch_first": "Switch to another first:  %s",

"ui user.switched_to": "switched to",

"ui wipe.all_cancelled": "Cancelled -- nothing was deleted.",

"ui wipe.all_done": "Everything wiped -- every profile deleted.",

"ui wipe.all_fresh": "PyQuest is factory-fresh; the next launch starts from scratch.",

"ui wipe.all_hint": "(to delete every profile and start factory-fresh:  %s)",

"ui wipe.all_how": "Type %s (exactly) to go ahead; anything else cancels.",

"ui wipe.all_tty_only": "Run this in a terminal -- it needs a typed confirmation.",

"ui wipe.all_warn": "This deletes EVERY profile on this install --",

"ui wipe.all_warn_2": "all progress, saved code, notes, and settings (theme, language).",

"ui wipe.cleared": "Cleared this profile's progress, saved code, and workspace.",

"ui wipe.confirm_hint": "It cannot be undone. To go ahead:  %s",

"ui wipe.done": "Profile wiped.",

"ui wipe.open_menu": "Open the menu to start again:  %s",

"ui wipe.restart_hint": "(to clear just the current puzzle instead, use  %s)",

"ui wipe.warn": "This erases EVERYTHING in profile '%s' --",

"ui wipe.warn_2": "every completed puzzle, all saved code, and the workspace.",
}
