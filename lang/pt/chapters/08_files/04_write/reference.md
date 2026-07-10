Abrir com o modo **`"w"`** abre um ficheiro para **escrita**. **Cria** o
ficheiro se não existir e **trunca-o** (esvazia-o) se já existir, pelo que o
conteúdo anterior é perdido.

- **`f.write(text)`** escreve uma cadeia de caracteres e, ao contrário do
  `print`, não acrescenta **nenhuma** quebra de linha final — inclui tu mesmo
  `"\n"` onde quiseres quebras de linha.
- `f.write` aceita apenas cadeias de caracteres; converte números com `str()`
  ou com uma f-string primeiro.
- Usa `with` para que os dados sejam gravados e o ficheiro fechado
  corretamente.

```python
with open("out.txt", "w") as f:
    f.write("first line\n")
    f.write("second line\n")   # newlines are explicit
```
