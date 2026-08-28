text = "John went to school. He studied Python."

sentences = text.split(".")

name = sentences[0].split()[0]

for word in sentences[1].split():
    if word == "He":
        print("He refers to", name)
