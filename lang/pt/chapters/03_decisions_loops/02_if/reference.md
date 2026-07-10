Uma instrução **`if`** executa um bloco indentado **apenas quando** a sua condição é verdadeira.
A condição é avaliada como um booleano; se for verdadeira, o bloco é executado; se for falsa, é
ignorado e o programa continua abaixo.

- O bloco é definido pela **indentação** (por convenção, 4 espaços). Todas as linhas
  indentadas sob o `if` pertencem-lhe; a primeira linha de volta ao nível exterior
  termina-o.
- A condição não precisa de ser um `True`/`False` literal — qualquer valor é testado quanto
  à sua **veracidade** (*truthiness*): `0`, `0.0`, `""` e coleções vazias são falsos; tudo o
  resto é verdadeiro.

```python
if temperature > 30:
    print("hot")        # runs only when the test is True
print("done")           # always runs -- not indented under the if
```
