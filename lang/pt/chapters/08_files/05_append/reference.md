O modo **`"a"`** abre um ficheiro para **anexar** (append): as escritas vão
para o **fim**, e todo o conteúdo existente é mantido. É o equivalente não
destrutivo de `"w"`.

- `"a"` cria o ficheiro se não existir; se existir, `f.write` acrescenta
  depois do que já lá está — nada é substituído.
- `"w"` esvazia o ficheiro primeiro; recorre a `"a"` para fazer crescer um
  registo (log) ou acumular resultados entre execuções.
- Tal como com `"w"`, as quebras de linha não são adicionadas por ti.

```python
with open("log.txt", "a") as f:
    f.write("another entry\n")   # added at the end, old lines kept
```
