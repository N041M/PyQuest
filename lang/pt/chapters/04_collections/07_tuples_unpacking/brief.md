# 4.7 -- Tuplos e desempacotamento

## Conceito

Um **tuplo** é como uma lista, mas **imutável** -- uma vez criado, não pode ser
alterado. Escreve-se um com parênteses (ou apenas com vírgulas):

```python
point = (3, 7)
print(point[0])    # 3
```

O **desempacotamento** atribui vários valores a várias variáveis de uma só vez, a
partir de um tuplo (ou lista):

```python
x, y = point       # x = 3, y = 7
```

Os nomes do lado esquerdo correspondem aos itens do lado direito, por ordem. Um
truque interessante que isto permite é **trocar** duas variáveis sem uma variável
temporária:

```python
a, b = 1, 2
a, b = b, a        # now a = 2, b = 1
```

O lado direito `b, a` constrói um tuplo, que é depois desempacotado para `a, b`.

## Exemplo

```python
a, b = 10, 20
a, b = b, a
print(a)    # 20
print(b)    # 10
```

## A tua tarefa

Lê dois números inteiros (cada um na sua própria linha). **Troca-os** usando
desempacotamento de tuplos, depois imprime o primeiro, depois o segundo.

Para a entrada `3` seguida de `7`:

```
7
3
```

## Está feito quando

- `3, 7` imprime `7` depois `3`.
- Funciona para quaisquer dois números (incluindo dois números iguais).
