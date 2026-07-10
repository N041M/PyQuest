Um **tuplo** é uma sequência ordenada e **imutável**, escrita com vírgulas
(frequentemente entre parênteses): `(3, 4)`, ou apenas `3, 4`. Uma vez criado, não
pode ser alterado.

- O **desempacotamento** atribui os itens de uma sequência a vários nomes de uma
  só vez: `a, b = point`. A contagem em cada lado tem de corresponder.
- Isto permite a **troca** numa só linha `a, b = b, a`: o lado direito é primeiro
  construído como um tuplo, e depois desempacotado, por isso não é preciso nenhuma
  variável temporária.
- Usa um tuplo para um grupo fixo de valores relacionados (uma coordenada, um
  registo); usa uma lista quando a coleção cresce ou muda.

```python
point = (3, 4)
x, y = point        # x = 3, y = 4
a, b = b, a         # swap in one line
```
