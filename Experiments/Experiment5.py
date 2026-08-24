from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ["playing", "played", "running", "studies"]

for w in words:
    print(w, "->", ps.stem(w))
