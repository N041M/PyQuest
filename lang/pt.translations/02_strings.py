# PyQuest translations -- language 'pt' -- chapter 02_strings -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"2.1 brief": r"""# 2.1 -- Indexação

## Conceito

Uma cadeia de caracteres é uma sequência de caracteres, e cada caractere tem uma **posição**
(chamada de *índice*). A contagem começa em **0**, não em 1. Assim, na cadeia `"cat"`:

```
character:  c  a  t
index:      0  1  2
```

Lês um único caractere com parênteses retos: `s[index]`.

```python
word = "cat"
print(word[0])   # c
print(word[1])   # a
```

`word[0]` é o primeiro caractere, porque a indexação começa em zero. Isto confunde
quase toda a gente à primeira: o "primeiro" caractere está no índice 0.

## Exemplo

```python
s = "python"
print(s[0])   # p
```

## A tua tarefa

Lê uma palavra com `input()`, depois imprime apenas o seu **primeiro** caractere.

Para a entrada `hello` a saída é:

```
h
```

## Está feito quando

- Para `hello` imprime `h`.
- Funciona para qualquer palavra, incluindo uma palavra de uma só letra (o
  verificador testa algumas).
""",

"2.1 hints": r"""Os caracteres são numerados a partir de 0. Os parênteses retos leem um deles: s[0].

---

Guarda primeiro a entrada, depois imprime o índice 0: `s = input()` e depois `print(s[0])`.

---

s = input()
print(s[0])
""",

"2.1 reference": r"""Uma cadeia de caracteres é uma sequência ordenada de caracteres, e `s[index]` lê o que está numa
determinada posição. As posições são **baseadas em zero**: o primeiro caractere é `s[0]`, o
segundo `s[1]`, e assim por diante.

- O resultado é, em si, uma cadeia de um único caractere (o Python não tem um tipo
  de caractere separado).
- Um índice igual ou superior ao comprimento gera `IndexError`; para uma cadeia de
  comprimento *n*, as posições válidas vão de `0` a `n - 1`.
- As cadeias de caracteres são **imutáveis** — indexar lê um caractere, mas `s[0] = "x"` é um
  erro. Para alterar o texto, constrói-se uma nova cadeia.

```python
word = "Python"
word[0]    # 'P'
word[3]    # 'h'
```
""",

"2.2 brief": r"""# 2.2 -- Indexação negativa

## Conceito

Também podes contar a partir do **fim** de uma cadeia de caracteres usando índices negativos. `-1` é
o último caractere, `-2` o penúltimo, e assim por diante.

```
character:   c   a   t
index:       0   1   2
from end:   -3  -2  -1
```

```python
word = "cat"
print(word[-1])   # t
print(word[-2])   # a
```

Isto é útil quando não queres contar o comprimento: `s[-1]` é sempre o
último caractere, seja qual for o comprimento da cadeia.

## Exemplo

```python
s = "python"
print(s[-1])   # n
```

## A tua tarefa

Lê uma palavra e depois imprime o seu **último** caractere.

Para a entrada `hello` a saída é:

```
o
```

## Está feito quando

- Para `hello` imprime `o`.
- Também funciona para uma palavra de uma só letra (`-1` aponta para esse único caractere).
""",

"2.2 hints": r"""Os índices negativos contam a partir do fim. -1 é o último caractere.

---

`s = input()` e depois `print(s[-1])`.

---

s = input()
print(s[-1])
""",

"2.2 reference": r"""Um índice **negativo** conta a partir do fim da cadeia: `s[-1]` é o último
caractere, `s[-2]` o penúltimo, e assim por diante. Poupa-te a escrever
`s[len(s) - 1]`.

- `s[-1]` e `s[len(s) - 1]` designam o mesmo caractere; a forma negativa apenas
  não precisa do comprimento.
- O intervalo negativo válido vai de `-1` até `-len(s)`; ir mais além (por exemplo,
  `s[-99]` numa cadeia curta) gera `IndexError`.
- `s[0]` é o primeiro caractere; não existe `-0` (isso é apenas `0`).

```python
word = "Python"
word[-1]   # 'n'
word[-2]   # 'o'
```
""",

"2.3 brief": r"""# 2.3 -- Fatiamento

## Conceito

Uma **fatia** retira um intervalo de caracteres de uma só vez: `s[start:stop]`. Inclui o
caractere em `start` e vai **até, mas sem incluir**, `stop`. A isto chama-se
*semiaberto*: o índice de paragem não é incluído.

```python
s = "python"
print(s[0:3])   # pyt   (indexes 0, 1, 2 -- not 3)
print(s[2:5])   # tho   (indexes 2, 3, 4)
```

Se omitires `start`, começa em 0; se omitires `stop`, vai até ao fim:

```python
print(s[:3])    # pyt   (same as s[0:3])
print(s[3:])    # hon   (from index 3 to the end)
```

Como o `stop` não é incluído, `s[0:3]` dá-te exatamente **3** caracteres.

## Exemplo

```python
s = "rainbow"
print(s[0:4])   # rain
```

## A tua tarefa

Lê uma palavra e depois imprime os seus **primeiros três** caracteres.

Para a entrada `hello` a saída é:

```
hel
```

## Está feito quando

- Para `hello` imprime `hel`.
- Para uma palavra com menos de três letras, imprime a palavra inteira -- fatiar para lá
  do fim é seguro e não gera erro. O verificador testa `hi`.
""",

"2.3 hints": r"""Uma fatia s[start:stop] retira caracteres desde start até (mas sem incluir) stop.

---

Os primeiros três caracteres são s[0:3], ou simplesmente s[:3].

---

s = input()
print(s[:3])
""",

"2.3 reference": r"""Uma **fatia** `s[start:stop]` devolve uma nova cadeia contendo os caracteres desde a
posição `start` até **mas sem incluir** `stop` — um intervalo *semiaberto*. O
comprimento do resultado é `stop - start` (quando ambos estão dentro do intervalo).

- `s[2:5]` dá os caracteres nos índices 2, 3, 4 — três caracteres.
- Qualquer um dos limites pode ser omitido: `s[:3]` começa no início, `s[3:]` vai até
  ao fim, e `s[:]` copia a cadeia inteira.
- O fatiamento nunca gera erro para limites fora do intervalo — em vez disso, ajusta-os.
  `s[:100]` numa cadeia curta devolve simplesmente tudo o que ela tem.

```python
s = "Python"
s[0:3]    # 'Pyt'
s[:2]     # 'Py'
s[2:]     # 'thon'
```
""",

"2.4 brief": r"""# 2.4 -- Fatiar o meio

## Conceito

O fatiamento combina-se bem com índices negativos, e as fatias nunca rebentam -- se uma fatia
está vazia, obténs simplesmente a cadeia vazia `""`.

`s[1:-1]` significa "do índice 1 até (mas sem incluir) o último caractere" -- por
outras palavras, elimina o primeiro e o último caracteres:

```python
s = "python"
print(s[1:-1])   # ytho
```

Se a cadeia for demasiado curta para ter um meio, a fatia é simplesmente vazia:

```python
print("ab"[1:-1])   # (nothing -- an empty string)
print("a"[1:-1])    # (nothing)
```

Sem erro. Uma fatia vazia é um resultado normal e válido.

## Erro comum

Ir "fora do intervalo" com uma fatia **não** provoca erro, ao contrário de indexar um único
caractere. `"hi"[5]` seria um erro, mas `"hi"[1:5]` está bem -- simplesmente para
no fim.

## Exemplo

```python
s = "hello"
print(s[1:-1])   # ell
```

## A tua tarefa

Lê uma palavra e depois imprime-a **sem o primeiro e o último caracteres**.

Para a entrada `hello` a saída é:

```
ell
```

## Está feito quando

- Para `hello` imprime `ell`.
- Para uma palavra de 1 ou 2 letras imprime uma linha vazia (sem meio) e não
  rebenta. O verificador testa `ab` e `a`.
""",

"2.4 hints": r"""O índice 1 é o segundo caractere; -1 é o último. Fatia entre eles.

---

Usa s[1:-1] para eliminar o primeiro e o último caracteres.

---

s = input()
print(s[1:-1])
""",

"2.4 reference": r"""Os limites de uma fatia podem ser **negativos**, contando a partir do fim, e os dois estilos
combinam-se livremente. `s[1:-1]` elimina o primeiro e o último caractere — começa no
índice 1, para mesmo antes do último.

- Uma fatia cujo início esteja no ou para lá do seu fim é **vazia**, não um erro:
  `s[3:3]` e `s[5:2]` dão ambos `""`.
- Os limites fora do intervalo são ajustados, por isso o fatiamento é tolerante onde a
  indexação simples gera erro: `s[1:99]` está bem.
- Como o `stop` é exclusivo, `s[:-1]` remove exatamente o último caractere e
  `s[1:]` remove o primeiro.

```python
s = "Python"
s[1:-1]   # 'ytho'  -- both ends trimmed
s[2:2]    # ''      -- empty, not an error
```
""",

"2.5 brief": r"""# 2.5 -- Passos e inverter

## Conceito

Uma fatia pode levar um terceiro número, o **passo**: `s[start:stop:step]`. O passo indica
quantas posições avançar de cada vez. Um passo de `2` retira cada segundo caractere:

```python
s = "abcdef"
print(s[::2])   # ace   (every 2nd character)
```

Um passo **negativo** anda para trás. O atalho `s[::-1]` -- início vazio, fim
vazio, passo `-1` -- inverte a cadeia inteira:

```python
s = "python"
print(s[::-1])   # nohtyp
```

`s[::-1]` é a forma padrão em Python de inverter uma cadeia.

## Exemplo

```python
print("hello"[::-1])   # olleh
```

## A tua tarefa

Lê uma palavra e depois imprime-a **invertida**.

Para a entrada `hello` a saída é:

```
olleh
```

## Está feito quando

- Para `hello` imprime `olleh`.
- Para uma única letra, ou uma palavra que se lê igual ao contrário (como `level`), imprime
  a palavra sem alterações. O verificador testa ambos os casos.
""",

"2.5 hints": r"""Uma fatia pode ter um passo: s[start:stop:step]. Um passo negativo vai para trás.

---

Inverte com o idioma padrão: s[::-1].

---

s = input()
print(s[::-1])
""",

"2.5 reference": r"""Uma fatia leva uma terceira parte, o **passo**: `s[start:stop:step]` retira cada
caractere de `step` em `step`. O passo por omissão é 1.

- `s[::2]` retira cada segundo caractere (índices 0, 2, 4, …).
- Um passo **negativo** anda para trás. `s[::-1]` é a forma idiomática de
  **inverter** uma cadeia; com um passo negativo, o início/fim por omissão invertem-se para
  o fim e o início.
- `s[::-2]` retira cada segundo caractere, do fim para o início.

```python
s = "Python"
s[::2]    # 'Pto'
s[::-1]   # 'nohtyP'  -- reversed
```
""",

"2.6 brief": r"""# 2.6 -- Comprimento, juntar, repetir

## Conceito

Três ferramentas do dia a dia para cadeias de caracteres:

- `len(s)` dá o **número de caracteres** em `s` (um número):
  ```python
  len("cat")    # 3
  ```
- `+` junta duas cadeias (já viste isto no capítulo 1):
  ```python
  "cat" + "!"   # "cat!"
  ```
- `*` com um número **repete** uma cadeia:
  ```python
  "ab" * 3      # "ababab"
  "-" * 5       # "-----"
  ```

`len` devolve um número, por isso podes fazer contas com ele. `+` e `*` constroem
novas cadeias.

## Exemplo

```python
s = "hi"
print(len(s))    # 2
print(s + "!")   # hi!
print(s * 3)     # hihihi
```

## A tua tarefa

Lê uma palavra e imprime três linhas:

1. o número de caracteres na palavra
2. a palavra com um ponto de exclamação adicionado no fim
3. a palavra repetida três vezes

Para a entrada `hi` a saída é:

```
2
hi!
hihihi
```

## Está feito quando

- Para `hi` as três linhas são `2`, `hi!`, `hihihi`.
- Também funciona para uma entrada vazia: `0`, `!`, e uma linha vazia. O
  verificador testa isso.
""",

"2.6 hints": r"""len(s) é um número; + junta cadeias; * repete-as.

---

print(len(s)) para a contagem, print(s + "!") para acrescentar, print(s * 3) para repetir.

---

s = input()
print(len(s))
print(s + "!")
print(s * 3)
""",

"2.6 reference": r"""Três operações fundamentais com cadeias de caracteres:

- **`len(s)`** devolve o número de caracteres em `s` como um `int`; `len("")`
  é `0`.
- **`+` concatena**: `"ab" + "cd"` é `"abcd"`. Ambos os operandos têm de ser cadeias
  — `"n" + 5` gera `TypeError`; converte primeiro com `str(5)`.
- **`*` repete**: `s * n` (ou `n * s`) junta `n` cópias. `"ab" * 3` é
  `"ababab"`; `n <= 0` dá a cadeia vazia `""`.

As três produzem cadeias **novas** e deixam as originais inalteradas (as cadeias de
caracteres são imutáveis).

```python
s = "ab"
len(s)    # 2
s + "c"   # 'abc'
s * 3     # 'ababab'
```
""",

"2.7 brief": r"""# 2.7 -- Limpar texto

## Conceito

As cadeias de caracteres têm **métodos** -- ações que chamas com um ponto depois da cadeia:
`s.method()`. Três comuns:

- `s.upper()` -> uma cópia em MAIÚSCULAS
- `s.lower()` -> uma cópia em minúsculas
- `s.strip()` -> uma cópia com os espaços removidos de **ambas as extremidades** (não do meio)

```python
"Hello".upper()     # "HELLO"
"Hello".lower()     # "hello"
"  hi  ".strip()    # "hi"
```

Os métodos devolvem uma cadeia **nova**; não alteram a original. Podes encadeá-los
-- cada um atua sobre o resultado do anterior:

```python
"  Hi  ".strip().upper()   # "HI"
```

## Exemplo

```python
s = "  python  "
print(s.strip().upper())   # PYTHON
```

## A tua tarefa

Lê uma linha, remove os espaços à volta dela e imprime-a em **maiúsculas**.

Para a entrada `  hello  ` a saída é:

```
HELLO
```

## Está feito quando

- Para `  hello  ` imprime `HELLO`.
- Os espaços no meio mantêm-se; só as extremidades são cortadas. O verificador também testa uma
  linha que só tem espaços (o resultado é uma linha vazia).
""",

"2.7 hints": r"""Os métodos chamam-se com um ponto: s.strip(), s.upper(). Devolvem cadeias novas.

---

Encadeia-os: s.strip() remove os espaços das extremidades, .upper() maiusculiza o resultado.

---

s = input()
print(s.strip().upper())
""",

"2.7 reference": r"""As cadeias de caracteres têm **métodos** — funções chamadas com a sintaxe `s.method()` que
calculam algo a partir da cadeia.

- **`.strip()`** devolve a cadeia com o **espaço em branco** inicial e final
  removido (espaços, tabulações, quebras de linha). `.lstrip()` / `.rstrip()` cortam apenas um lado.
- **`.upper()`** / **`.lower()`** devolvem a cadeia com todas as letras em maiúsculas
  ou minúsculas.

Como cada método devolve uma cadeia **nova** (a original nunca é modificada),
as chamadas **encadeiam-se**: cada uma atua sobre o resultado da anterior.

```python
"  Hi  ".strip()            # 'Hi'
"Hi".upper()                # 'HI'
"  Hello  ".strip().lower() # 'hello'  -- trimmed, then lowered
```
""",

"2.8 brief": r"""# 2.8 -- Substituir e contar

## Conceito

Mais dois métodos de cadeias de caracteres:

- `s.replace(old, new)` devolve uma cópia de `s` com **todas** as ocorrências de `old`
  trocadas por `new`:
  ```python
  "banana".replace("a", "o")   # "bonono"
  ```
- `s.count(sub)` devolve **quantas vezes** `sub` aparece (um número):
  ```python
  "banana".count("a")          # 3
  ```

Se `old` não estiver presente, `replace` devolve a cadeia sem alterações; se `sub` não
estiver presente, `count` devolve `0`.

## Exemplo

```python
s = "foo bar"
print(s.replace("o", "0"))   # f00 bar
print(s.count("o"))          # 2
```

## A tua tarefa

Lê uma linha e imprime duas linhas:

1. a linha com todas as letras `o` substituídas por um zero `0`
2. quantos `o`s havia na linha **original**

Para a entrada `foobar` a saída é:

```
f00bar
2
```

## Está feito quando

- Para `foobar` as linhas são `f00bar` e `2`.
- Para uma linha sem nenhum `o` imprime a linha sem alterações e `0`. O verificador testa
  isso.
""",

"2.8 hints": r"""replace troca todas as correspondências; count diz-te quantas correspondências existem.

---

print(s.replace("o", "0")) e depois print(s.count("o")).

---

s = input()
print(s.replace("o", "0"))
print(s.count("o"))
""",

"2.8 reference": r"""Dois métodos de procura e contagem:

- **`s.replace(old, new)`** devolve uma cadeia nova com **todas** as ocorrências
  não sobrepostas de `old` trocadas por `new`. Substitui todas as correspondências, não só a
  primeira; se `old` não ocorrer, a cadeia volta sem alterações.
- **`s.count(sub)`** devolve quantas vezes `sub` aparece, contando
  correspondências não sobrepostas da esquerda para a direita. `"aaa".count("aa")` é `1`, não 2.

Ambos apenas leem `s` e devolvem informação nova; a cadeia original permanece intocada.

```python
"a-b-c".replace("-", "_")   # 'a_b_c'  -- every match
"banana".count("a")          # 3
```
""",

"2.9 brief": r"""# 2.9 -- Encontrar uma posição

## Conceito

`s.find(sub)` devolve o **índice** onde `sub` aparece pela primeira vez -- um número que podes
depois usar para fatiar. (Se `sub` não for encontrado, devolve `-1`.)

```python
s = "name=Sam"
i = s.find("=")    # 4
print(i)           # 4
print(s[i+1:])     # Sam   (everything after the "=")
```

Portanto, `find` localiza um marcador, e uma fatia extrai a parte que queres em relação a ele.
Aqui `s[i+1:]` significa "de uma posição depois do `=` até ao fim".

## Exemplo

```python
s = "color=blue"
i = s.find("=")
print(s[i+1:])     # blue
```

## A tua tarefa

Cada entrada é uma linha com a forma `key=value` (com um único `=`). Imprime apenas o
**valor** -- tudo o que vem depois do `=`.

Para a entrada `color=blue` a saída é:

```
blue
```

## Está feito quando

- Para `color=blue` imprime `blue`.
- Para `x=1` imprime `1`; para `a=` imprime uma linha vazia; para `k=a=b` imprime
  `a=b` (só o primeiro `=` a divide). O verificador testa estes casos.
""",

"2.9 hints": r"""find diz-te onde está o "=". Depois fatia a partir de logo a seguir.

---

i = s.find("=") dá a posição; s[i+1:] é tudo o que vem depois dela.

---

s = input()
i = s.find("=")
print(s[i+1:])
""",

"2.9 reference": r"""**`s.find(sub)`** devolve o índice da **primeira** ocorrência de `sub` em `s`,
ou **`-1`** se não for encontrado (nunca gera erro). Combiná-lo com fatiamento extrai
o texto à volta de um marcador.

- O índice devolvido é onde `sub` começa, por isso `s[:i]` é a parte antes dele e
  `s[i + len(sub):]` a parte depois.
- Verifica se é `-1` antes de usar o resultado — caso contrário, um `s.find` que
  devolva `-1` fatiaria a partir do fim.
- `.index(sub)` é semelhante mas **gera** `ValueError` quando ausente; usa `.find`
  quando "não estar presente" é um caso normal.

```python
s = "key=value"
i = s.find("=")     # 3
s[:i]               # 'key'
s[i + 1:]           # 'value'
```
""",

"2.10 brief": r"""# 2.10 -- f-strings

## Conceito

Uma **f-string** permite-te colocar valores diretamente dentro de texto. Coloca um `f` antes da
aspa de abertura e depois escreve `{...}` onde quiseres que vá um valor:

```python
name = "Sam"
print(f"Hello, {name}!")     # Hello, Sam!
```

Dentro das `{}` podes colocar qualquer expressão, não só uma simples variável -- ela é
calculada e o resultado é colocado no texto:

```python
word = "cat"
print(f"{word} has {len(word)} letters")    # cat has 3 letters
print(f"{word} reversed is {word[::-1]}")   # cat reversed is tac
```

As f-strings são a forma mais clara de construir texto a partir de valores -- muito mais arrumada do que
juntar pedaços com `+`.

## Exemplo

```python
s = "python"
print(f"{s} reversed is {s[::-1]}")   # python reversed is nohtyp
```

## A tua tarefa

Lê uma palavra e depois imprime exatamente esta frase usando uma f-string:

```
WORD reversed is REVERSED
```

onde `WORD` é a entrada e `REVERSED` é ela ao contrário. Para a entrada `hello`:

```
hello reversed is olleh
```

## Está feito quando

- Para `hello` imprime `hello reversed is olleh`.
- Funciona para qualquer palavra, incluindo uma única letra. O verificador testa algumas.
""",

"2.10 hints": r"""Uma f-string começa com f" e insere valores dentro de { }.

---

Podes colocar uma expressão dentro das chavetas: f"{w} reversed is {w[::-1]}".

---

w = input()
print(f"{w} reversed is {w[::-1]}")
""",

"2.10 reference": r"""Uma **f-string** (literal de cadeia formatada) é uma cadeia prefixada com `f` na qual
`{ }` contém uma **expressão** Python; a expressão é avaliada e o seu valor é
inserido, convertido em texto.

- Qualquer expressão cabe dentro das chavetas: `f"{name}"`, `f"{a + b}"`,
  `f"{nums[0]}"`.
- Uma chaveta literal escreve-se duplicando-a: `f"{{literal}}"` mostra `{literal}`.
- Uma especificação de formato depois de dois pontos controla a apresentação, por exemplo,
  `f"{price:.2f}"` mostra duas casas decimais e `f"{n:>5}"` alinha à direita num campo
  com 5 de largura.

As f-strings são a forma mais clara de construir texto a partir de valores, substituindo cadeias de
`+` e `str()`.

```python
name, n = "Ada", 3
f"{name} solved {n} puzzles"   # 'Ada solved 3 puzzles'
f"{1/3:.2f}"                    # '0.33'
```
""",
}
