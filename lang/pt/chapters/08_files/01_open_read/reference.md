**`open(name)`** liga-se a um ficheiro em disco; a instrução **`with`** gere-o
para que o ficheiro seja **fechado automaticamente** quando o bloco termina,
mesmo que ocorra um erro. Dentro do bloco, o objeto de ficheiro `f` fornece o
conteúdo.

- `with open(name) as f:` abre para **leitura** de texto (o modo predefinido
  `"r"`) e associa o ficheiro aberto a `f`.
- **`f.read()`** devolve todo o conteúdo como uma única cadeia de caracteres.
  (`f.read(n)` lê no máximo `n` caracteres.)
- Abrir um caminho que não existe gera `FileNotFoundError`. Usa sempre `with`
  em vez de um `open` isolado — garante o fecho.

```python
with open("notes.txt") as f:
    text = f.read()      # whole file as a string
# file is closed here
```
