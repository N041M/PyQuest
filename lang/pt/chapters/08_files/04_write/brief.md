# 8.4 -- Escrever num ficheiro

## Conceito

Ler é metade da história; os programas também **criam** ficheiros. Abre com o
modo `"w"` (de *write*, escrita) e chama `.write()`:

```python
with open("out.txt", "w") as f:
    f.write("hello\n")
```

Duas coisas a saber:

- `"w"` cria um ficheiro novo em folha (ou **esvazia** um já existente), e só
  depois escreve.
- `.write()` coloca **exatamente** o texto que lhe dás -- sem a quebra de
  linha automática que o `print()` acrescenta. Se quiseres quebras de linha,
  inclui tu mesmo o `"\n"`.

Um padrão comum é **ler um ficheiro, escrever noutro**:

```python
with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
```

## Exemplo

Se `in.txt` contiver `quiet please`, então `out.txt` deve acabar por conter
`QUIET PLEASE`.

## A tua tarefa

Lê `in.txt`, e escreve o seu conteúdo **em maiúsculas** (`.upper()` de 2.7)
num novo ficheiro chamado `out.txt`.

## Está feito quando

- `out.txt` contém exatamente o texto de `in.txt`, em maiúsculas.
- Um `in.txt` vazio produz um `out.txt` vazio -- sem erro.
- Usaste `with` e abriste `out.txt` em modo `"w"`.
