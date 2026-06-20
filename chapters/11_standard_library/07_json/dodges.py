DODGES = [
    ("glues the JSON string together by hand, never importing json",
     "def to_json(record):\n"
     "    return \"{\" + \", \".join('\"%s\": %d' % (k, v)\n"
     "                            for k, v in record.items()) + \"}\"\n"),
]
