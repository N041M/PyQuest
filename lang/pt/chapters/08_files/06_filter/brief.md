# 8.6 -- Filtrar linhas para um novo ficheiro

## Conceito

Junta a leitura e a escrita e obténs a tarefa quotidiana de dados: percorrer
um ficheiro de entrada linha a linha, **decidir** que linhas manter (3.2
`if`), e escrever apenas essas num ficheiro de saída.

```python
with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if keep(line):
            f.write(line)
```

`f.readlines()` lê o ficheiro inteiro para uma lista de linhas de uma vez --
útil quando queres terminar de ler antes de começares a escrever.

Uma linha vazia ou só com espaços está "em branco": `line.strip()` devolve
`""` para ela, e uma cadeia de caracteres vazia é falsa (*falsey*, 3.1), por
isso `if line.strip():` é um teste limpo para "esta linha tem conteúdo real".

## Exemplo

A partir de um `lines.txt` de:

```
keep me

and me
```

a linha vazia do meio é descartada, ficando `keep me` e `and me`.

## A tua tarefa

Lê `lines.txt` e escreve apenas as suas linhas **não vazias** em `kept.txt`,
pela mesma ordem. Descarta qualquer linha que esteja vazia ou seja só espaço
em branco.

## Está feito quando

- `kept.txt` contém exatamente as linhas não vazias de `lines.txt`, por ordem.
- Um ficheiro sem linhas em branco é copiado sem alterações; um ficheiro todo
  em branco produz um `kept.txt` vazio.
- Usaste `with`, um ciclo, e um `if` para decidir o que manter.
