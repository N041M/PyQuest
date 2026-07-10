O capstone é o verdadeiro ponto do capítulo: **compor módulos da
biblioteca padrão** num pequeno pipeline em vez de escrever cada passo de
raiz.

- **Ler** com `json` — `json.loads(text)` transforma a entrada JSON em
  valores Python (aqui, uma lista de números).
- **Resumir** com `statistics` e os nativos — `statistics.mean(nums)` para a
  média, `max(nums)` / `min(nums)` para os extremos, `len(nums)` para a
  contagem.
- **Devolver** um `dict` simples, para que quem chama a função receba valores
  Python comuns para usar.

Cada etapa é um módulo que outra pessoa escreveu e testou; o teu trabalho
é ligá-los entre si. É isso que a maioria dos programas reais são — cola
entre bibliotecas bem feitas.

```python
import json
import statistics

def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {"count": len(nums), "mean": statistics.mean(nums),
            "max": max(nums), "min": min(nums)}

summary("[2, 4, 6]")   # {'count': 3, 'mean': 4, 'max': 6, 'min': 2}
```
