`import json` at the top. The function you want is `json.dumps`, which takes a
Python object and returns its JSON text.

---

`json.dumps(record)` does the whole job. The function body is one line that
returns it.

---

import json


def to_json(record):
    return json.dumps(record)
