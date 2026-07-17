# Finite State Machine for English Plural Formation

def pluralize(word):

    irregular = {
        "child": "children",
        "man": "men",
        "woman": "women",
        "mouse": "mice",
        "goose": "geese",
        "tooth": "teeth",
        "foot": "feet",
        "person": "people",
        "ox": "oxen"
    }

    # State 1: Check irregular nouns
    if word.lower() in irregular:
        return irregular[word.lower()]

    # State 2: Ends with s, x, z, ch, sh
    elif word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"

    # State 3: Ends with consonant + y
    elif word.endswith("y") and len(word) > 1 and word[-2].lower() not in "aeiou":
        return word[:-1] + "ies"

    # State 4: Ends with fe
    elif word.endswith("fe"):
        return word[:-2] + "ves"

    # State 5: Ends with f
    elif word.endswith("f"):
        return word[:-1] + "ves"

    # State 6: Default rule
    else:
        return word + "s"


word = input("Enter a singular noun: ")

print("Plural:", pluralize(word))
