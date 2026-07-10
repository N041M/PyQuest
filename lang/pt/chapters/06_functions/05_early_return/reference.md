Um `return` pode aparecer **em qualquer lugar** de uma função, e alcançá-lo termina a chamada de
imediato — as linhas seguintes não correm. Um **retorno antecipado** usa isto para tratar um caso e
sair de imediato.

- Achata o código: trata o caso especial ou inválido logo à cabeça com uma guarda
  (`if bad: return ...`), depois escreve o caminho principal sem o aninhar num
  `else`.
- O primeiro `return` alcançado vence; nada depois dele nessa chamada é executado.

```python
def reciprocal(n):
    if n == 0:
        return None     # bail out early on the bad case
    return 1 / n        # main path, not indented under an else
```
