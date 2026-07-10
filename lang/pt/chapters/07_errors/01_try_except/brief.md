# 7.1 -- try / except

## Conceito

Já *causaste* bastantes erros até agora. Chegou a altura de **tratares** de um.

Quando o Python encontra algo impossível -- como `int("hello")` -- **levanta uma
exceção**: o fluxo normal para de repente e, a menos que alguém trate disso, o
programa falha com um traceback. `try`/`except` é a forma de tratares disso:

```python
try:
    n = int(text)
    print("a number!")
except ValueError:
    print("not a number")
```

Como isto funciona:

- O bloco `try` corre normalmente -- **até** uma linha levantar uma exceção.
- Se nada levantar uma exceção, o bloco `except` é ignorado por completo.
- Se `int(text)` levantar um `ValueError` (a sua queixa sobre texto que não é
  convertível), o resto do bloco `try` é abandonado e o bloco `except` corre
  em vez disso. **Sem falha.**

O programa *recupera*: escolheu o que a falha significa, em vez de simplesmente cair.

## Exemplo

A entrada `7` imprime `14`. A entrada `seven` imprime `not a number` -- o mesmo
código, sem falhar em nenhum dos casos.

## A tua tarefa

Lê uma linha. Se ela se converter num número inteiro, imprime esse número
**duplicado**. Se não se converter, imprime exatamente `not a number`. (Este é
outra vez um puzzle de script: `input()` e `print()` estão de volta.)

## Está feito quando

- `7` imprime `14`; `-3` imprime `-6`.
- `seven` e `12abc` imprimem `not a number` -- e o programa termina de forma
  limpa, sem traceback.
- Usaste `try`/`except` -- o verificador exige mesmo isso.
