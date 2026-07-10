# 2.7 -- Limpar texto

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
