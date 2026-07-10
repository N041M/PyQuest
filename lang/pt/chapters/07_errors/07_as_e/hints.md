O `as e` vai mesmo na linha do except: except ValueError as e:

---

Dentro do bloco except, basta print(e) -- o objeto imprime-se como a sua
mensagem.

---

line = input()
try:
    print(int(line))
except ValueError as e:
    print(e)
