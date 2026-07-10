# PyQuest translations -- language 'pt' -- chapter 08_files -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"8.1 brief": r"""# 8.1 -- Abrir um ficheiro

## Conceito

Até agora todos os valores vinham de um literal que escreveste ou de `input()`.
Os programas a sério também leem **ficheiros** -- texto já guardado em disco.

`open(name)` dá-te um *objeto de ficheiro*. A forma correta de o usar é um bloco
`with`:

```python
with open("note.txt") as f:
    text = f.read()
```

- `with open(...) as f:` abre o ficheiro e associa-o a `f`;
- `f.read()` devolve **todo o conteúdo** do ficheiro como uma única cadeia de
  caracteres;
- quando o bloco termina, o Python **fecha o ficheiro por ti** -- mesmo que o
  código lá dentro tenha gerado um erro. Esse fecho automático é a única razão
  para preferires `with` a um `open()` isolado.

O ficheiro é procurado em relação ao local onde o programa corre, por isso
`"note.txt"` significa "um ficheiro chamado note.txt ao meu lado".

## Exemplo

Se `note.txt` contiver:

```
buy milk
call sam
```

então `text` é a cadeia de caracteres `"buy milk\ncall sam\n"` -- com as
quebras de linha incluídas.

## A tua tarefa

Existe um ficheiro chamado `note.txt` ao lado do teu programa. Lê todo o seu
conteúdo e imprime-o.

## Está feito quando

- O programa imprime exatamente o que `note.txt` contém.
- Funciona seja qual for o conteúdo do ficheiro -- uma linha, várias linhas, ou
  nenhuma.
- Abriste o ficheiro com uma instrução `with`.
""",

"8.1 hints": r"""Um bloco `with open(name) as f:` dá-te o ficheiro como `f`. Dentro dele, pede
ao ficheiro tudo o que contém.

---

`f.read()` devolve o ficheiro inteiro como uma única cadeia de caracteres.
Guarda-a e depois imprime-a a seguir (ou dentro) do bloco.

---

with open("note.txt") as f:
    text = f.read()
print(text)
""",

"8.1 reference": r"""**`open(name)`** liga-se a um ficheiro em disco; a instrução **`with`** gere-o
para que o ficheiro seja **fechado automaticamente** quando o bloco termina,
mesmo que ocorra um erro. Dentro do bloco, o objeto de ficheiro `f` fornece o
conteúdo.

- `with open(name) as f:` abre para **leitura** de texto (o modo predefinido
  `"r"`) e associa o ficheiro aberto a `f`.
- **`f.read()`** devolve todo o conteúdo como uma única cadeia de caracteres.
  (`f.read(n)` lê no máximo `n` caracteres.)
- Abrir um caminho que não existe gera `FileNotFoundError`. Usa sempre `with`
  em vez de um `open` isolado — garante o fecho.

```python
with open("notes.txt") as f:
    text = f.read()      # whole file as a string
# file is closed here
```
""",

"8.2 brief": r"""# 8.2 -- Um ficheiro, linha a linha

## Conceito

`f.read()` dá-te tudo de uma vez. Mais frequentemente queres o ficheiro **uma
linha de cada vez** -- e um objeto de ficheiro é *iterável*, por isso um ciclo
`for` percorre as suas linhas por ti:

```python
with open("tasks.txt") as f:
    for line in f:
        ...
```

Um pormenor: cada `line` ainda traz a quebra de linha que a terminou --
`"wash\n"`, não `"wash"`. Remove-a com `line.strip()` (3.7) antes de usares o
texto, ou a tua saída acumula linhas em branco.

## Exemplo

Para um `tasks.txt` de:

```
wash
cook
sleep
```

numerar cada linha dá:

```
1. wash
2. cook
3. sleep
```

`enumerate` (5.5) é a escolha natural -- começa-o em `1`:

```python
for i, line in enumerate(f, start=1):
    print(f"{i}. {line.strip()}")
```

## A tua tarefa

Lê `tasks.txt` e imprime cada linha **numerada a partir de 1**, na forma
`1. wash`. Remove a quebra de linha final para não haver linhas em branco
soltas.

## Está feito quando

- Cada linha é impressa como `<número>. <texto>`, contando a partir de 1.
- Funciona para um ficheiro de qualquer comprimento.
- Abriste o ficheiro com `with` e percorreste-o com `for`.
""",

"8.2 hints": r"""Um objeto de ficheiro é iterável: `for line in f:` dá-te uma linha por
passagem.

---

`enumerate(f, start=1)` dá `(1, primeiralinha), (2, segundalinha), ...`. Cada
linha ainda termina em `\n` -- usa `line.strip()` para a remover.

---

with open("tasks.txt") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")
""",

"8.2 reference": r"""Um objeto de ficheiro é **iterável**: percorrê-lo num ciclo produz o ficheiro
**uma linha de cada vez**, sem carregar tudo para a memória. É a forma padrão
de processar um ficheiro linha a linha.

- `for line in f:` associa `line` a cada linha **incluindo a sua quebra de
  linha final** `"\n"`; chama `line.strip()` (ou `.rstrip("\n")`) para a
  remover.
- Lê de forma preguiçosa (*lazy*), por isso lida bem com ficheiros grandes.
- `f.readlines()`, em vez disso, devolve uma **lista** com todas as linhas de
  uma vez -- bom para ficheiros pequenos, dispendioso para os grandes.

```python
with open("log.txt") as f:
    for line in f:
        print(line.strip())   # one line per pass, newline removed
```
""",

"8.3 brief": r"""# 8.3 -- Somar um ficheiro

## Conceito

Um ficheiro é sempre **texto**. Uma linha que parece `42` chega como a cadeia
de caracteres `"42\n"`, não como o número 42 -- por isso, antes de poderes
fazer contas, tens de a converter com `int()` (1.11), exatamente como fizeste
com `input()`.

`int()` ignora de bom grado os espaços em branco à volta, por isso
`int("42\n")` é `42` -- nem sequer precisas de fazer `strip` primeiro.

```python
total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
```

## Exemplo

Para um `prices.txt` de:

```
10
25
7
```

o total é `42`.

## A tua tarefa

`prices.txt` contém um número inteiro por linha. Lê-os, soma-os todos, e
imprime o total.

## Está feito quando

- O programa imprime a soma de todos os números do ficheiro.
- Números negativos e um ficheiro de uma só linha funcionam ambos.
- Abriste o ficheiro com `with` e converteste cada linha com `int()`.
""",

"8.3 hints": r"""Começa um total acumulado em 0, abre o ficheiro, e percorre as suas linhas.

---

Cada linha é uma cadeia de caracteres como `"25\n"`. `int(line)` transforma-a
num número que podes somar. Imprime o total depois do ciclo.

---

total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
print(total)
""",

"8.3 reference": r"""O conteúdo de um ficheiro é sempre **texto**, por isso uma linha como `"42\n"`
é uma *cadeia de caracteres*. Para fazer contas tens de converter primeiro
cada linha num número.

- `int(line)` interpreta um inteiro; tolera espaços em branco à volta
  (incluindo a quebra de linha final), por isso `int("42\n")` é `42`. Usa
  `float(line)` para decimais.
- Uma linha em branco ou não numérica gera `ValueError` — salta as linhas em
  branco (`if not line.strip(): continue`) ou envolve a conversão num `try`.
- Acumula à medida que avanças: mantém um total corrente e soma cada valor
  interpretado.

```python
total = 0
with open("nums.txt") as f:
    for line in f:
        total += int(line)    # text -> number, then add
```
""",

"8.4 brief": r"""# 8.4 -- Escrever num ficheiro

## Conceito

Ler é metade da história; os programas também **criam** ficheiros. Abre com o
modo `"w"` (de *write*, escrita) e chama `.write()`:

```python
with open("out.txt", "w") as f:
    f.write("hello\n")
```

Duas coisas a saber:

- `"w"` cria um ficheiro novo em folha (ou **esvazia** um já existente), e só
  depois escreve.
- `.write()` coloca **exatamente** o texto que lhe dás -- sem a quebra de
  linha automática que o `print()` acrescenta. Se quiseres quebras de linha,
  inclui tu mesmo o `"\n"`.

Um padrão comum é **ler um ficheiro, escrever noutro**:

```python
with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
```

## Exemplo

Se `in.txt` contiver `quiet please`, então `out.txt` deve acabar por conter
`QUIET PLEASE`.

## A tua tarefa

Lê `in.txt`, e escreve o seu conteúdo **em maiúsculas** (`.upper()` de 2.7)
num novo ficheiro chamado `out.txt`.

## Está feito quando

- `out.txt` contém exatamente o texto de `in.txt`, em maiúsculas.
- Um `in.txt` vazio produz um `out.txt` vazio -- sem erro.
- Usaste `with` e abriste `out.txt` em modo `"w"`.
""",

"8.4 hints": r"""Dois passos: primeiro lê in.txt para uma cadeia de caracteres, depois abre
out.txt em modo `"w"` e escreve a cadeia em maiúsculas.

---

`open("out.txt", "w")` é a parte da escrita; `text.upper()` faz a conversão
para maiúsculas. `.write()` escreve a cadeia tal como está.

---

with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
""",

"8.4 reference": r"""Abrir com o modo **`"w"`** abre um ficheiro para **escrita**. **Cria** o
ficheiro se não existir e **trunca-o** (esvazia-o) se já existir, pelo que o
conteúdo anterior é perdido.

- **`f.write(text)`** escreve uma cadeia de caracteres e, ao contrário do
  `print`, não acrescenta **nenhuma** quebra de linha final — inclui tu mesmo
  `"\n"` onde quiseres quebras de linha.
- `f.write` aceita apenas cadeias de caracteres; converte números com `str()`
  ou com uma f-string primeiro.
- Usa `with` para que os dados sejam gravados e o ficheiro fechado
  corretamente.

```python
with open("out.txt", "w") as f:
    f.write("first line\n")
    f.write("second line\n")   # newlines are explicit
```
""",

"8.5 brief": r"""# 8.5 -- Anexar, não substituir

## Concept

O modo `"w"` é impiedoso: **esvazia** o ficheiro antes de escrever. Isso está
errado quando queres *acrescentar* a um ficheiro -- um registo (log) que vais
fazendo crescer, por exemplo. Para isso existe o modo `"a"` (de *append*,
anexar):

```python
with open("log.txt", "a") as f:
    f.write("another line\n")
```

`"a"` deixa intacto tudo o que já está no ficheiro e escreve o teu novo texto
**depois** disso (e se o ficheiro ainda não existir, `"a"` simplesmente
cria-o). O mesmo `.write()`, a mesma necessidade de acrescentares o teu
próprio `"\n"` -- só a letra do modo muda, e essa letra é toda a diferença
entre "acrescentar a" e "apagar e substituir". Todo o objetivo do `"a"` é que
*não* leias o ficheiro primeiro -- limitas-te a escrever no fim.

## Exemplo

Se `log.txt` já contiver:

```
woke up
ate
```

então anexar a linha `ran` deixa-o com `woke up`, `ate`, `ran` -- as três, por
ordem.

## A tua tarefa

Já existe um ficheiro `log.txt`. Lê uma linha de texto da entrada (`input()`)
e **anexa-a** a `log.txt` como uma nova linha, mantendo tudo o que já lá
estava.

## Está feito quando

- O conteúdo original de `log.txt` continua presente, por ordem.
- A nova entrada é adicionada como a sua própria linha no fim.
- Usar `"w"` apagaria as linhas antigas -- por isso tens de usar `"a"`.
""",

"8.5 hints": r"""Lê a entrada com `input()`, depois abre o ficheiro num modo que *mantenha* o
que já lá está.

---

O modo `"a"` anexa em vez de apagar. Não te esqueças do `"\n"` para que a nova
entrada fique na sua própria linha.

---

entry = input()
with open("log.txt", "a") as f:
    f.write(entry + "\n")
""",

"8.5 reference": r"""O modo **`"a"`** abre um ficheiro para **anexar** (append): as escritas vão
para o **fim**, e todo o conteúdo existente é mantido. É o equivalente não
destrutivo de `"w"`.

- `"a"` cria o ficheiro se não existir; se existir, `f.write` acrescenta
  depois do que já lá está — nada é substituído.
- `"w"` esvazia o ficheiro primeiro; recorre a `"a"` para fazer crescer um
  registo (log) ou acumular resultados entre execuções.
- Tal como com `"w"`, as quebras de linha não são adicionadas por ti.

```python
with open("log.txt", "a") as f:
    f.write("another entry\n")   # added at the end, old lines kept
```
""",

"8.6 brief": r"""# 8.6 -- Filtrar linhas para um novo ficheiro

## Conceito

Junta a leitura e a escrita e obténs a tarefa quotidiana de dados: percorrer
um ficheiro de entrada linha a linha, **decidir** que linhas manter (3.2
`if`), e escrever apenas essas num ficheiro de saída.

```python
with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if keep(line):
            f.write(line)
```

`f.readlines()` lê o ficheiro inteiro para uma lista de linhas de uma vez --
útil quando queres terminar de ler antes de começares a escrever.

Uma linha vazia ou só com espaços está "em branco": `line.strip()` devolve
`""` para ela, e uma cadeia de caracteres vazia é falsa (*falsey*, 3.1), por
isso `if line.strip():` é um teste limpo para "esta linha tem conteúdo real".

## Exemplo

A partir de um `lines.txt` de:

```
keep me

and me
```

a linha vazia do meio é descartada, ficando `keep me` e `and me`.

## A tua tarefa

Lê `lines.txt` e escreve apenas as suas linhas **não vazias** em `kept.txt`,
pela mesma ordem. Descarta qualquer linha que esteja vazia ou seja só espaço
em branco.

## Está feito quando

- `kept.txt` contém exatamente as linhas não vazias de `lines.txt`, por ordem.
- Um ficheiro sem linhas em branco é copiado sem alterações; um ficheiro todo
  em branco produz um `kept.txt` vazio.
- Usaste `with`, um ciclo, e um `if` para decidir o que manter.
""",

"8.6 hints": r"""Lê primeiro todas as linhas, depois abre o ficheiro de saída em modo `"w"` e
percorre-as, escrevendo apenas as que queres manter.

---

`if line.strip():` é verdadeiro apenas quando a linha tem conteúdo real.
Escreve a `line` original (já termina em `\n`), não uma cópia sem espaços.

---

with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if line.strip():
            f.write(line)
""",

"8.6 reference": r"""Uma passagem de **filtragem** lê um ficheiro, mantém apenas as linhas que um
`if` aceita, e escreve-as noutro — a versão em ficheiros do padrão
compreensão-com-`if`.

- Abre a origem para leitura e o destino para escrita, percorre a origem, e só
  faz `f_out.write(line)` quando a linha passa no teu teste.
- As linhas da entrada mantêm a sua quebra de linha, por isso escrevê-las de
  volta reproduz as quebras de linha sem acrescentar nenhuma.
- Ler e escrever o **mesmo** caminho ao mesmo tempo não é seguro; escreve para
  um ficheiro novo (ou reúne os resultados e só depois escreve).

```python
with open("all.txt") as src, open("kept.txt", "w") as out:
    for line in src:
        if "ERROR" in line:
            out.write(line)       # keep only matching lines
```
""",

"8.7 brief": r"""# 8.7 -- Um relatório de frequências

## Conceito

Esta puzzle junta o capítulo com a contagem por dicionário de 5.9: lê um
ficheiro, **conta** algo ao longo dele, e escreve o resultado noutro
ficheiro.

Lê as palavras, depois conta-as com um dicionário (o padrão `dict.get`):

```python
with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

`f.read().split()` lê o ficheiro inteiro e divide-o em qualquer espaço em
branco, dando-te assim uma lista simples de palavras, fosse qual fosse o seu
espaçamento.

Depois escreve o relatório, **ordenado por contagem, do maior para o menor**,
com empates desfeitos alfabeticamente. `sorted` com uma `key` (5.4) faz as
duas coisas de uma vez:

```python
for w in sorted(counts, key=lambda w: (-counts[w], w)):
    f.write(f"{w}: {counts[w]}\n")
```

A chave `(-counts[w], w)` ordena por contagem decrescente (negando-a) e depois
pela própria palavra em caso de empate.

## Exemplo

Um `words.txt` de `fig fig pear fig pear` torna-se num `report.txt` de:

```
fig: 3
pear: 2
```

## A tua tarefa

Conta quantas vezes cada palavra aparece em `words.txt`, e escreve
`report.txt` com uma linha `word: count` por palavra distinta -- ordenada por
contagem (a mais alta primeiro), com empates por ordem alfabética.

## Está feito quando

- Cada palavra distinta aparece uma vez, como `word: count`.
- As linhas estão ordenadas por contagem decrescente, alfabética dentro de um
  empate.
- Usaste `with`, um dicionário para contar, e leste as palavras do ficheiro.
""",

"8.7 hints": r"""Lê as palavras para uma lista, depois constrói um dicionário de contagens com
o padrão `counts[w] = counts.get(w, 0) + 1` de 5.9.

---

Para ordenar o relatório, ordena as chaves do dicionário com uma função
`key`: `sorted(counts, key=lambda w: (-counts[w], w))` dá a contagem mais alta
primeiro, alfabética dentro dos empates. Escreve cada
`f"{w}: {counts[w]}\n"`.

---

with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as f:
    for w in sorted(counts, key=lambda w: (-counts[w], w)):
        f.write(f"{w}: {counts[w]}\n")
""",

"8.7 reference": r"""Um **relatório de frequências** é um pipeline de ficheiros em três etapas:
**ler** o ficheiro, **contar** para um dicionário, e depois **escrever** um
resumo ordenado.

- Percorre as linhas (ou palavras), contando com
  `counts[k] = counts.get(k, 0) + 1`.
- Ordena o resultado com `sorted(counts.items(), ...)` — por chave, ou por
  contagem com `key=lambda kv: kv[1]` (acrescenta `reverse=True` para a mais
  frequente primeiro).
- Escreve cada par como uma linha formatada, por exemplo
  `out.write(f"{word}: {n}\n")`.

Compõe a E/S de ficheiros deste capítulo com as ferramentas de dicionário e
`sorted` de capítulos anteriores.

```python
counts = {}
with open("words.txt") as f:
    for line in f:
        w = line.strip()
        counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as out:
    for w, n in sorted(counts.items()):
        out.write(f"{w}: {n}\n")
```
""",

"8.8 brief": r"""# 8.8 -- Capítulo final: um relatório de classificação

## Conceito

Este capítulo final é um pequeno programa a sério: lê um ficheiro de
registos, classifica-os, e escreve um relatório formatado -- usando split
(4.4), desempacotamento (4.7), `int()` (1.11), `sorted` com uma key (5.4),
f-strings (2.10), e ficheiros (este capítulo), tudo junto.

`scores.txt` tem um registo por linha, um nome e uma pontuação separados por
um espaço:

```
alice 40
bob 25
cara 40
```

Cada linha divide-se nos seus dois campos:

```python
name, score = line.split()
score = int(score)
```

Queres que `ranking.txt` liste os jogadores da pontuação mais alta para a
mais baixa (empates por ordem alfabética), seguido de uma linha final de
total:

```
alice - 40
cara - 40
bob - 25
Total: 105
```

Repara no formato exato: `name - score` por jogador (espaços à volta do
travessão), e uma linha final de fecho `Total: <sum>`.

## A tua tarefa

Lê `scores.txt`, e escreve `ranking.txt` com uma linha `name - score` por
jogador ordenada por pontuação (a mais alta primeiro, empates por ordem
alfabética), seguida de uma linha final `Total: <soma de todas as
pontuações>`.

## Está feito quando

- Os jogadores estão listados como `name - score`, a pontuação mais alta
  primeiro, empates por ordem alfabética.
- A última linha é `Total: ` seguido da soma de todas as pontuações.
- Um ficheiro com um só jogador funciona, e usaste `with` para ambos os
  ficheiros.
""",

"8.8 hints": r"""Lê as linhas, e para cada uma `name, score = line.split()`; converte a
pontuação com `int()`. Reúne os pares numa lista.

---

Ordena com `key=lambda p: (-p[1], p[0])` para a pontuação mais alta primeiro,
empates por ordem alfabética. Escreve cada `f"{name} - {score}\n"`, e depois
um `f"Total: {sum_of_scores}\n"` final.

---

with open("scores.txt") as f:
    lines = f.read().splitlines()
players = []
for line in lines:
    name, score = line.split()
    players.append((name, int(score)))
players.sort(key=lambda p: (-p[1], p[0]))
total = sum(score for name, score in players)
with open("ranking.txt", "w") as f:
    for name, score in players:
        f.write(f"{name} - {score}\n")
    f.write(f"Total: {total}\n")
""",

"8.8 reference": r"""O capítulo final lê **registos**, interpreta cada um em campos utilizáveis,
classifica-os, e escreve um **relatório formatado** — a forma do trabalho real
com dados.

- **Interpretar**: divide cada linha em campos e converte os tipos (por
  exemplo `name, score = line.split(","); score = int(score)`), reunindo os
  registos numa lista.
- **Classificar**: `sorted(records, key=..., reverse=True)` ordena pelo campo
  que importa.
- **Formatar**: escreve linhas alinhadas e legíveis por humanos, usando
  larguras de campo em f-strings (`f"{name:<12}{score:>5}"`) para que as
  colunas fiquem alinhadas.

```python
records = []
with open("scores.csv") as f:
    for line in f:
        name, score = line.strip().split(",")
        records.append((name, int(score)))
with open("ranked.txt", "w") as out:
    for name, score in sorted(records, key=lambda r: r[1], reverse=True):
        out.write(f"{name:<12}{score:>5}\n")
```
""",
}
