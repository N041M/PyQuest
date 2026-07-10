# 11.3 -- import as: renomear à entrada

## Conceito

Às vezes o nome de um módulo é longo, ou entra em conflito com um teu. **`import ... as
...`** traz o módulo sob um nome que **tu** escolhes:

```python
import statistics as stats

stats.mean([1, 2, 3, 4])    # 2.5
```

- `import statistics as stats` associa o módulo a `stats`; `stats.mean` é
  exatamente `statistics.mean`.
- O alias é só uma alcunha local -- o módulo mantém-se inalterado, e só o teu
  ficheiro vê o novo nome.
- É por isso que vais ver aliases convencionais por todo o lado (`import numpy as np`);
  aqui encurtamos `statistics`.

O módulo **`statistics`** faz as médias mais comuns por ti. `stats.mean(nums)`
é a média aritmética -- a soma dividida pela contagem -- sem teres de escrever
`sum(nums) / len(nums)`.

## Exemplo

```python
import statistics as stats

def midpoint(nums):
    return stats.median(nums)
```

## A tua tarefa

Usando **`import statistics as stats`**, define `average(nums)` que devolve a
média da lista `nums`, calculada com `stats.mean`.

## Está feito quando

- `average([2, 4, 6])` devolve `4`, `average([1, 2])` devolve `1.5`.
- `average([5])` devolve `5`.
- A média vem de `statistics.mean`, importado como `stats`.
