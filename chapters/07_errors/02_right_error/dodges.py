# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("bare except swallows everything -- a TypeError must escape",
     "def safe_int(text):\n"
     "    try:\n"
     "        return int(text)\n"
     "    except:\n"
     "        return None\n"),
    ("except Exception is still too broad -- TypeError must escape",
     "def safe_int(text):\n"
     "    try:\n"
     "        return int(text)\n"
     "    except Exception:\n"
     "        return None\n"),
]
