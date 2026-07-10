# 1.10 -- Perguntar ao utilizador

## Conceito

`input()` pausa o programa, deixa a pessoa escrever uma linha, e **devolve o que
ela escreveu como texto** (uma cadeia de caracteres). Normalmente guardas isso numa variável:

```python
name = input()
print("Hi, " + name)
```

Se a pessoa escrever `Sam`, o programa imprime `Hi, Sam`.

`input()` devolve sempre uma **cadeia de caracteres**, mesmo que a pessoa escreva dígitos. (Vais
lidar com isso no próximo puzzle.)

Podes juntar o texto escrito com outro texto usando `+`, tal como no puzzle 1.7:

```python
city = input()
print("You live in " + city)
```

> Nota: quando corres `check`, o verificador fornece a entrada por ti automaticamente
> -- não precisas de escrever nada à mão.

## Exemplo

Entrada escrita: `Berlin`

```python
city = input()
print("Welcome to " + city)
```

Resultado:

```
Welcome to Berlin
```

## A tua tarefa

Lê uma linha de entrada (um nome) e cumprimenta-a. Se a entrada for `World`, o resultado
tem de ser exatamente:

```
Hello, World
```

Portanto: lê o nome com `input()`, depois imprime `Hello, ` unido ao nome. Presta atenção
à vírgula e ao único espaço depois dela.

## Está feito quando

- Dada a entrada `World`, o resultado é `Hello, World`.
- Dado qualquer outro nome, cumprimenta esse nome da mesma forma (o verificador tenta
  mais do que um).
