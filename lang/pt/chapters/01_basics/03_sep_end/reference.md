`sep` e `end` são argumentos exclusivamente nomeados que controlam o espaçamento à volta
do resultado de um `print`.

- **`sep`** é a cadeia inserida entre cada par de valores adjacentes. O valor por
  omissão é `" "`. Nunca aparece antes do primeiro valor nem depois do último,
  por isso *N* valores produzem *N − 1* separadores.
- **`end`** é a cadeia escrita uma vez, depois do último valor. O valor por omissão é
  `"\n"`, motivo pelo qual cada `print` termina a sua linha. Define `end=""` para deixar o
  cursor na mesma linha, para que o próximo `print` a continue.

```python
print("2024", "01", "15", sep="-")   # 2024-01-15
print("loading", end="")
print("...")                          # loading... (one line)
```
