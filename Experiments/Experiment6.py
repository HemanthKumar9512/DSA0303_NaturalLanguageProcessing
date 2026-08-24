import random

text = "I like NLP and I like Python"
words = text.split()

bigrams = list(zip(words, words[1:]))

word = "I"
result = [word]

for i in range(5):
    next_words = [b for a, b in bigrams if a == word]
    if not next_words:
        break
    word = random.choice(next_words)
    result.append(word)

print(" ".join(result))
