Analisa primeiro a cadeia para uma data com `date.fromisoformat(text)`. Um
objeto de data consegue dizer-te o seu dia da semana.

---

`.weekday()` devolve 0 para segunda-feira até 6 para domingo. Chama-o sobre a
data analisada e devolve o resultado.

---

from datetime import date


def weekday(text):
    return date.fromisoformat(text).weekday()
