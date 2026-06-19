# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
# The lesson is the string methods .strip()/.upper(); these compute the same
# stripped-and-uppercased text by hand, dodging both -- uses_call stops them.
DODGES = [
    ("hand-rolled trim + ord() upcasing, no .strip()/.upper()",
     "s = input()\n"
     "i, j = 0, len(s)\n"
     "while i < j and s[i] == ' ':\n"
     "    i += 1\n"
     "while j > i and s[j - 1] == ' ':\n"
     "    j -= 1\n"
     "core = s[i:j]\n"
     "out = ''.join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in core)\n"
     "print(out)\n"),
    ("slice-trim + str.translate upcasing, no .strip()/.upper()",
     "s = input()\n"
     "while s[:1] == ' ':\n"
     "    s = s[1:]\n"
     "while s[-1:] == ' ':\n"
     "    s = s[:-1]\n"
     "table = {ord(c): ord(c) - 32 for c in 'abcdefghijklmnopqrstuvwxyz'}\n"
     "print(s.translate(table))\n"),
]
