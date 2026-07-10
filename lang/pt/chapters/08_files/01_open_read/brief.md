# 8.1 -- Abrir um ficheiro

## Conceito

Até agora todos os valores vinham de um literal que escreveste ou de `input()`.
Os programas a sério também leem **ficheiros** -- texto já guardado em disco.

`open(name)` dá-te um *objeto de ficheiro*. A forma correta de o usar é um bloco
`with`:

```python
with open("note.txt") as f:
    text = f.read()
```

- `with open(...) as f:` abre o ficheiro e associa-o a `f`;
- `f.read()` devolve **todo o conteúdo** do ficheiro como uma única cadeia de
  caracteres;
- quando o bloco termina, o Python **fecha o ficheiro por ti** -- mesmo que o
  código lá dentro tenha gerado um erro. Esse fecho automático é a única razão
  para preferires `with` a um `open()` isolado.

O ficheiro é procurado em relação ao local onde o programa corre, por isso
`"note.txt"` significa "um ficheiro chamado note.txt ao meu lado".

## Exemplo

Se `note.txt` contiver:

```
buy milk
call sam
```

então `text` é a cadeia de caracteres `"buy milk\ncall sam\n"` -- com as
quebras de linha incluídas.

## A tua tarefa

Existe um ficheiro chamado `note.txt` ao lado do teu programa. Lê todo o seu
conteúdo e imprime-o.

## Está feito quando

- O programa imprime exatamente o que `note.txt` contém.
- Funciona seja qual for o conteúdo do ficheiro -- uma linha, várias linhas, ou
  nenhuma.
- Abriste o ficheiro com uma instrução `with`.
