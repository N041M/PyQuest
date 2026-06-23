`import json` nahoře. Funkce, kterou chceš, je `json.dumps`, která bere pythonovský
objekt a vrací jeho JSON text.

---

`json.dumps(record)` udělá celou práci. Tělo funkce je jeden řádek, který ho vrátí.

---

import json


def to_json(record):
    return json.dumps(record)
