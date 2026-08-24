import re

def tag(word):
    if re.match(r".*ing$", word):
        return "VBG"
    if re.match(r".*ly$", word):
        return "ADV"
    if re.match(r".*ed$", word):
        return "VBD"
    return "NOUN"

for w in "John is running quickly".split():
    print(w, tag(w))
