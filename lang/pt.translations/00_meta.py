# PyQuest translations -- language 'pt' -- pack name + UI strings.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"name": "Português",

"ui app.no_loaded_menu": "Ainda não há nenhum puzzle carregado -- aqui está o menu.",

"ui app.no_puzzles": "Não foram encontrados puzzles em %s",

"ui app.open_menu_status": r"""Abre o menu para te configurares e escolheres um nível:  %s
""",

"ui app.run_full_list": "corre  %s  para a lista completa.",

"ui app.setup_below": r"""Configura-te e escolhe um nível no menu abaixo.
""",

"ui app.unknown": "Comando desconhecido '%s'.",

"ui app.unknown_suggest": "Comando desconhecido '%s'. Querias dizer  %s ?",

"ui app.welcome": "Bem-vindo ao PyQuest!",

"ui card.chapter": "capítulo %d · %s",

"ui card.f_edit": "editar",

"ui card.f_read": "ler",

"ui card.hint_lead": "dica  ",

"ui card.locked": "bloqueado",

"ui card.note_lead": "nota  ",

"ui card.save_before": "(guarda antes de verificar)",

"ui card.solved": "resolvido",

"ui check.banner_not_yet": "ainda não",

"ui check.banner_so_close": "quase lá",

"ui check.banner_solved": "resolvido",

"ui check.bonus_default": "isto funciona, mas podia ser mais eficiente",

"ui check.bonus_no": "bónus: ainda não é o ideal — %s",

"ui check.bonus_yes": "bónus: ideal — solução eficiente",

"ui check.code_saved": "o teu código está guardado.",

"ui check.crash_body": r"""O Python levantou um erro%s:

%s

Lê o nome do erro: indica o que correu mal.

%s
""",

"ui check.crash_title": "Falha -- o teu código começou mas encontrou um erro",

"ui check.crash_title2": "Falha -- o teu código encontrou um erro",

"ui check.expected": "Esperado:",

"ui check.got": "Obtido:",

"ui check.lesson_body": r"""O teu resultado está correto -- mas este puzzle não é sobre a resposta em si.
Ensina uma ferramenta específica, e a tua solução chegou ao resultado
de outra forma, pelo que a lição acabou por ser evitada.
""",

"ui check.lesson_rework": "Refaz para usares o que o puzzle ensina, depois verifica outra vez.",

"ui check.lesson_title": "Resposta correta -- mas não é a lição deste puzzle",

"ui check.lesson_wants": "Este puzzle pretende:",

"ui check.missing_body": r"""O teu ficheiro não define `%s`.

Verifica a ortografia, ou adiciona-o. Para uma função, o enunciado pede
`%s`, define-a com:  def %s(...):
""",

"ui check.missing_title": "Falta uma peça -- ainda não está definido algo",

"ui check.next": "seguinte",

"ui check.no_loaded": "Nenhum puzzle carregado.",

"ui check.nudge_hard": "Modo difícil: as dicas desbloqueiam-se ao fim de 3 tentativas (%d até agora).",

"ui check.nudge_hints": "Já há dicas disponíveis:  %s",

"ui check.nudge_stuck": "Encravado?  %s",

"ui check.retry": "repetir",

"ui check.retry_hint": "para o limpar e resolver de novo do zero",

"ui check.save_tip": r"""Guardaste o work.py no teu editor? Alterações não guardadas são a causa
número um de uma verificação que "devia" passar mas não passa.
""",

"ui check.start_first": "Começa primeiro um:  ",

"ui check.syntax_body": r"""O Python parou em %s

Isto costuma significar um erro de digitação: falta uma aspa, um parêntese,
dois pontos, ou a indentação está errada. Abre o work.py e verifica essa linha.
""",

"ui check.syntax_title": "Erro de sintaxe -- o Python não conseguiu ler o teu ficheiro",

"ui check.tests_unloadable": r"""Interno: não foi possível carregar os testes deste puzzle.
""",

"ui check.was_last": "esse foi o último puzzle do curso.",

"ui check.wrong_title": "Resultado errado -- o código corre mas a resposta está incorreta",

"ui check.your_code": "O teu código:",

"ui cockpit.footer": "setas movem · Enter corre · escreve um verbo · Esc para o shell",

"ui date.today": "hoje",

"ui date.yesterday": "ontem",

"ui goto.footer": "corre  %s   ex.  %s   (um número de capítulo simples também funciona: %s)",

"ui goto.no_match": "Não existe nenhum puzzle '%s'. Escolhe um destes:",

"ui goto.prompt": "id (em branco = cancelar) > ",

"ui goto.title": "ir para · escolhe um puzzle",

"ui help.available_now": "disponível agora",

"ui help.footer": "%s disponível agora   %s precisa de um puzzle carregado",

"ui help.group_always": "em qualquer lado",

"ui help.group_puzzle": "a resolver um puzzle",

"ui help.in_puzzle": "no puzzle %s",

"ui help.load_first": "carrega primeiro um puzzle (%s)",

"ui help.no_loaded": "nenhum puzzle carregado",

"ui help.title": "referência de comandos",

"ui hint.hard_locked": "Modo difícil: as dicas desbloqueiam-se ao fim de 3 tentativas (%d até agora).",

"ui hint.more": "corre hint outra vez para mais",

"ui hint.no_more": "Não há mais dicas. Tenta:  %s",

"ui hint.none": "Sem dicas para este puzzle.",

"ui hint.title": "dica  %d / %d · %s",

"ui jump.locked": "'%s' está bloqueado.",

"ui jump.locked_2": "No modo %s só podes revisitar puzzles desbloqueados.",

"ui jump.locked_3": "Usa %s para avançar um, ou muda para o modo fácil.",

"ui jump.now_on": "Agora em %s -- %s%s",

"ui jump.restored": "  (o teu código guardado foi restaurado)",

"ui keys.arrows": "setas movem",

"ui keys.enter": "Enter seleciona",

"ui keys.esc": "Esc voltar",

"ui keys.position": "%d de %d",

"ui keys.type": "escreve para entrar num",

"ui lang.picker_title": "idioma",

"ui lang.prompt": "código do idioma  (0 = voltar) > ",

"ui lang.set": "idioma definido para %s.",

"ui map.title": "mapa",

"ui menu.footer_compact": "setas selecionam · Enter corre · escreve um verbo",

"ui menu.footer_full": "setas movem · Enter escolhe · escreve um verbo · help",

"ui menu.learn": "aprender",

"ui menu.level_prompt": "id  (0 = voltar) > ",

"ui menu.level_title": "seleciona o nível",

"ui menu.main_title": "menu principal",

"ui menu.note.map": "a árvore de capítulos / puzzles",

"ui menu.note.select": "salta para qualquer puzzle",

"ui menu.note.settings": "tema · modo · perfis · atalhos",

"ui menu.note.stats": "tentativas · dicas · ritmo",

"ui menu.note.textbook": "sintaxe e dicas até agora",

"ui menu.note.textbook_sealed": "selado no modo difícil",

"ui menu.play": "jogar",

"ui menu.see_you": "até já no terminal -- resolve com  ",

"ui menu.setup": "configurar",

"ui menu.tty_only": "(corre isto num terminal para escolher)",

"ui menu.type_number": "escreve um número de 0 a 6, ou um comando.",

"ui menu.verb_needs_puzzle": "'%s' corre no teu terminal, assim que um puzzle estiver aberto.",

"ui menu.verb_needs_puzzle_2": "Escolhe %s para começar, depois guarda o work.py e corre  %s",

"ui menu.verb_terminal": "'%s' é um comando de terminal, não uma opção do menu.",

"ui menu.verb_terminal_2": "Sai do menu (%s) e corre  %s",

"ui mode.current": "Modo atual: %s",

"ui mode.desc_easy": "Pistas mostradas, dicas/solução sempre disponíveis, saltos livres.",

"ui mode.desc_hard": "Sem saltar; dicas ao fim de 3 tentativas; solução depois de resolver; manual selado.",

"ui mode.desc_normal": "Dicas disponíveis a pedido, avançar é permitido.",

"ui mode.picker_title": "dificuldade",

"ui mode.prompt": "fácil / normal / difícil  (0 = voltar) > ",

"ui mode.set": "Modo definido para '%s'.",

"ui mode.usage": "Utilização: %s",

"ui nav.hard_skip": "Muda para um modo mais fácil para saltar:  %s",

"ui nav.hard_solve": "Modo difícil: tens de resolver %s antes de avançar.",

"ui nav.last_puzzle": "Esse foi o último puzzle do curso.",

"ui nav.moved_on": "Avançaste de",

"ui nav.not_solved": "%s ainda não está resolvido.",

"ui nav.not_solved_2": "Corre %s até passar, ou %s para avançar sem resolver.",

"ui nav.skipped": "Saltado (não resolvido)",

"ui note.add_one": "adiciona uma com  ",

"ui note.cleared": "Nota apagada em %s.",

"ui note.header": "nota em %s:",

"ui note.none_clear": "não há nota em %s para apagar.",

"ui note.none_yet": "ainda não há nota em %s.",

"ui note.saved": "Anotado em %s.",

"ui profiles.arrow_hint": "usa as setas até um nome para mudar · '+ new profile' para criar · ou escreve 'rename a b' / 'delete a'",

"ui profiles.new_entry": "+ novo perfil",

"ui profiles.new_prompt": "nome do novo perfil  (em branco = cancelar) > ",

"ui profiles.prompt": "nome para mudar/criar · 'rename a b' · 'delete a'  (0 = voltar) > ",

"ui profiles.title": "perfis",

"ui restart.done": "Reiniciado %s -- área de trabalho em branco, progresso apagado.",

"ui resume.all_solved": "Todos os puzzles estão resolvidos -- nada para retomar.",

"ui resume.at": "A retomar em %s.",

"ui resume.revisit": "revisita qualquer um com  ",

"ui retry.reload": "se o teu editor ainda mostrar código antigo, recarrega o work.py -- a cópia em disco está agora em branco.",

"ui retry.reset": "Repõe %s numa área de trabalho em branco -- tenta outra vez.",

"ui retry.stays_solved": "(continua marcado como resolvido; isto é só prática)",

"ui search.broaden": "tenta uma palavra mais genérica, ou navega pelo  ",

"ui search.no_match": "nenhum puzzle corresponde a '%s'.",

"ui search.title": "procurar · %s",

"ui search.usage": "utilização:  ",

"ui search.usage_hint": "Encontra um puzzle por uma palavra no título ou conceito.",

"ui session.no_shell": r"""A abrir o menu. (Não foi possível configurar os atalhos para este
shell; ainda podes correr `%s start.py <comando>`.)
""",

"ui session.starting": "A iniciar o PyQuest com os atalhos ativos para esta sessão.",

"ui session.when_done": r"""Quando terminares, escreve  exit  para sair da sessão do PyQuest.
""",

"ui settings.persistent": "persistente: %s",

"ui settings.title": "definições",

"ui settings.type_hint": "escreve theme / mode / profiles / shortcuts / language, ou Esc.",

"ui settings.type_number": "escreve 1-5, ou 0 para voltar.",

"ui setup.activate_now": "Ativa agora:  %s",

"ui setup.already": "Já ativado em %s.",

"ui setup.enable_title": "ativar os atalhos",

"ui setup.enabled": "Atalhos ativados em %s.",

"ui setup.f_python": "python",

"ui setup.f_status": "estado",

"ui setup.missing": "%s está em falta -- não é possível instalar.",

"ui setup.none": "Nenhum atalho persistente em %s.",

"ui setup.opt_a": "A) só este terminal",

"ui setup.opt_b": "B) todos os terminais",

"ui setup.persist_off": "atalhos não instalados de forma persistente",

"ui setup.persist_on": "atalhos persistentes ativados em %s",

"ui setup.remove_later": "remove mais tarde com  python3 start.py uninstall",

"ui setup.removed": "Atalhos do PyQuest removidos de %s.",

"ui setup.run": "corre:  ",

"ui setup.skip": "ou salta os atalhos por completo -- python3 start.py … funciona sempre.",

"ui setup.title": "configuração",

"ui setup.uninstall_note": "Novos terminais não vão carregar os atalhos. Este terminal mantém-nos até",

"ui setup.uninstall_note_2": "o fechares -- ou corres:  %s",

"ui shortcuts.disc_funcs": "São funções de shell definidas em %s (check, hint, start, …).",

"ui shortcuts.disc_local": "Local = nada fora desta pasta muda.  Persistente = uma linha no ficheiro de arranque do teu shell.",

"ui shortcuts.disc_post": "  em vez de  python3 start.py check.",

"ui shortcuts.disc_pre": "Os atalhos deixam-te escrever  ",

"ui shortcuts.opt_local": "ativar só para ESTE terminal (local, nada é guardado)",

"ui shortcuts.opt_persist": "instalar de forma persistente (uma linha no teu ficheiro de arranque)",

"ui shortcuts.opt_uninstall": "desinstalar (remover a linha persistente)",

"ui shortcuts.run_yourself": "Corre isto tu mesmo (um programa não se consegue integrar no teu shell):",

"ui shortcuts.title": "atalhos",

"ui solution.hard_locked": "Modo difícil: a solução só se desbloqueia depois de a resolveres.",

"ui solution.none": "Sem ficheiro de solução para este puzzle.",

"ui solution.title": "solução · %s · %s",

"ui solution.why": "porque funciona",

"ui stats.by_chapter": "por capítulo",

"ui stats.clean_tail": "resolvido à primeira, sem dicas",

"ui stats.course_complete": "curso completo",

"ui stats.f_active": "ativo",

"ui stats.f_clean": "limpo",

"ui stats.f_hints": "dicas",

"ui stats.f_since": "desde",

"ui stats.f_solved": "resolvidos",

"ui stats.f_streak": "sequência",

"ui stats.f_today": "hoje",

"ui stats.f_tries": "tentativas",

"ui stats.hints_tail": "dicas reveladas",

"ui stats.in_a_row": "seguidos",

"ui stats.title": "estatísticas · %s",

"ui stats.today_tail": "resolvidos hoje",

"ui stats.tries_tail": "execuções de check em todos os puzzles",

"ui stats.x_of_y": "%d de %d",

"ui status.no_current": "Nenhum puzzle atual.  ",

"ui status.no_loaded": "Nenhum puzzle carregado.",

"ui status.open_menu": "Abre o menu para escolher um nível e começar:  ",

"ui status.revisit_goto": "revisita qualquer um com  goto <id>",

"ui textbook.f_read": "ler",

"ui textbook.hard_sealed": "Modo difícil: o manual está selado -- trabalha a partir do enunciado.",

"ui textbook.md_chapter": "Capítulo %d · %s",

"ui textbook.md_empty": "Ainda não foi abordado nada -- avança por alguns temas, ou corre `textbook all` para pré-ver toda a linguagem.",

"ui textbook.md_full_1": "Toda a linguagem que o PyQuest cobre -- todos os capítulos, os %d temas.",

"ui textbook.md_full_2": "Corre `textbook` para voltar só aos capítulos que já alcançaste.",

"ui textbook.md_reached_1": "Uma referência técnica para o que já alcançaste -- %d de %d temas.",

"ui textbook.md_reached_2": "Corre `textbook all` para a linguagem completa; `textbook` traz-te de volta aqui.",

"ui textbook.md_title": "Manual do PyQuest",

"ui textbook.open_it": "abre-o no teu editor",

"ui textbook.ready": "Manual pronto: %s.",

"ui textbook.revert": "volta só ao que já alcançaste:  ",

"ui textbook.see_all": "vê a linguagem completa:  ",

"ui textbook.where_full": "a referência completa",

"ui textbook.where_none": "ainda nada alcançado",

"ui textbook.where_reached": "o que já alcançaste -- %d de %d",

"ui theme.add_own": "adiciona o teu: coloca um ficheiro JSON em themes/ (vê themes/README.md)",

"ui theme.list_title": "temas",

"ui theme.picker_title": "tema",

"ui theme.prompt": "nome do tema  (0 = voltar) > ",

"ui theme.set": "tema definido para '%s'.",

"ui theme.set_with": "define com  ",

"ui theme.unknown": "tema desconhecido '%s'. opções: %s",

"ui transfer.exists_hint": "Importa com um nome novo, ou substitui-o:",

"ui transfer.exported": "Perfil '%s' exportado para %s.",

"ui transfer.import_usage_hint": "Importa um perfil exportado com  %s.",

"ui transfer.imported": "Importado para o perfil '%s' (agora ativo).",

"ui transfer.move_hint": "Move-o para outra máquina, depois:  %s",

"ui transfer.no_file": "Não existe o ficheiro: %s",

"ui transfer.not_export": "%s não é um ficheiro de exportação do PyQuest.",

"ui transfer.pass_name": "Indica um nome válido:  %s",

"ui transfer.read_fail": "Não foi possível ler %s como uma exportação do PyQuest.",

"ui transfer.summary": "%s, %s.",

"ui transfer.write_fail": "Não foi possível escrever %s (%s).",

"ui ui.back": "voltar",

"ui ui.legend": "%s feito   %s aqui   %s por fazer",

"ui ui.mode": "modo",

"ui ui.no_current": "Nenhum puzzle atual.",

"ui ui.no_puzzle": "nenhum puzzle '%s'.",

"ui ui.off": "desligado",

"ui ui.on": "ligado",

"ui ui.usage": "utilização:  ",

"ui user.already_on": "já está em '%s'.",

"ui user.created_switched": "criado e mudado para",

"ui user.deleted": "Perfil '%s' e todo o seu progresso foram apagados.",

"ui user.exists": "O perfil '%s' já existe.",

"ui user.invalid_name": "'%s' não pode ser o nome de um perfil.",

"ui user.is_active": "'%s' é o perfil ativo.",

"ui user.list_title": "perfis",

"ui user.manage": "renomear  %s      apagar  %s",

"ui user.manage_hint": "Para gerir perfis:  %s  ·  %s",

"ui user.name_rules": "Usa só letras, dígitos, traços ou sublinhados (até 32 caracteres).",

"ui user.name_rules_1": "Os nomes tornam-se pastas dentro de users/, por isso usa só letras,",

"ui user.name_rules_2": "dígitos, traços ou sublinhados (até 32 caracteres).",

"ui user.no_profile": "Não existe o perfil '%s'.",

"ui user.no_spaces": "'%s' não pode ser o nome de um perfil (sem espaços).",

"ui user.renamed": "'%s' renomeado para '%s'.",

"ui user.same_name": "'%s' já é o nome atual.",

"ui user.switch_create": "muda ou cria com  ",

"ui user.switch_first": "Muda primeiro para outro:  %s",

"ui user.switched_to": "mudado para",

"ui wipe.cleared": "Progresso, código guardado e área de trabalho deste perfil foram apagados.",

"ui wipe.confirm_hint": "Não pode ser desfeito. Para continuar:  %s",

"ui wipe.done": "Perfil apagado.",

"ui wipe.open_menu": "Abre o menu para começar de novo:  %s",

"ui wipe.restart_hint": "(para apagar só o puzzle atual, usa  %s)",

"ui wipe.warn": "Isto apaga TUDO no perfil '%s' --",

"ui wipe.warn_2": "cada puzzle completado, todo o código guardado, e a área de trabalho.",
}
