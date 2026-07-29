import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from collections import Counter

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True) # Added to resolve LookupError

# 1. Define the corpus
corpus_raw = [
    "Students learn NLP.",
    "Students learn Python.",
    "Students write code.",
    "Teachers teach NLP."
]

corpus_processed = []
for sentence in corpus_raw:
    corpus_processed.append(sentence.lower())

text = " ".join(corpus_processed)

print("--- Processed Corpus ---")
print(text)

# 2. Tokenize the text into words
tokens = word_tokenize(text)
tokens = [word for word in tokens if word.isalpha()]

print("\n--- Tokens ---")
print(tokens)

# 3. Generate unigram and bigram frequency counts
unigram_freq = Counter(tokens)
bigram_list = list(bigrams(tokens))
bigram_freq = Counter(bigram_list)

print("\n--- Unigram Frequencies ---")
for word, freq in unigram_freq.items():
    print(f"{word}: {freq}")

print("\n--- Bigram Frequencies ---")
for bg, freq in bigram_freq.items():
    print(f"{bg}: {freq}")

# 4. Calculate vocabulary size (V)
vocabulary = set(tokens)
V = len(vocabulary)
print(f"\nVocabulary Size (V): {V}")
