# PyQuest translations -- language 'cs' -- pack name + UI strings.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply cs

TRANSLATIONS = {

"name": "Čeština",

"ui app.lang_nudge": "PyQuest umí i %s -- napiš  language %s  v menu.",

"ui app.no_loaded_menu": "Zatím není načtený žádný úkol -- tady je menu.",

"ui app.no_puzzles": "Pod %s nebyly nalezeny žádné úkoly",

"ui app.open_menu_status": r"""Otevři menu, nastav se a vyber úroveň:  %s
""",

"ui app.run_full_list": "spusť  %s  pro úplný seznam.",

"ui app.setup_below": r"""Nastav se a vyber úroveň v menu níže.
""",

"ui app.unknown": "Neznámý příkaz '%s'.",

"ui app.unknown_suggest": "Neznámý příkaz '%s'. Nemyslel jsi  %s ?",

"ui app.wb_where": "Skončil jsi na %s · %s.",

"ui app.welcome": "Vítej v PyQuestu!",

"ui app.welcome_back.few": "Vítej zpět -- jsou to %d dny.",

"ui app.welcome_back.one": "Vítej zpět -- je to %d den.",

"ui app.welcome_back.other": "Vítej zpět -- je to %d dní.",

"ui brief.none": "Tahle úloha nemá zadání.",

"ui brief.title": "zadání · %s · %s",

"ui card.chapter": "kapitola %d · %s",

"ui card.f_edit": "uprav",

"ui card.f_read": "čti",

"ui card.hint_lead": "rada  ",

"ui card.locked": "zamčeno",

"ui card.note_lead": "pozn. ",

"ui card.save_before": "(před kontrolou ulož)",

"ui card.solved": "vyřešeno",

"ui chapter.intro": "kapitola %d · %s",

"ui chapter.puzzles.few": "%d úlohy",

"ui chapter.puzzles.one": "%d úloha",

"ui chapter.puzzles.other": "%d úloh",

"ui check.banner_not_yet": "ještě ne",

"ui check.banner_so_close": "tak blízko",

"ui check.banner_solved": "vyřešeno",

"ui check.bonus_default": "funguje to, ale šlo by to efektivněji",

"ui check.bonus_no": "bonus: zatím není optimální — %s",

"ui check.bonus_yes": "bonus: optimální — efektivní řešení",

"ui check.chapter_done": "kapitola %d dokončena -- %d/%d",

"ui check.code_saved": "tvůj kód je uložený.",

"ui check.course_done": "KURZ DOKONČEN -- všechny úlohy vyřešeny!",

"ui check.crash_body": r"""Python vyvolal chybu%s:

%s

Přečti si název chyby: ukazuje, co se pokazilo.

%s
""",

"ui check.crash_title": "Pád -- tvůj kód se rozběhl, ale narazil na chybu",

"ui check.crash_title2": "Pád -- tvůj kód narazil na chybu",

"ui check.expected": "Očekáváno:",

"ui check.first_diff": "%s označuje řádek %d -- první řádek, který se liší.",

"ui check.got": "Dostal jsi:",

"ui check.lesson_body": r"""Tvůj výstup je správný -- ale tenhle úkol vlastně není o odpovědi.
Učí konkrétní nástroj a tvé řešení došlo k výsledku
jinak, takže se lekce přeskočila.
""",

"ui check.lesson_rework": "Přepracuj to tak, abys použil, co úkol učí, a zkontroluj znovu.",

"ui check.lesson_title": "Správná odpověď -- ale ne to, co tenhle úkol učí",

"ui check.lesson_wants": "Tenhle úkol chce:",

"ui check.missing_body": r"""Tvůj soubor nedefinuje `%s`.

Zkontroluj pravopis nebo to doplň. Funkci, kterou zadání žádá
`%s`, definuj takto:  def %s(...):
""",

"ui check.missing_title": "Chybí kousek -- něco ještě není definováno",

"ui check.next": "další",

"ui check.no_loaded": "Žádný úkol není načtený.",

"ui check.nudge_hard": "Těžký režim: rady se odemknou po 3 pokusech (zatím %d).",

"ui check.nudge_hints": "Rady jsou teď k dispozici:  %s",

"ui check.nudge_stuck": "Nevíš jak dál?  %s",

"ui check.retry": "znovu",

"ui check.retry_hint": "smazat a vyřešit znovu od začátku",

"ui check.save_tip": r"""Uložil jsi work.py v editoru? Neuložené úpravy jsou
číslo 1 příčina kontroly, která „má“ projít, ale neprojde.
""",

"ui check.start_first": "Nejdřív nějaký spusť:  ",

"ui check.streak.few": "%d dny v řadě",

"ui check.streak.one": "%d den v řadě",

"ui check.streak.other": "%d dní v řadě",

"ui check.syntax_body": r"""Python se zastavil na %s

Obvykle to znamená překlep: chybějící uvozovku, závorku, dvojtečku,
nebo špatné odsazení. Otevři work.py a zkontroluj ten řádek.
""",

"ui check.syntax_title": "Syntaktická chyba -- Python nedokázal přečíst tvůj soubor",

"ui check.tests_unloadable": r"""Interní: nepodařilo se načíst testy tohoto úkolu.
""",

"ui check.tip_attributeerror": "AttributeError: tahle hodnota takovou metodu ani atribut nemá -- zkontroluj, na jakém typu ji voláš.",

"ui check.tip_indexerror": "IndexError: tahle pozice neexistuje -- pozice začínají od 0 a poslední je len(...) - 1.",

"ui check.tip_keyerror": "KeyError: tenhle klíč ve slovníku není -- zkontroluj přesný zápis, nebo čti přes .get(klíč).",

"ui check.tip_nameerror": "NameError: tohle jméno ještě není definované -- zkontroluj překlepy, nebo ho definuj nad řádkem, který ho používá.",

"ui check.tip_typeerror": "TypeError: typy hodnot k operaci nesedí -- třeba sčítání textu s číslem; nejdřív převeď přes str() nebo int().",

"ui check.tip_unbound": "UnboundLocalError: proměnná se čte dřív, než na této cestě dostane hodnotu -- dej jí nejdřív výchozí hodnotu.",

"ui check.tip_valueerror": "ValueError: typ sedí, ale hodnota nefunguje -- třeba int('abc').",

"ui check.tip_zerodivision": "ZeroDivisionError: dělení nulou -- před dělením zajisti, že jmenovatel nemůže být 0.",

"ui check.today.few": "%d vyřešené dnes",

"ui check.today.one": "%d vyřešená dnes",

"ui check.today.other": "%d vyřešených dnes",

"ui check.unchanged": "work.py je do posledního bajtu stejný jako při minulém pokusu -- uložil jsi ho v editoru?",

"ui check.was_last": "to byl poslední úkol v kurzu.",

"ui check.wrong_title": "Špatný výsledek -- kód běží, ale odpověď nesedí",

"ui check.your_code": "Tvůj kód:",

"ui cockpit.footer": "šipky pohyb · Enter spustí · napiš příkaz · Esc do shellu",

"ui date.days_ago.few": "před %d dny",

"ui date.days_ago.one": "před %d dnem",

"ui date.days_ago.other": "před %d dny",

"ui date.today": "dnes",

"ui date.yesterday": "včera",

"ui doctor.color_off": "bez barev",

"ui doctor.color_on": "barvy",

"ui doctor.cols": "sloupců",

"ui doctor.keys_off": "psaný vstup",

"ui doctor.keys_on": "šipky",

"ui doctor.paste_hint": "tento blok vlož do hlášení chyby.",

"ui doctor.persistent": "zkratky trvale: %s",

"ui doctor.profiles": "profilů",

"ui doctor.puzzles.few": "%d úlohy",

"ui doctor.puzzles.one": "%d úloha",

"ui doctor.puzzles.other": "%d úloh",

"ui doctor.title": "diagnostika",

"ui goto.footer": "spusť  %s   např.  %s   (funguje i samotné číslo kapitoly: %s)",

"ui goto.no_match": "Úkol '%s' neexistuje. Vyber si jeden z těchto:",

"ui goto.prompt": "id (prázdné = zrušit) > ",

"ui goto.title": "goto · vyber úkol",

"ui help.available_now": "k dispozici teď",

"ui help.desc.brief": "přečti si zadání aktuální úlohy přímo v terminálu",

"ui help.desc.check": "zkontroluj svůj work.py",

"ui help.desc.doctor": "přehled prostředí: verze, terminál, profil -- vlož do hlášení chyby",

"ui help.desc.export": "ulož postup tohoto profilu do přenosného souboru",

"ui help.desc.goto": "skoč na úkol (goto 2.4, nebo goto 2 pro kapitolu 2; samotné otevře výběr)",

"ui help.desc.help": "zobraz tento seznam příkazů",

"ui help.desc.hint": "odhal další radu",

"ui help.desc.import": "načti profil z exportovaného souboru",

"ui help.desc.map": "strom kapitol a úloh (map all rozbalí vyřešené kapitoly)",

"ui help.desc.menu": "otevři hlavní menu (začni tady, nebo se vrať z úkolu)",

"ui help.desc.mode": "nastav obtížnost: easy | normal | hard",

"ui help.desc.next": "pokračuj dál, jakmile je úkol vyřešený",

"ui help.desc.note": "připiš si k úkolu osobní poznámku (samotné note ji zobrazí, note clear ji smaže)",

"ui help.desc.restart": "začni úkol znovu: prázdný kód + smazání postupu (retry ho nechá vyřešený)",

"ui help.desc.resume": "skoč na první nevyřešený úkol",

"ui help.desc.retry": "vyprázdni pracovní soubor a procvičuj znovu (zůstane vyřešený)",

"ui help.desc.search": "najdi úkol podle slova v názvu nebo konceptu",

"ui help.desc.setup": "nastav krátké příkazy (nabízí lokální nebo trvalé)",

"ui help.desc.skip": "vzdej to a pokračuj bez vyřešení (ne v těžkém režimu)",

"ui help.desc.solution": "zobraz vzorové řešení",

"ui help.desc.stats": "tvá čísla: pokusy, rady, dokončení po kapitolách",

"ui help.desc.status": "zobraz postup a aktuální úkol",

"ui help.desc.textbook": "syntaxe a tipy, kam jsi došel (textbook all: vše · textbook <kapitola|slovo>: výsek)",

"ui help.desc.theme": "přepni barevné téma (neon, amber, forest, mono, nebo preset z themes/)",

"ui help.desc.uninstall": "odeber trvalé zkratky",

"ui help.desc.user": "přepni nebo vytvoř profil",

"ui help.desc.wipe": "smazání postupu: tento profil (wipe profile), nebo všechny profily i nastavení (wipe everything, vyžádá si napsat ERASE)",

"ui help.footer": "%s k dispozici teď   %s vyžaduje načtený úkol",

"ui help.group_always": "kdekoli",

"ui help.group_puzzle": "při řešení úkolu",

"ui help.in_puzzle": "v úkolu %s",

"ui help.load_first": "nejdřív načti úkol (%s)",

"ui help.no_loaded": "žádný úkol není načtený",

"ui help.title": "přehled příkazů",

"ui hint.hard_locked": "Těžký režim: rady se odemknou po 3 pokusech (zatím %d).",

"ui hint.more": "spusť hint znovu pro další",

"ui hint.no_more": "Žádné další rady. Zkus:  %s",

"ui hint.none": "K tomuto úkolu nejsou žádné rady.",

"ui hint.title": "rada  %d / %d · %s",

"ui jump.locked": "'%s' je zamčený.",

"ui jump.locked_2": "V režimu %s se můžeš vracet jen k odemčeným úkolům.",

"ui jump.locked_3": "Použij %s pro postup o jeden, nebo přepni na easy režim.",

"ui jump.now_on": "Teď na %s -- %s%s",

"ui jump.restored": "  (tvůj uložený kód byl obnoven)",

"ui keys.arrows": "šipky pohyb",

"ui keys.enter": "Enter vybere",

"ui keys.esc": "Esc zpět",

"ui keys.filter": "piš pro filtrování",

"ui keys.filter_matches": "%d z %d odpovídá · Enter vybere",

"ui keys.no_filter_match": "nic neodpovídá -- Backspace upraví, Enter odešle text, Esc zpět",

"ui keys.position": "%d z %d",

"ui keys.type": "piš pro zadání",

"ui lang.picker_title": "jazyk",

"ui lang.prompt": "kód jazyka  (0 = zpět) > ",

"ui lang.set": "jazyk nastaven na %s.",

"ui map.folded": "všech %d vyřešeno -- rozbal pomocí  %s",

"ui map.title": "mapa",

"ui menu.footer_compact": "šipky vybírají · Enter spustí · napiš příkaz",

"ui menu.footer_full": "šipky pohyb · Enter vybírá · napiš příkaz · help",

"ui menu.learn": "učit se",

"ui menu.level_prompt": "id  (0 = zpět) > ",

"ui menu.level_title": "vyber úroveň",

"ui menu.main_title": "hlavní menu",

"ui menu.note.map": "strom kapitol / úkolů",

"ui menu.note.select": "skoč na libovolný úkol",

"ui menu.note.settings": "téma · režim · profily · zkratky",

"ui menu.note.stats": "pokusy · rady · tempo",

"ui menu.note.textbook": "syntaxe a tipy zatím",

"ui menu.note.textbook_sealed": "zapečetěno v těžkém režimu",

"ui menu.play": "hrát",

"ui menu.see_you": "uvidíme se v terminálu -- řeš pomocí  ",

"ui menu.setup": "nastavit",

"ui menu.tty_only": "(spusť v terminálu pro výběr)",

"ui menu.type_number": "napiš číslo 0-6, nebo příkaz.",

"ui menu.verb_needs_puzzle": "'%s' běží v terminálu, jakmile je úkol otevřený.",

"ui menu.verb_needs_puzzle_2": "Vyber %s pro start, pak ulož work.py a spusť  %s",

"ui menu.verb_terminal": "'%s' je příkaz terminálu, ne položka menu.",

"ui menu.verb_terminal_2": "Opusť menu (%s) a spusť  %s",

"ui mode.current": "Aktuální režim: %s",

"ui mode.desc_easy": "Ukazatele zobrazené, rady/řešení vždy k dispozici, volné skoky.",

"ui mode.desc_hard": "Žádné přeskoky; rady po 3 pokusech; řešení po vyřešení; učebnice zapečetěná.",

"ui mode.desc_normal": "Rady na vyžádání, přeskok vpřed povolen.",

"ui mode.picker_title": "obtížnost",

"ui mode.prompt": "easy / normal / hard  (0 = zpět) > ",

"ui mode.set": "Režim nastaven na '%s'.",

"ui mode.usage": "Použití: %s",

"ui nav.hard_skip": "Přepni na snazší režim pro přeskočení:  %s",

"ui nav.hard_solve": "Těžký režim: než půjdeš dál, musíš vyřešit %s.",

"ui nav.last_puzzle": "To byl poslední úkol v kurzu.",

"ui nav.moved_on": "Posunul ses z",

"ui nav.not_solved": "%s ještě není vyřešený.",

"ui nav.not_solved_2": "Spouštěj %s, dokud neprojde, nebo %s pro posun bez vyřešení.",

"ui nav.skipped": "Přeskočeno (nevyřešeno)",

"ui note.add_one": "přidej ji pomocí  ",

"ui note.cleared": "Poznámka smazána u %s.",

"ui note.header": "poznámka u %s:",

"ui note.none_clear": "u %s není žádná poznámka ke smazání.",

"ui note.none_yet": "u %s zatím není žádná poznámka.",

"ui note.saved": "Poznamenáno u %s.",

"ui profiles.arrow_hint": "šipkou na jméno pro přepnutí · nebo napiš 'rename a b' / 'delete a'",

"ui profiles.new_entry": "+ nový profil",

"ui profiles.new_prompt": "jméno nového profilu  (prázdné = zrušit) >",

"ui profiles.prompt": "jméno pro přepnutí · 'rename a b' · 'delete a'  (0 = zpět) > ",

"ui profiles.title": "profily",

"ui restart.done": "Restartováno %s -- prázdný pracovní soubor, postup smazán.",

"ui resume.all_solved": "Všechny úkoly jsou vyřešené -- není kam navázat.",

"ui resume.at": "Navazuji u %s.",

"ui resume.revisit": "vrať se k libovolnému pomocí  ",

"ui retry.reload": "pokud editor pořád ukazuje starý kód, znovu načti work.py -- jeho kopie na disku je teď prázdná.",

"ui retry.reset": "Vynulováno %s na prázdný pracovní soubor -- zkus to znovu.",

"ui retry.stays_solved": "(zůstává označený jako vyřešený; tohle je jen procvičování)",

"ui search.broaden": "zkus obecnější slovo, nebo prolistuj  ",

"ui search.matches.few": "%d shody -- otevři jednu pomocí  %s",

"ui search.matches.one": "%d shoda -- otevři jednu pomocí  %s",

"ui search.matches.other": "%d shod -- otevři jednu pomocí  %s",

"ui search.no_match": "žádný úkol neodpovídá '%s'.",

"ui search.title": "hledat · %s",

"ui search.usage": "použití:  ",

"ui search.usage_hint": "Najdi úkol podle slova v jeho názvu nebo konceptu.",

"ui session.no_shell": r"""Otevírám menu. (Nepodařilo se nastavit krátké příkazy pro tento
shell; pořád můžeš spustit `%s start.py <příkaz>`.)
""",

"ui session.starting": "Spouštím PyQuest s krátkými příkazy pro tuto relaci.",

"ui session.when_done": r"""Až skončíš, napiš  exit  pro opuštění relace PyQuest.
""",

"ui settings.persistent": "trvalé: %s",

"ui settings.title": "nastavení",

"ui settings.type_hint": "napiš theme / mode / profiles / shortcuts / language, nebo Esc.",

"ui settings.type_number": "napiš 1-5, nebo 0 pro návrat.",

"ui setup.activate_now": "Aktivuj teď:  %s",

"ui setup.already": "Už zapnuto v %s.",

"ui setup.enable_title": "zapni krátké příkazy",

"ui setup.enabled": "Zkratky zapnuty v %s.",

"ui setup.f_python": "python",

"ui setup.f_status": "stav",

"ui setup.missing": "%s chybí -- nelze nainstalovat.",

"ui setup.none": "Žádné trvalé zkratky v %s.",

"ui setup.opt_a": "A) jen tento terminál",

"ui setup.opt_b": "B) každý terminál",

"ui setup.persist_off": "zkratky nejsou trvale nainstalované",

"ui setup.persist_on": "trvalé zkratky zapnuté v %s",

"ui setup.remove_later": "později odeber pomocí  python3 start.py uninstall",

"ui setup.removed": "Odebrány zkratky PyQuestu z %s.",

"ui setup.run": "spusť:  ",

"ui setup.skip": "nebo zkratky úplně vynech -- python3 start.py … funguje vždy.",

"ui setup.title": "nastavení zkratek",

"ui setup.uninstall_note": "Nové terminály zkratky nenačtou. Tento terminál si je drží, dokud",

"ui setup.uninstall_note_2": "ho nezavřeš -- nebo nespustíš:  %s",

"ui shortcuts.disc_funcs": "Jsou to shellové funkce definované v %s (check, hint, start, …).",

"ui shortcuts.disc_local": "Lokální = nic mimo tuto složku se nemění.  Trvalé = jeden řádek ve startovacím souboru shellu.",

"ui shortcuts.disc_post": "  místo  python3 start.py check.",

"ui shortcuts.disc_pre": "Zkratky ti umožní psát  ",

"ui shortcuts.opt_local": "zapni pro TENTO terminál (lokálně, nic se neukládá)",

"ui shortcuts.opt_persist": "nainstaluj trvale (jeden řádek do startovacího souboru)",

"ui shortcuts.opt_uninstall": "odinstaluj (odeber trvalý řádek)",

"ui shortcuts.run_yourself": "Spusť si to sám (program neumí source do tvého shellu):",

"ui shortcuts.title": "zkratky",

"ui solution.hard_locked": "Těžký režim: řešení se odemkne až po vyřešení.",

"ui solution.none": "K tomuto úkolu není soubor s řešením.",

"ui solution.title": "řešení · %s · %s",

"ui solution.why": "proč to funguje",

"ui stats.all_solved.few": "vyřešeny %d úkoly -- %d napoprvé, bez nápověd.",

"ui stats.all_solved.one": "vyřešen %d úkol -- %d napoprvé, bez nápověd.",

"ui stats.all_solved.other": "vyřešeno %d úkolů -- %d napoprvé, bez nápověd.",

"ui stats.by_chapter": "po kapitolách",

"ui stats.clean_tail": "vyřešeno napoprvé, bez nápověd",

"ui stats.course_complete": "kurz dokončen",

"ui stats.f_active": "aktivní",

"ui stats.f_clean": "čistě",

"ui stats.f_hints": "rady",

"ui stats.f_pace": "tempo",

"ui stats.f_since": "od",

"ui stats.f_solved": "vyřešeno",

"ui stats.f_streak": "série",

"ui stats.f_today": "dnes",

"ui stats.f_tries": "pokusy",

"ui stats.hints_tail": "odhalených rad",

"ui stats.in_a_row": "v řadě",

"ui stats.last_14": "vyřešené, posledních 14 dní",

"ui stats.streak.few": "%d dny",

"ui stats.streak.one": "%d den",

"ui stats.streak.other": "%d dní",

"ui stats.title": "statistiky · %s",

"ui stats.today_tail": "vyřešeno dnes",

"ui stats.tries_tail": "spuštění kontroly přes všechny úkoly",

"ui stats.x_of_y": "%d z %d",

"ui status.all_complete.few": "%s  Hotové %d úkoly.",

"ui status.all_complete.one": "%s  Hotový %d úkol.",

"ui status.all_complete.other": "%s  Hotových %d úkolů.",

"ui status.no_current": "Žádný aktuální úkol.  ",

"ui status.no_loaded": "Žádný úkol není načtený.",

"ui status.open_menu": "Otevři menu, vyber úroveň a začni:  ",

"ui status.revisit_goto": "vrať se k libovolnému pomocí  goto <id>",

"ui textbook.f_read": "čti",

"ui textbook.hard_sealed": "Těžký režim: učebnice je zapečetěná -- pracuj ze zadání.",

"ui textbook.md_chapter": "Kapitola %d · %s",

"ui textbook.md_empty": "Zatím nic probráno -- projdi pár témat, nebo spusť `textbook all` pro náhled celého jazyka.",

"ui textbook.md_full_1": "Celý jazyk, který PyQuest pokrývá -- každá kapitola, všech %d témat.",

"ui textbook.md_full_2": "Spusť `textbook` pro návrat jen ke kapitolám, ke kterým ses dostal.",

"ui textbook.md_reached_1": "Technická reference k tomu, ke kterému ses dostal -- %d z %d témat.",

"ui textbook.md_reached_2": "Spusť `textbook all` pro celý jazyk; `textbook` tě vrátí sem.",

"ui textbook.md_title": "Učebnice PyQuest",

"ui textbook.md_topic": "Jen %s. Spusť `textbook` pro vše, kam jsi došel, `textbook all` pro celý jazyk.",

"ui textbook.no_topic": "žádná kapitola ani téma neodpovídá '%s'.",

"ui textbook.open_it": "otevři ji v editoru",

"ui textbook.ready": "Učebnice připravena: %s.",

"ui textbook.revert": "vrať se jen k tomu, ke kterému ses dostal:  ",

"ui textbook.scope_chapter": "kapitola %s",

"ui textbook.see_all": "zobraz celý jazyk:  ",

"ui textbook.topic_hint": "zkus číslo kapitoly nebo slovo:",

"ui textbook.where_full": "úplná reference",

"ui textbook.where_none": "zatím nic dosaženo",

"ui textbook.where_reached": "to, ke kterému ses dostal -- %d z %d",

"ui textbook.where_topic.few": "%s -- %d témata",

"ui textbook.where_topic.one": "%s -- %d téma",

"ui textbook.where_topic.other": "%s -- %d témat",

"ui theme.add_own": "přidej si vlastní: vlož JSON soubor do themes/ (viz themes/README.md)",

"ui theme.list_title": "témata",

"ui theme.picker_title": "téma",

"ui theme.prompt": "název tématu  (0 = zpět) > ",

"ui theme.set": "téma nastaveno na '%s'.",

"ui theme.set_with": "nastav pomocí  ",

"ui theme.unknown": "neznámé téma '%s'. možnosti: %s",

"ui transfer.answers.few": "%d uložené odpovědi",

"ui transfer.answers.one": "%d uložená odpověď",

"ui transfer.answers.other": "%d uložených odpovědí",

"ui transfer.dropped.few": "poznámka: %d dokončená id nejsou v obsahu této verze a byla vynechána.",

"ui transfer.dropped.one": "poznámka: %d dokončené id není v obsahu této verze a bylo vynecháno.",

"ui transfer.dropped.other": "poznámka: %d dokončených id není v obsahu této verze a bylo vynecháno.",

"ui transfer.exists_hint": "Importuj pod novým jménem, nebo ho přepiš:",

"ui transfer.exported": "Profil '%s' exportován do %s.",

"ui transfer.import_usage_hint": "Importuje profil exportovaný pomocí  %s.",

"ui transfer.imported": "Importováno do profilu '%s' (nyní aktivní).",

"ui transfer.move_hint": "Přenes to na jiný počítač, pak:  %s",

"ui transfer.no_file": "Soubor neexistuje: %s",

"ui transfer.not_export": "%s není exportní soubor PyQuestu.",

"ui transfer.pass_name": "Zadej platné jméno:  %s",

"ui transfer.puzzles.few": "%d dokončené úkoly",

"ui transfer.puzzles.one": "%d dokončený úkol",

"ui transfer.puzzles.other": "%d dokončených úkolů",

"ui transfer.read_fail": "Nepodařilo se přečíst %s jako export PyQuestu.",

"ui transfer.summary": "%s, %s.",

"ui transfer.write_fail": "Nepodařilo se zapsat %s (%s).",

"ui ui.back": "zpět",

"ui ui.legend": "%s hotovo   %s tady   %s zbývá",

"ui ui.mode": "režim",

"ui ui.no_current": "Žádný aktuální úkol.",

"ui ui.no_puzzle": "žádný úkol '%s'.",

"ui ui.off": "vyp",

"ui ui.on": "zap",

"ui ui.usage": "použití:  ",

"ui user.already_on": "už jsi na '%s'.",

"ui user.created_switched": "vytvořen a přepnuto na",

"ui user.deleted": "Smazán profil '%s' a celý jeho postup.",

"ui user.exists": "Profil '%s' už existuje.",

"ui user.invalid_name": "'%s' nemůže být jméno profilu.",

"ui user.is_active": "'%s' je aktivní profil.",

"ui user.list_title": "uživatelé",

"ui user.manage": "přejmenuj  %s      smaž  %s",

"ui user.manage_hint": "Pro správu profilů:  %s  ·  %s",

"ui user.name_rules": "Používej jen písmena, číslice, pomlčky nebo podtržítka (až 32 znaků).",

"ui user.name_rules_1": "Jména se stanou složkami v users/, takže používej jen písmena,",

"ui user.name_rules_2": "číslice, pomlčky nebo podtržítka (až 32 znaků).",

"ui user.no_profile": "Žádný profil '%s'.",

"ui user.no_spaces": "'%s' nemůže být jméno profilu (bez mezer).",

"ui user.renamed": "Přejmenováno '%s' na '%s'.",

"ui user.same_name": "'%s' už se tak jmenuje.",

"ui user.switch_create": "přepni nebo vytvoř pomocí  ",

"ui user.switch_first": "Nejdřív přepni na jiný:  %s",

"ui user.switched_to": "přepnuto na",

"ui wipe.all_cancelled": "Zrušeno -- nic nebylo smazáno.",

"ui wipe.all_done": "Vše smazáno -- všechny profily odstraněny.",

"ui wipe.all_fresh": "PyQuest je jako čerstvě nainstalovaný; příští spuštění začne od nuly.",

"ui wipe.all_hint": "(smazat všechny profily a začít od nuly:  %s)",

"ui wipe.all_how": "Napiš %s (přesně) pro potvrzení; cokoli jiného akci zruší.",

"ui wipe.all_tty_only": "Spusť to v terminálu -- vyžaduje napsané potvrzení.",

"ui wipe.all_warn": "Tohle smaže VŠECHNY profily této instalace --",

"ui wipe.all_warn_2": "veškerý postup, uložený kód, poznámky i nastavení (téma, jazyk).",

"ui wipe.cleared": "Smazán postup tohoto profilu, uložený kód i pracovní soubor.",

"ui wipe.confirm_hint": "Nelze to vrátit. Pokud chceš pokračovat:  %s",

"ui wipe.done": "Profil vymazán.",

"ui wipe.open_menu": "Otevři menu a začni znovu:  %s",

"ui wipe.restart_hint": "(pro smazání jen aktuálního úkolu použij  %s)",

"ui wipe.warn": "Tohle smaže VŠECHNO v profilu '%s' --",

"ui wipe.warn_2": "každý dokončený úkol, veškerý uložený kód i pracovní soubor.",
}
