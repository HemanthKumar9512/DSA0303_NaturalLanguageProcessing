import nltk
from nltk import word_tokenize, pos_tag

# Download the necessary NLTK data for POS tagging (if not already downloaded)
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

sentence = "The intelligent student quickly solved the problem."

tokens = word_tokenize(sentence)

tags = pos_tag(tokens)

print(tags)
