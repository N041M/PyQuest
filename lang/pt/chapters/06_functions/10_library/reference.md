Uma **biblioteca** aqui significa um conjunto de funções relacionadas que escreveste, cada uma nomeada
pelo seu trabalho, que juntas formam um conjunto de ferramentas reutilizável — a recompensa do capítulo.

- Constrói funções pequenas que fazem cada uma uma coisa e devolvem (`return`) o seu resultado; depois
  as funções de nível superior chamam-nas. O código que as chama lê-se como uma sequência de intenções.
- Manter a lógica dentro de funções nomeadas (em vez de copiada em linha) significa que uma correção ou
  melhoria acontece num só sítio e todos os que chamam beneficiam.

```python
def clean(s):    return s.strip().lower()
def words(s):    return clean(s).split()
def wordcount(s): return len(words(s))

wordcount("  The quick fox ")   # 3  -- each function builds on the last
```
