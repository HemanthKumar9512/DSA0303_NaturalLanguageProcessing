# Porter Stemmer using NLTK

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download required resources (Run only once)
nltk.download('punkt')

# Create Porter Stemmer object
ps = PorterStemmer()

# Input sentence
text = input("Enter a sentence: ")

# Tokenize the sentence into words
words = word_tokenize(text)

print("\nOriginal Words -> Stemmed Words")
print("--------------------------------")

# Apply stemming
for word in words:
    print(f"{word} -> {ps.stem(word)}")
