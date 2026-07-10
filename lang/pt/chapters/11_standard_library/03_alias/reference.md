**`import module as alias`** importa um módulo, mas associa-o a um nome à tua
escolha. `import statistics as stats` torna o módulo disponível como `stats`;
`stats.mean` *é* `statistics.mean` — o alias só muda o nome local, não
o módulo.

- Usa-o para **encurtar** o nome longo de um módulo ou para **evitar um
  conflito** com um teu. Os aliases convencionais que vais encontrar (`import numpy as
  np`) são exatamente isto.
- O mesmo `as` funciona num único nome de um from-import: `from statistics
  import mean as avg`.
- Só o teu ficheiro vê o alias; outros módulos mantêm os seus próprios nomes
  para ele.

```python
import statistics as stats

stats.mean([1, 2, 3, 4])     # 2.5
stats.median([1, 5, 2])      # 2
```
