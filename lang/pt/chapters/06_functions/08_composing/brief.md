# 6.8 -- Funções a chamar funções

## Conceito

As tuas funções podem chamar-se **umas às outras**. Esse é o verdadeiro golpe de mestre: resolve um
problema pequeno uma vez, dá-lhe um nome, e constrói a função seguinte em cima dele.

```python
def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
```

`same_word` não repete a receita de retirar espaços e minusculizar -- **delega** em
`clean`. Se alguma vez melhorares `clean` (digamos, removendo também pontuação), todas as
funções construídas sobre ela melhoram de graça. Repetir a receita nos dois sítios
é como nascem os bugs: corriges uma cópia, esqueces a outra.

Repara que `same_word` devolve o resultado de uma comparação -- um **booleano**
(`True`/`False`), como em 3.1. Não é preciso `if`: `clean(a) == clean(b)` já
*é* a resposta.

## Exemplo

```python
clean("  Tea ")              # "tea"
same_word("  Tea ", "tea")   # True
same_word("tea", "milk")     # False
```

## A tua tarefa

Define **ambas** as funções:

- `clean(text)` -- devolve o texto sem os espaços à volta e em minúsculas
  (2.7).
- `same_word(a, b)` -- devolve `True` exatamente quando os dois textos são iguais
  depois de limpos. Tem de **chamar `clean`** em vez de refazer a receita.

## Está feito quando

- `clean("  Tea ")` devolve `"tea"`.
- `same_word("  Tea ", "tea")` é `True`; `same_word("tea", "milk")` é `False`.
- `same_word` chama `clean` -- o verificador procura a delegação.
