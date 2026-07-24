# Programming Challenge
# Corpus, Frequency Count and Probability Estimation

import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from collections import Counter
import matplotlib.pyplot as plt

# Download tokenizer (only first time)
nltk.download('punkt')

# Sample Corpus
text = """
Natural Language Processing is interesting.
Machine Learning is powerful.
Artificial Intelligence is transforming the world.
Natural Language Processing improves Artificial Intelligence.
"""

# -----------------------------
# Step 1: Tokenize the text
# -----------------------------
tokens = word_tokenize(text.lower())

# Remove punctuation
tokens = [word for word in tokens if word.isalpha()]

print("Tokens:")
print(tokens)

# -----------------------------
# Step 2: Build Corpus
# -----------------------------
print("\nCorpus:")
print(tokens)

# -----------------------------
# Step 3: Word Frequency
# -----------------------------
word_freq = Counter(tokens)

print("\nWord Frequency")
for word, freq in word_freq.items():
    print(f"{word} : {freq}")

# -----------------------------
# Step 4: Unigram Probability
# -----------------------------
total_words = len(tokens)

print("\nUnigram Probabilities")
for word, freq in word_freq.items():
    print(f"P({word}) = {freq}/{total_words} = {freq/total_words:.4f}")

# -----------------------------
# Step 5: Bigram Frequency
# -----------------------------
bigram_list = list(bigrams(tokens))
bigram_freq = Counter(bigram_list)

print("\nBigram Frequencies")
for bg, freq in bigram_freq.items():
    print(f"{bg} : {freq}")

# -----------------------------
# Step 6: Bigram Probability
# -----------------------------
print("\nBigram Probabilities")
for bg, freq in bigram_freq.items():
    first_word = bg[0]
    probability = freq / word_freq[first_word]
    print(f"P({bg[1]} | {bg[0]}) = {freq}/{word_freq[first_word]} = {probability:.4f}")

# -----------------------------
# Step 7: Visualization
# -----------------------------
plt.figure(figsize=(10,5))
plt.bar(word_freq.keys(), word_freq.values())
plt.title("Word Frequency Distribution")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
