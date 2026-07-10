`import json` no topo. A função que queres é `json.dumps`, que recebe um
objeto Python e devolve o seu texto JSON.

---

`json.dumps(record)` faz todo o trabalho. O corpo da função é uma linha
que o devolve.

---

import json


def to_json(record):
    return json.dumps(record)
