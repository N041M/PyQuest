Cada etapa é o seu próprio pequeno gerador. `numbers` percorre `range(n)` e
produz; `keep_even` percorre `stream` e produz apenas os pares; `labelled`
percorre `stream` e produz uma cadeia de caracteres formatada. Nenhum deles
constrói uma lista.

---

`keep_even` e `labelled` recebem um `stream` e `for x in stream:` -- esse
ciclo funciona quer `stream` seja uma lista quer outro gerador, o que é o
que te permite aninhá-los. Usa uma f-string para a etiqueta:
`yield f"#{x}"`.

---

def numbers(n):
    for i in range(n):
        yield i


def keep_even(stream):
    for x in stream:
        if x % 2 == 0:
            yield x


def labelled(stream):
    for x in stream:
        yield f"#{x}"
