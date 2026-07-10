# 5.1 -- in: testar pertença

## Conceito

Encontraste o `in` com conjuntos (4.11). Na verdade funciona em quase tudo:

```python
"e" in "hello"        # True   (substring of a string)
3 in [1, 2, 3]        # True   (item of a list)
"sam" in {"sam": 20}  # True   (KEY of a dict)
```

`x in s` é uma expressão que dá um **booleano** (`True`/`False`), por isso
encaixa diretamente num `if`:

```python
if "@" in address:
    print("looks like an email")
```

Também existe o oposto, `not in`:

```python
if "x" not in word:
    print("no x here")
```

Compara com o capítulo 2, onde usaste `s.find()` e verificaste `-1`.
O `in` diz a mesma coisa em linguagem simples -- prefere-o sempre que só precises de saber
*se* algo está lá, não *onde*.

## Exemplo

```python
word = "banana"
print("n" in word)     # True
print("z" in word)     # False
```

## A tua tarefa

Lê uma palavra, depois uma única letra. Imprime `yes` se a letra aparecer na
palavra, e `no` se não aparecer.

Para a entrada `banana`, depois `n`:

```
yes
```

## Está feito quando

- Uma letra que aparece imprime `yes`; uma que não aparece imprime `no`.
- Também funciona para uma palavra de uma letra.
- Usaste o operador `in` (não `.find()` nem `.count()`).
