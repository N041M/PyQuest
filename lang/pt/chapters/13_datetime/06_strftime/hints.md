Analisa a data com `date.fromisoformat(text)` e depois chama `.strftime(...)`
sobre ela com o formato que queres.

---

A cadeia de formato para DD/MM/YYYY é `"%d/%m/%Y"`. As barras são copiadas
literalmente; os códigos preenchem os números com zeros.

---

from datetime import date


def pretty(text):
    return date.fromisoformat(text).strftime("%d/%m/%Y")
