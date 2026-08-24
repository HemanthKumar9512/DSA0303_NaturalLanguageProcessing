import nltk

text = "John plays football"

words = nltk.word_tokenize(text)
print(nltk.pos_tag(words))
