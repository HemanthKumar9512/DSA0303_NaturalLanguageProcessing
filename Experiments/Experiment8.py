import random

tags = {
    "I": ["PRON"],
    "like": ["VERB"],
    "Python": ["NOUN"],
    "good": ["ADJ"]
}

text = "I like Python"

for word in text.split():
    print(word, "->", random.choice(tags.get(word, ["NOUN"])))
