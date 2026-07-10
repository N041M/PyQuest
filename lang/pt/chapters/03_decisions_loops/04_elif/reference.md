O **`elif`** ("else if") acrescenta mais ramos entre o `if` e o `else`. O Python verifica
cada condição **por ordem** e executa o bloco da **primeira** que for verdadeira,
ignorando as restantes. Um `else` final opcional trata o caso "nenhuma correspondeu".

- Apenas um ramo é executado — o primeiro que for verdadeiro. As condições seguintes nem
  sequer são avaliadas.
- Como a primeira correspondência vence, a ordem importa: coloca os testes mais
  específicos ou de maior prioridade primeiro.
- Uma cadeia de `elif` é mais plana e clara do que aninhar um `if` dentro de cada
  `else`.

```python
if score >= 90:
    grade = "A"
elif score >= 80:       # only checked if the first was False
    grade = "B"
else:
    grade = "C"
```
