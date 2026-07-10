# 2.10 -- f-strings

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
