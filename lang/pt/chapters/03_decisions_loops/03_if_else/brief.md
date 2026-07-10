# 3.3 -- if / else

## Conceito

O `else` dá ao `if` um segundo ramo: código a executar quando a condição é
**False**. Executa-se exatamente um dos dois blocos.

```python
if temperature > 30:
    print("hot")
else:
    print("not hot")
```

O `else:` alinha-se com o `if` (mesma indentação), e o seu bloco é indentado
tal como o bloco do `if`.

## Um lembrete

`n % 2` é o resto da divisão de `n` por 2 (conheceste o `%` no capítulo 1). Um
número é **par** exatamente quando `n % 2 == 0`.

## Exemplo

```python
n = 7
if n % 2 == 0:
    print("even")
else:
    print("odd")
# prints: odd
```

## A tua tarefa

Lê um número inteiro e imprime `even` se for par, ou `odd` se não for.

Para a entrada `10` a saída é:

```
even
```

## Está feito quando

- Números pares imprimem `even`, números ímpares imprimem `odd`.
- Funciona para `0` (par) e também para números negativos.
