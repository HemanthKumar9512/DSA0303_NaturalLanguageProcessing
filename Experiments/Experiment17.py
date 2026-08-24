from nltk.corpus import wordnet

word = "car"

for syn in wordnet.synsets(word):
    print(syn.name())
    print(syn.definition())
