# 1.3 -- Escolher o separador

## Conceito

Quando dás ao `print` vários valores, ele junta-os com um espaço por omissão. Podes
mudar essa cadeia de junção com uma configuração especial chamada **`sep`** (abreviatura de
*separator*, separador).

Uma configuração como esta escreve-se `nome=valor` dentro dos parênteses, depois dos
teus valores:

```python
print("a", "b", "c", sep="-")
```

mostra:

```
a-b-c
```

`sep="-"` diz ao `print` para colocar um traço entre os valores em vez de um espaço. O
separador só aparece *entre* valores -- nunca antes do primeiro nem depois do último.
Podes usar qualquer texto como separador: `sep=", "`, `sep=""` (nada), `sep="/"`,
e assim por diante.

`sep` tem de ser escrito exatamente assim, sem espaço antes do `=`, e o valor entre
aspas porque é texto.

## Exemplo

```python
print("home", "user", "docs", sep="/")
```

mostra:

```
home/user/docs
```

## A tua tarefa

Imprime esta data exata, usando três **números** unidos por traços:

```
2024-12-25
```

Passa `2024`, `12`, `25` a um único `print` e define `sep` para que sejam unidos com
`-`. Não escrevas os traços como parte do texto tu mesmo.

## Está feito quando

- O resultado é exatamente `2024-12-25`.
- Vem de três números mais uma configuração `sep`, não de uma cadeia escrita à mão.
