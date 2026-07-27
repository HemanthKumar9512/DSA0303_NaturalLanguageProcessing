import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from collections import Counter

# Download tokenizer (only first time, ensure it's downloaded if not already)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True) # Added to resolve LookupError

# 1. Read a small text corpus
text_corpus = (
    "Natural Language Processing is interesting. "
    "Machine Learning is powerful. "
    "Artificial Intelligence is transforming the world. "
    "Natural Language Processing improves Artificial Intelligence."
)

print("--- Text Corpus ---")
print(text_corpus)

# 2. Tokenize the text into words and preprocess
tokens = word_tokenize(text_corpus.lower())
# Remove punctuation and non-alphabetic tokens
tokens = [word for word in tokens if word.isalpha()]

print("\n--- Tokenized Words ---")
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

# 4. Compute unigram probabilities
total_words = len(tokens)
unigram_probabilities = {word: freq / total_words for word, freq in unigram_freq.items()}

print("\n--- Unigram Probabilities ---")
for word, prob in unigram_probabilities.items():
    print(f"P({word}) = {prob:.4f}")

# 5. Compute bigram probabilities using MLE
bigram_probabilities = {}
for bg, freq in bigram_freq.items():
    first_word = bg[0]
    # Avoid division by zero for unigrams that might not be in the corpus (though they should be here)
    if unigram_freq[first_word] > 0:
        probability = freq / unigram_freq[first_word]
        bigram_probabilities[bg] = probability
    else:
        bigram_probabilities[bg] = 0.0 # Should not happen with current logic

print("\n--- Bigram Probabilities (MLE) ---")
for bg, prob in bigram_probabilities.items():
    print(f"P({bg[1]} | {bg[0]}) = {prob:.4f}")

# 6. Check whether a given bigram exists and 7. Report zero probability for unseen bigrams.
def check_bigram_existence_and_probability(bigram_tuple, bigram_probabilities_dict):
    if bigram_tuple in bigram_probabilities_dict:
        prob = bigram_probabilities_dict[bigram_tuple]
        print(f"\nBigram '{bigram_tuple[0]} {bigram_tuple[1]}' exists with probability: {prob:.4f}")
    else:
        print(f"\nBigram '{bigram_tuple[0]} {bigram_tuple[1]}' is unseen. Probability: 0.0000")

# Test cases
check_bigram_existence_and_probability(('natural', 'language'), bigram_probabilities)
check_bigram_existence_and_probability(('language', 'processing'), bigram_probabilities)
check_bigram_existence_and_probability(('is', 'powerful'), bigram_probabilities)
check_bigram_existence_and_probability(('python', 'programming'), bigram_probabilities) # Unseen bigram
