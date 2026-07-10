Um `#` inicia um **comentário**: do `#` até ao fim dessa linha, o texto é
ignorado pelo Python. Os comentários explicam *porquê* o código faz algo; não têm
efeito no que corre.

- Um comentário pode estar na sua própria linha ou seguir código na mesma linha
  (`x = 1  # set up`).
- Um `#` dentro de uma string literal é apenas um carácter, não um comentário
  (`"#1"` é o texto `#1`).
- O Python **não tem sintaxe de comentário em bloco**: comenta cada linha com `#`, ou — para um
  bloco descartável — usa uma string literal, que é avaliada e descartada.

"Comentar" uma linha (colocar `#` à frente) é a forma mais rápida de a desativar
sem a apagar.

```python
# this whole line is ignored
print("hi")   # and this trailing note is too
```
