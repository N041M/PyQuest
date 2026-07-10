# PyQuest translations -- language 'pt' -- chapter 13_datetime -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"13.1 brief": r"""# 13.1 -- date: um dia do calendário

## Conceito

O módulo **`datetime`** modela datas de calendário e horas reais. O seu tipo
**`date`** guarda um único dia -- ano, mês, dia -- como um único objeto:

```python
from datetime import date

d = date(2026, 6, 20)
d.year      # 2026
d.isoformat()   # '2026-06-20'
```

- `date(year, month, day)` constrói o objeto e **valida-o**: `date(2026,
  13, 1)` gera um erro, porque não existe o mês 13.
- `.isoformat()` apresenta-o como a cadeia padrão `YYYY-MM-DD`, preenchida com zeros.
- Um `date` é muito melhor do que três números inteiros soltos: conhece o
  calendário, por isso consegue comparar-se, subtrair-se e formatar-se.

## Exemplo

```python
from datetime import date

def new_year(year):
    return date(year, 1, 1).isoformat()
```

## A tua tarefa

Usando **`date`** de `datetime`, define `iso(y, m, d)` que constrói a data e
devolve a sua cadeia `YYYY-MM-DD` através de `.isoformat()`.

## Está feito quando

- `iso(2026, 6, 20)` devolve `"2026-06-20"`.
- `iso(1999, 1, 5)` devolve `"1999-01-05"` (repara no preenchimento com zeros).
- A cadeia vem do `.isoformat()` de um objeto `date`, não de formatação manual.
""",

"13.1 hints": r"""`from datetime import date`, depois `date(y, m, d)` cria o objeto. Tem um
método `.isoformat()` que devolve a cadeia YYYY-MM-DD.

---

Encadeia-os: `date(y, m, d).isoformat()`. O preenchimento com zeros é tratado
por ti.

---

from datetime import date


def iso(y, m, d):
    return date(y, m, d).isoformat()
""",

"13.1 reference": r"""O módulo **`datetime`** disponibiliza tipos para datas de calendário e horas.
O seu tipo **`date`** guarda um dia como um único objeto: `date(year, month, day)`.

- O construtor **valida** os valores em relação ao calendário real —
  `date(2026, 2, 30)` gera `ValueError`, para que uma data impossível não
  passe despercebida.
- Os atributos `.year`, `.month`, `.day` lêem as partes de volta;
  **`.isoformat()`** apresenta a cadeia padrão `YYYY-MM-DD`, sempre preenchida
  com zeros.
- Um `date` conhece o calendário, por isso consegue comparar (`<`, `==`),
  subtrair (13.5) e indicar o seu dia da semana (13.3) — coisas que três
  números inteiros soltos ou uma cadeia construída à mão não conseguem fazer.
  `date.today()` devolve o dia atual.

```python
from datetime import date

d = date(2026, 6, 20)
d.month          # 6
d.isoformat()    # '2026-06-20'
date(2026, 1, 5).isoformat()   # '2026-01-05'  -- padded
```
""",

"13.2 brief": r"""# 13.2 -- fromisoformat: de texto para data

## Conceito

As datas costumam chegar como **texto** -- de um ficheiro, um formulário, uma
API. **`date.from
isoformat`** analisa uma cadeia padrão `YYYY-MM-DD` e produz
um objeto `date` real, o inverso de `.isoformat()`:

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
d.year      # 2026
d.month     # 6
d.day       # 20
```

- Devolve um `date`, por isso podes depois ler `.year` / `.month` / `.day`,
  comparar a data ou fazer aritmética com ela -- tudo o que uma data consegue
  fazer.
- Espera exatamente a forma `YYYY-MM-DD`; uma cadeia malformada gera
  `ValueError`.

Analisar para uma data real (em vez de recortares a cadeia tu próprio)
significa que o valor fica validado e pronto para trabalho de calendário.

## Exemplo

```python
from datetime import date

def month_of(text):
    return date.fromisoformat(text).month
```

## A tua tarefa

Usando **`date.fromisoformat`**, define `parts(text)` que analisa uma cadeia
`YYYY-MM-DD` e devolve o tuplo de inteiros `(year, month, day)` lidos a partir
dos atributos do objeto de data.

## Está feito quando

- `parts("2026-06-20")` devolve `(2026, 6, 20)`.
- `parts("1999-01-05")` devolve `(1999, 1, 5)`.
- Os valores vêm dos atributos de um `date` analisado, não de
  `text.split("-")`.
""",

"13.2 hints": r"""`date.fromisoformat(text)` transforma a cadeia num objeto de data. Guarda-o
numa variável.

---

Lê `d.year`, `d.month`, `d.day` desse objeto e devolve-os como um tuplo.

---

from datetime import date


def parts(text):
    d = date.fromisoformat(text)
    return (d.year, d.month, d.day)
""",

"13.2 reference": r"""**`date.fromisoformat(text)`** analisa uma cadeia padrão `YYYY-MM-DD` e
produz um objeto `date` — o inverso de `.isoformat()`. O resultado é uma data
real, por isso podes ler os seus atributos, comparar ou fazer aritmética com
ela.

- Espera exatamente a forma ISO; uma cadeia malformada ou impossível gera
  `ValueError`, o que valida a entrada como efeito secundário.
- `.year`, `.month`, `.day` lêem os componentes de volta como inteiros.
- Analisar para uma data (em vez de recortares o texto tu próprio) é o
  objetivo: o valor fica verificado e imediatamente pronto para trabalho de
  calendário. Para formatos que não sejam ISO, `datetime.strptime` analisa
  segundo um formato explícito (13.7).

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
(d.year, d.month, d.day)     # (2026, 6, 20)
d < date.fromisoformat("2026-12-31")   # True
```
""",

"13.3 brief": r"""# 13.3 -- weekday: que dia da semana

## Conceito

Dada uma data, que dia da semana é? Calcular isto à mão significa conhecer os
anos bissextos e a duração de cada mês. O objeto `date` já o faz -- basta
perguntar-lhe:

```python
from datetime import date

date(2026, 6, 20).weekday()     # 5  (Saturday)
```

- **`.weekday()`** devolve um inteiro: **segunda-feira é 0**, terça-feira 1,
  ... domingo 6.
- (`.isoweekday()` é a mesma ideia mas segunda-feira=1 .. domingo=7.)

Isto é o tipo de coisa que deixas a biblioteca fazer: ela codifica o
calendário real, por isso a resposta é correta para qualquer data, anos
bissextos incluídos.

## Exemplo

```python
from datetime import date

def is_weekend(text):
    return date.fromisoformat(text).weekday() >= 5
```

## A tua tarefa

Define `weekday(text)` que recebe uma cadeia `YYYY-MM-DD` e devolve o seu dia
da semana como um inteiro, **segunda-feira=0 .. domingo=6**, usando o
`.weekday()` do objeto de data.

## Está feito quando

- `weekday("2026-06-20")` devolve `5` (um sábado).
- `weekday("2000-01-01")` devolve `5`.
- A resposta vem de `.weekday()` sobre um `date` analisado.
""",

"13.3 hints": r"""Analisa primeiro a cadeia para uma data com `date.fromisoformat(text)`. Um
objeto de data consegue dizer-te o seu dia da semana.

---

`.weekday()` devolve 0 para segunda-feira até 6 para domingo. Chama-o sobre a
data analisada e devolve o resultado.

---

from datetime import date


def weekday(text):
    return date.fromisoformat(text).weekday()
""",

"13.3 reference": r"""**`date.weekday()`** devolve o dia da semana como um inteiro,
**segunda-feira = 0** até **domingo = 6**. Como um `date` codifica o
calendário real — anos bissextos, meses de duração variável — calcula isto
corretamente para qualquer data, que é exatamente o tipo de trabalho que
delegas na biblioteca em vez de deduzires à mão.

- `.isoweekday()` é o mesmo mas **segunda-feira = 1 .. domingo = 7** (a
  convenção ISO).
- Um uso comum é `weekday() >= 5` para testar se é fim de semana.
- O companheiro `.strftime("%A")` formata o **nome** do dia da semana, mas
  isso depende da configuração regional; o `.weekday()` numérico é estável em
  qualquer lugar.

```python
from datetime import date

date(2026, 6, 20).weekday()      # 5  (Saturday)
date(2026, 6, 22).weekday()      # 0  (Monday)
date(2026, 6, 20).weekday() >= 5 # True -- it's the weekend
```
""",

"13.4 brief": r"""# 13.4 -- timedelta: aritmética de datas

## Conceito

Um **`timedelta`** é uma **duração** -- um intervalo de tempo. Adiciona um a
uma data e obténs outra data, com toda a confusão do calendário (duração dos
meses, mudança de ano, dias bissextos) tratada por ti:

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)     # date(2026, 7, 30)
date(2026, 12, 25) + timedelta(days=10)    # date(2027, 1, 4)  -- crosses the year
```

- `timedelta(days=n)` é uma duração de `n` dias (também aceita `weeks=`,
  `hours=`, etc.). `n` pode ser **negativo** para ir para trás.
- `date + timedelta` dá um novo `date`; `date - timedelta` vai no sentido
  contrário.
- É por isso que nunca fazes contas de datas à mão: a biblioteca sabe que
  fevereiro tem 29 dias num ano bissexto, e tu não precisas de saber.

## Exemplo

```python
from datetime import date, timedelta

def tomorrow(text):
    return (date.fromisoformat(text) + timedelta(days=1)).isoformat()
```

## A tua tarefa

Define `add_days(text, n)` que recebe uma cadeia `YYYY-MM-DD` e um inteiro
`n`, e devolve a cadeia `YYYY-MM-DD` da data `n` dias depois (usando
`timedelta`). `n` pode ser negativo.

## Está feito quando

- `add_days("2026-06-20", 40)` devolve `"2026-07-30"`.
- `add_days("2026-01-01", -1)` devolve `"2025-12-31"`.
- O deslocamento usa `timedelta` sobre um `date` real, não uma contagem de
  dias feita à mão.
""",

"13.4 hints": r"""Importa `date` e `timedelta`. Analisa o texto e depois adiciona
`timedelta(days=n)` à data.

---

`date.fromisoformat(text) + timedelta(days=n)` dá uma nova data; chama
`.isoformat()` nessa data para obteres a cadeia. `n` negativo simplesmente
funciona.

---

from datetime import date, timedelta


def add_days(text, n):
    return (date.fromisoformat(text) + timedelta(days=n)).isoformat()
""",

"13.4 reference": r"""Um **`timedelta`** representa uma **duração** — um intervalo de tempo, não um
ponto nele. Adicionar um a um `date` produz outro `date`, com toda a
contabilidade do calendário (duração dos meses, fronteiras de ano, dias
bissextos) tratada automaticamente.

- `timedelta(days=n)` é `n` dias; também aceita `weeks=`, `hours=`,
  `minutes=`, `seconds=`. `n` pode ser **negativo** para se mover para trás.
- `date + timedelta` e `date - timedelta` dão uma nova data; subtrair duas
  *datas* dá um `timedelta` (13.5).
- É por isso que a aritmética de datas passa pela biblioteca: `date(2026, 12, 25) +
  timedelta(days=10)` avança corretamente para o ano seguinte, e a duração de
  fevereiro nunca é problema teu.

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)    # date(2026, 7, 30)
date(2026, 1, 1) - timedelta(days=1)      # date(2025, 12, 31)
date(2026, 6, 20) + timedelta(weeks=2)    # date(2026, 7, 4)
```
""",

"13.5 brief": r"""# 13.5 -- Subtrair datas: dias entre elas

## Conceito

Adicionar uma duração a uma data dá uma data. O inverso também funciona:
**subtrai uma data de outra** e obténs um **`timedelta`** -- o intervalo entre
elas:

```python
from datetime import date

gap = date(2026, 7, 1) - date(2026, 6, 20)
gap            # timedelta(days=11)
gap.days       # 11
```

- `date_b - date_a` é um `timedelta`; o seu **`.days`** é o número inteiro de
  dias entre elas.
- Se `date_b` for **anterior** a `date_a`, `.days` é **negativo**.
- É exato ao longo de meses, anos e dias bissextos -- a biblioteca conta, tu
  não precisas.

## Exemplo

```python
from datetime import date

def days_old(born, today):
    return (date.fromisoformat(today) - date.fromisoformat(born)).days
```

## A tua tarefa

Define `days_between(a, b)` que recebe duas cadeias `YYYY-MM-DD` e devolve o
número de dias **de `a` até `b`** (de modo que um `b` posterior dê um número
positivo), usando subtração de datas.

## Está feito quando

- `days_between("2026-06-20", "2026-07-01")` devolve `11`.
- `days_between("2026-07-01", "2026-06-20")` devolve `-11`.
- `days_between("2026-06-20", "2026-06-20")` devolve `0`.
- A contagem vem de subtrair dois objetos `date`, não de aritmética manual.
""",

"13.5 hints": r"""Analisa as duas cadeias para datas e depois subtrai-as. `date_b - date_a` é
um timedelta.

---

Um timedelta tem um atributo `.days`. Para "de a até b", subtrai `a` de `b`:
`(date.fromisoformat(b) - date.fromisoformat(a)).days`.

---

from datetime import date


def days_between(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days
""",

"13.5 reference": r"""Subtrair um `date` de outro produz um **`timedelta`** — o intervalo entre
eles — e o seu atributo **`.days`** é o número inteiro de dias, calculado com
exatidão ao longo de meses, anos e dias bissextos.

- `date_b - date_a` mede de `a` até `b`: se `b` for **anterior**, `.days` é
  **negativo**, por isso o sinal indica-te a direção.
- O resultado é uma duração, por isso compõe-se: adiciona-a de volta a uma
  data, multiplica-a, compara dois intervalos.
- Este é o contraponto de contagem de adicionar um `timedelta` (13.4) —
  juntos, tornam as datas numa pequena álgebra: `date + duration = date`,
  `date - date = duration`.

```python
from datetime import date

(date(2026, 7, 1) - date(2026, 6, 20)).days     # 11
(date(2026, 6, 20) - date(2026, 7, 1)).days     # -11
(date(2026, 3, 1) - date(2024, 3, 1)).days      # 730  -- 2024 was a leap year
```
""",

"13.6 brief": r"""# 13.6 -- strftime: formata uma data à tua maneira

## Conceito

`.isoformat()` dá sempre `YYYY-MM-DD`. Quando precisas de um formato
diferente, **`strftime`** ("string format time") apresenta uma data usando
**códigos de formato**:

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y.%m.%d")     # '2026.06.20'
```

- `%d` é o dia, `%m` o mês, `%Y` o ano com quatro dígitos -- todos preenchidos
  com zeros. Tudo o resto na cadeia de formato (o `/`, o `.`, os espaços) é
  copiado literalmente.
- Existem outros códigos (`%H` hora, `%M` minuto, e códigos de nome como
  `%A`), mas os numéricos são os principais.

Assim, um único objeto de data consegue apresentar-se da forma que um
relatório ou utilizador esperar.

## Exemplo

```python
from datetime import date

def dotted(text):
    return date.fromisoformat(text).strftime("%Y.%m.%d")
```

## A tua tarefa

Define `pretty(text)` que recebe uma cadeia `YYYY-MM-DD` e a devolve no
formato **`DD/MM/YYYY`**, usando `strftime("%d/%m/%Y")` sobre a data
analisada.

## Está feito quando

- `pretty("2026-06-20")` devolve `"20/06/2026"`.
- `pretty("1999-01-05")` devolve `"05/01/1999"` (preenchido com zeros).
- A formatação é feita por `strftime`, não reorganizando pedaços separados.
""",

"13.6 hints": r"""Analisa a data com `date.fromisoformat(text)` e depois chama `.strftime(...)`
sobre ela com o formato que queres.

---

A cadeia de formato para DD/MM/YYYY é `"%d/%m/%Y"`. As barras são copiadas
literalmente; os códigos preenchem os números com zeros.

---

from datetime import date


def pretty(text):
    return date.fromisoformat(text).strftime("%d/%m/%Y")
""",

"13.6 reference": r"""**`strftime(format)`** ("string-format-time") apresenta uma data ou datetime
numa cadeia que descreves com **códigos de formato**. Onde `.isoformat()` dá
um formato fixo, `strftime` dá qualquer formato.

- Códigos comuns: `%Y` ano com quatro dígitos, `%m` mês, `%d` dia — todos
  preenchidos com zeros; `%H` hora, `%M` minuto, `%S` segundo. Quaisquer
  outros caracteres (`/`, `.`, espaços) são copiados literalmente.
- Códigos de nome como `%A` (dia da semana) e `%B` (mês) **dependem da
  configuração regional**, por isso prefere os códigos numéricos para
  resultados que têm de ser estáveis.
- `strptime` é o inverso — ele *analisa* uma cadeia segundo um formato (13.7).

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y%m%d")       # '20260620'
d.strftime("%d.%m.%y")     # '20.06.26'  -- %y is the 2-digit year
```
""",

"13.7 brief": r"""# 13.7 -- strptime: analisar segundo um formato

## Conceito

`date.fromisoformat` só lê o único formato ISO. Para **qualquer** formato --
uma data com uma hora, uma ordem personalizada -- usa **`datetime.strptime`**
("parse time"). Dás-lhe a cadeia **e** um formato que a descreve, com os
mesmos códigos do `strftime`:

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.year     # 2026
dt.hour     # 14
dt.minute   # 30
```

- O formato tem de corresponder à forma da cadeia; uma incompatibilidade gera
  `ValueError`, por isso valida enquanto analisa.
- O resultado é um **`datetime`** -- uma data *e* uma hora -- com os
  atributos `.year`, `.month`, `.day`, `.hour`, `.minute`, `.second`.

`strptime` analisa, `strftime` formata: os mesmos códigos, sentidos opostos.

## Exemplo

```python
from datetime import datetime

def year_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").year
```

## A tua tarefa

Define `hour_of(text)` que recebe uma marca temporal como
`"2026-06-20 14:30"` e devolve a **hora** como um inteiro, analisando-a com
`datetime.strptime` e o formato `"%Y-%m-%d %H:%M"`.

## Está feito quando

- `hour_of("2026-06-20 14:30")` devolve `14`.
- `hour_of("1999-01-05 09:05")` devolve `9`.
- A hora vem de um `datetime` analisado, não de recorte de cadeia.
""",

"13.7 hints": r"""`datetime.strptime(text, format)` analisa a cadeia. O formato reflete a marca
temporal: `"%Y-%m-%d %H:%M"`.

---

O objeto analisado é um datetime com um atributo `.hour`. Devolve-o.

---

from datetime import datetime


def hour_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").hour
""",

"13.7 reference": r"""**`datetime.strptime(text, format)`** analisa uma cadeia e produz um
**`datetime`** usando os mesmos códigos de formato que `strftime` — é o
sentido inverso. Onde `date.fromisoformat` só lê o único formato ISO,
`strptime` lê **qualquer** formato que consigas descrever.

- O `format` tem de corresponder exatamente à forma da cadeia
  (`"%Y-%m-%d %H:%M"` para `"2026-06-20 14:30"`); uma incompatibilidade gera
  `ValueError`, validando enquanto analisa.
- O resultado é um `datetime` — uma data **e** uma hora — expondo `.year`,
  `.month`, `.day`, `.hour`, `.minute`, `.second`. (`.date()` e `.time()`
  extraem apenas uma parte.)
- Lembra-te do par: **strptime** analisa (cadeia → datetime), **strftime**
  formata (datetime → cadeia).

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.hour                      # 14
datetime.strptime("05/01/1999", "%d/%m/%Y").year   # 1999
```
""",

"13.8 brief": r"""# 13.8 -- Capstone: deslocar uma marca temporal

## Conceito

Isto junta o capítulo todo numa única viagem de ida e volta: **analisar** uma
marca temporal, **deslocá-la** por uma duração, **formatar** o resultado de
volta -- cada passo uma ferramenta que já conheces.

```python
from datetime import datetime, timedelta

dt = datetime.strptime("2026-06-20 23:30", "%Y-%m-%d %H:%M")  # parse
dt = dt + timedelta(hours=2)                                  # shift
dt.strftime("%Y-%m-%d %H:%M")                                 # '2026-06-21 01:30'
```

Repara que o deslocamento passou da meia-noite para o dia seguinte -- a
biblioteca trata disso automaticamente, ao longo de dias, meses e anos.
Fazer isto à mão significaria reimplementar o calendário e o relógio.

## A tua tarefa

Define `add_hours(timestamp, hours)` que recebe uma cadeia
`"YYYY-MM-DD HH:MM"` e um número inteiro de `hours` (que pode ser negativo),
e devolve a marca temporal deslocada por essas horas, no **mesmo formato
`"YYYY-MM-DD HH:MM"`**.

Usa `datetime.strptime` para analisar, `timedelta(hours=...)` para deslocar,
e `strftime` para formatar.

## Está feito quando

- `add_hours("2026-06-20 23:30", 2)` devolve `"2026-06-21 01:30"`.
- `add_hours("2026-01-01 00:30", -1)` devolve `"2025-12-31 23:30"`.
- O deslocamento usa `timedelta` sobre um `datetime` analisado, formatado com
  `strftime` -- não aritmética manual sobre a cadeia.
""",

"13.8 hints": r"""Três passos, três ferramentas: `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")`
para analisar, `+ timedelta(hours=hours)` para deslocar, `.strftime("%Y-%m-%d %H:%M")`
para formatar.

---

Importa `datetime` e `timedelta`. Analisa para um datetime, adiciona o
timedelta, e depois devolve o strftime do resultado. Horas negativas
funcionam da mesma forma.

---

from datetime import datetime, timedelta


def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    dt = dt + timedelta(hours=hours)
    return dt.strftime("%Y-%m-%d %H:%M")
""",

"13.8 reference": r"""A tarefa final é a **viagem de ida e volta** completa através do módulo,
compondo três das suas ferramentas:

1. **Analisar** — `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")` lê a
   cadeia e produz um `datetime`.
2. **Deslocar** — adicionar `timedelta(hours=h)` move-o por uma duração,
   avançando automaticamente ao longo de minutos, dias, meses e anos (e para
   trás no caso de `h` negativo).
3. **Formatar** — `.strftime("%Y-%m-%d %H:%M")` apresenta o resultado de
   volta no mesmo formato.

O objetivo do capítulo numa única função: cada caso complicado — uma hora que
atravessa a meia-noite, um dia que passa para um novo mês ou ano, um dia
bissexto — é tratado pelos tipos de `datetime`, não por ti. Tu descreves os
passos; a biblioteca mantém o calendário honesto.

```python
from datetime import datetime, timedelta

def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    return (dt + timedelta(hours=hours)).strftime("%Y-%m-%d %H:%M")

add_hours("2026-06-20 23:30", 2)    # '2026-06-21 01:30'
```
""",
}
