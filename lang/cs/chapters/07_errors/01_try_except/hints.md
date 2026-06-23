int("seven") vyvolá ValueError -- dej převod dovnitř bloku try.

---

try: převeď a vypiš dvojnásobek. except ValueError: vypiš zprávu.
Blok except se spustí jen tehdy, když převod selhal.

---

line = input()
try:
    n = int(line)
    print(n * 2)
except ValueError:
    print("not a number")
