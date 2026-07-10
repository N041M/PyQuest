# 14.1 -- lambda: uma função numa expressão

## Conceito

Uma **`lambda`** é uma função minúscula escrita em linha, sem nome e sem `def`:

```python
double = lambda x: x * 2
double(5)      # 10
```

- `lambda args: expression` -- o valor da expressão é devolvido
  automaticamente (sem `return`, e só é permitida uma expressão).
- Uma lambda é um **valor**, por isso podes guardá-la, **devolvê-la** de outra
  função, ou passá-la como argumento (é aí que ela realmente mostra o seu valor --
  o resto deste capítulo).

Como uma lambda é definida dentro de outra função, ela pode **capturar** as
variáveis dessa função. `lambda x: x * n` recorda o `n` do local onde foi criada.

(Para algo mais longo do que uma expressão, usa um `def` normal -- as lambdas
são para pequenas funções em linha.)

## Exemplo

```python
def adder(n):
    return lambda x: x + n     # remembers n
```

## A tua tarefa

Define `multiplier(n)` que **devolve uma lambda** que multiplica o seu argumento
por `n`. Assim, `multiplier(3)` devolve uma função, e chamar essa função com `4`
dá `12`.

## Está feito quando

- `multiplier(3)(4)` é `12`; `multiplier(10)(5)` é `50`.
- `multiplier(0)(7)` é `0`.
- A função devolvida é uma `lambda`, não um `def` aninhado.
