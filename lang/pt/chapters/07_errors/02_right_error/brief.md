# 7.2 -- Apanha o erro CERTO

## Conceito

`except` pode indicar qual o erro que trata -- e deve fazê-lo. Erros que não
esperavas são **informação**, e engoli-los esconde bugs.

```python
try:
    n = int(text)
except ValueError:        # exactly the error int() raises for bad TEXT
    n = None
```

O atalho tentador é um `except:` (ou `except Exception:`) sem nome -- "apanha
tudo, não pode falhar!" Mas *tudo* inclui erros que significam que **o teu
código está a ser usado incorretamente**. `int([1, 2])` não levanta um
`ValueError` -- levanta um `TypeError` ("um tipo de coisa completamente
errado"), e esse *deveria* falhar ruidosamente para que o bug de quem chamou
a função seja encontrado, não escondido.

A regra: **apanha exatamente o que esperas; deixa tudo o resto escapar.**

## Exemplo

```python
safe_int("42")      # 42
safe_int("nope")    # None         (ValueError, handled)
safe_int([1, 2])    # TypeError!   (NOT handled -- a misuse, let it crash)
```

## A tua tarefa

Define `safe_int(text)` que devolve `int(text)`, ou `None` quando o texto não
é um número válido. Apanha **apenas** `ValueError` -- um `TypeError` vindo de
algo que não é uma string tem de escapar.

## Está feito quando

- `safe_int("42")` é `42`; `safe_int("-7")` é `-7`.
- `safe_int("nope")` e `safe_int("")` são `None`.
- `safe_int([1, 2])` levanta `TypeError` -- o verificador chama-o de propósito
  com uma lista, por isso apanhar de mais falha.
