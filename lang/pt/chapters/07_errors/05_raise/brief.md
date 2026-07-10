# 7.5 -- raise: os erros também são teus

## Conceito

Até agora tens *apanhado* erros que o Python levantou. Também podes
**levantar os teus próprios** -- e boas funções fazem-no, assim que lhes é
entregue algo sem sentido:

```python
def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

`raise` cria o erro e lança-o ali mesmo: a função para, e quem a chamou
recebe o mesmo tratamento que `int("nope")` dá -- apanhável com `try`,
ruidoso se ignorado.

Porquê levantar em vez de devolver algo como `None` ou `-1`? Porque um valor
errado viaja: é guardado, somado, impresso, e a falha (se houver) acontece
longe do erro real. Um raise fixa a falha no momento e na mensagem --
`ValueError("age cannot be negative")` diz exatamente o que correu mal, e
onde correu mal. Lixo à entrada, **erro** à saída -- nunca lixo à saída.

## Exemplo

```python
checked_age(30)     # 30
checked_age(0)      # 0    -- zero is a fine age
checked_age(-1)     # ValueError: age cannot be negative
```

## A tua tarefa

Define `checked_age(age)` que devolve a idade sem alterações -- mas levanta
um `ValueError` quando ela é negativa. Dá-lhe uma mensagem que diga o que
está errado.

## Está feito quando

- `checked_age(30)` devolve `30`; `checked_age(0)` devolve `0`.
- `checked_age(-1)` levanta `ValueError`.
- Usaste `raise` -- o verificador procura a própria instrução.
