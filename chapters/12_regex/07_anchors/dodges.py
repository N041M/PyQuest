DODGES = [
    ("validates by hand with length and isdigit, never importing re",
     "def is_valid_code(text):\n"
     "    return (len(text) == 6 and text[:2].isalpha()\n"
     "            and text[:2].isupper() and text[2:].isdigit())\n"),
]
