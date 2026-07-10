while True à volta de um try: converte e break; o except simplesmente volta
a tentar.

---

except ValueError: pass -- `pass` significa "não faças nada", o que aqui
significa "tenta outra vez". Imprime DEPOIS do ciclo, onde n está garantido
que é bom.

---

while True:
    try:
        n = int(input())
        break
    except ValueError:
        pass
print(n * 2)
