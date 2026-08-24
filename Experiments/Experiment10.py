words = "I am running fast".split()

tags = ["NOUN"] * len(words)

# Transformation rules
for i, word in enumerate(words):
    if word == "I":
        tags[i] = "PRON"
    elif word == "am":
        tags[i] = "VERB"
    elif word.endswith("ing"):
        tags[i] = "VERB"

for w, t in zip(words, tags):
    print(w, "->", t)
