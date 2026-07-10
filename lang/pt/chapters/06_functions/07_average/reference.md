As funções **compõem funções nativas** numa operação nomeada e reutilizável. Uma função
`average` é o modelo: embrulha `sum` e `len` atrás de um nome claro.

- `return sum(nums) / len(nums)` calcula a média — mas `len(nums)` é `0` para uma
  lista vazia, o que levanta `ZeroDivisionError`, por isso protege-a com um retorno antecipado.
- Nomear a operação (`average(scores)`) faz com que o código que a chama se leia como intenção, e
  corrigir ou melhorar a lógica acontece num só sítio.

```python
def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

average([2, 4, 9])    # 5.0
```
