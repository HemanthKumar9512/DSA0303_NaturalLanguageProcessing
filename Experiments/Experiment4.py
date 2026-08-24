def plural(word):
    if word.endswith(("s", "sh", "ch", "x")):
        return word + "es"
    return word + "s"

for w in ["cat", "bus", "box", "book"]:
    print(w, "->", plural(w))
