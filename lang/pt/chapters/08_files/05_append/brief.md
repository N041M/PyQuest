# 8.5 -- Anexar, não substituir

## Concept

O modo `"w"` é impiedoso: **esvazia** o ficheiro antes de escrever. Isso está
errado quando queres *acrescentar* a um ficheiro -- um registo (log) que vais
fazendo crescer, por exemplo. Para isso existe o modo `"a"` (de *append*,
anexar):

```python
with open("log.txt", "a") as f:
    f.write("another line\n")
```

`"a"` deixa intacto tudo o que já está no ficheiro e escreve o teu novo texto
**depois** disso (e se o ficheiro ainda não existir, `"a"` simplesmente
cria-o). O mesmo `.write()`, a mesma necessidade de acrescentares o teu
próprio `"\n"` -- só a letra do modo muda, e essa letra é toda a diferença
entre "acrescentar a" e "apagar e substituir". Todo o objetivo do `"a"` é que
*não* leias o ficheiro primeiro -- limitas-te a escrever no fim.

## Exemplo

Se `log.txt` já contiver:

```
woke up
ate
```

então anexar a linha `ran` deixa-o com `woke up`, `ate`, `ran` -- as três, por
ordem.

## A tua tarefa

Já existe um ficheiro `log.txt`. Lê uma linha de texto da entrada (`input()`)
e **anexa-a** a `log.txt` como uma nova linha, mantendo tudo o que já lá
estava.

## Está feito quando

- O conteúdo original de `log.txt` continua presente, por ordem.
- A nova entrada é adicionada como a sua própria linha no fim.
- Usar `"w"` apagaria as linhas antigas -- por isso tens de usar `"a"`.
