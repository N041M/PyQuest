int("seven") levanta um ValueError -- põe a conversão dentro de um bloco try.

---

try: converte e imprime o dobro. except ValueError: imprime a mensagem.
O bloco except só corre quando a conversão falhou.

---

line = input()
try:
    n = int(line)
    print(n * 2)
except ValueError:
    print("not a number")
