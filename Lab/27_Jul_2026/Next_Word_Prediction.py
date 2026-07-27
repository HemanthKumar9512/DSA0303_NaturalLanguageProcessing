import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from collections import Counter

# Download tokenizer (only first time, ensure it's downloaded if not already)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True) # Added to resolve LookupError

# Re-define text_corpus and calculate bigram_probabilities for self-containment
text_corpus = (
    "<s> Natural Language Processing is interesting. </s>"
    "<s> Machine Learning is powerful. </s>"
    "<s> Artificial Intelligence is transforming the world. </s>"
    "<s> Natural Language Processing improves Artificial Intelligence. </s>"
)

# Tokenize the text into words and preprocess
tokens = word_tokenize(text_corpus.lower())
# Remove punctuation and non-alphabetic tokens
tokens = [word for word in tokens if word.isalpha()]

# Generate unigram and bigram frequency counts
unigram_freq = Counter(tokens)
bigram_list = list(bigrams(tokens))
bigram_freq = Counter(bigram_list)

# Compute bigram probabilities using MLE
bigram_probabilities = {}
for bg, freq in bigram_freq.items():
    first_word = bg[0]
    if unigram_freq[first_word] > 0:
        probability = freq / unigram_freq[first_word]
        bigram_probabilities[bg] = probability
    else:
        bigram_probabilities[bg] = 0.0

def predict_next_word(current_word, bigram_probs):
    best_next_word = None
    max_prob = -1

    print(f"\nPredicting next word for '{current_word}':")

    # Filter bigrams that start with the current word
    possible_next_words = {bg[1]: prob for bg, prob in bigram_probs.items() if bg[0] == current_word}

    if not possible_next_words:
        return "(No prediction: bigram not found)"

    for next_word, prob in possible_next_words.items():
        print(f"  P({next_word} | {current_word}) = {prob:.4f}")
        if prob > max_prob:
            max_prob = prob
            best_next_word = next_word

    return best_next_word

# Test the prediction function with some words from the corpus
print(f"Next word after 'natural': {predict_next_word('natural', bigram_probabilities)}")
print(f"Next word after 'is': {predict_next_word('is', bigram_probabilities)}")
print(f"Next word after 'world': {predict_next_word('world', bigram_probabilities)}")
print(f"Next word after 'python': {predict_next_word('python', bigram_probabilities)}") # Test for an unseen word
