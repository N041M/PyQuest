# 3.11 -- break e continue

## Conceito

Duas palavras-chave alteram o fluxo de um ciclo:

- **`break`** para o ciclo **imediatamente** -- não há mais passagens.
- **`continue`** salta o **resto da passagem atual** e avança para a
  seguinte.

```python
for ch in "a,b,c":
    if ch == ",":
        continue        # skip commas
    print(ch)
# prints a, b, c (commas skipped)

for n in range(100):
    if n == 3:
        break           # stop the whole loop at 3
    print(n)
# prints 0, 1, 2
```

O `continue` salta um item; o `break` termina o ciclo.

## Exemplo

```python
for ch in "abxcd":
    if ch == "x":
        break
    print(ch)
# prints a, b   (stops at x)
```

## A tua tarefa

Lê uma palavra e percorre os seus caracteres:

- **salta** a letra `o` (usa `continue` -- não a imprimas),
- **para** completamente na letra `x` (usa `break` -- não imprimas nada a partir
  do `x`),
- imprime todos os outros caracteres, cada um na sua própria linha.

Para a entrada `boxes` a saída é:

```
b
```

(`b`, depois `o` é saltado, depois `x` para o ciclo.)

## Está feito quando

- `boxes` imprime `b`; `good` imprime `g` e depois `d` (os `o`s são saltados);
  `abc` imprime `a`, `b`, `c`.
