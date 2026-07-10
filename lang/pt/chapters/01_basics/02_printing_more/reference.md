Um programa corre de cima para baixo, por isso instruções `print` sucessivas produzem linhas
sucessivas — cada chamada emite os seus argumentos e depois uma quebra de linha.

Passar **vários valores a um só `print`**, separados por vírgulas, é diferente de
várias chamadas a `print`: os valores aparecem numa *única* linha, unidos por `sep` (um
espaço por omissão). Isto é separação por vírgulas na chamada, não concatenação de texto
— os valores mantêm os seus próprios tipos e são convertidos de forma independente.

```python
print("one")
print("two")          # two lines

print("x", "y", 3)    # one line:  x y 3
```
