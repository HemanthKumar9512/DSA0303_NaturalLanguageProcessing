# 5. Implement Laplace smoothing function for bigram probabilities
def laplace_smoothed_bigram_probability(word1, word2, unigram_counts, bigram_counts, vocabulary_size):
    # Get count of the bigram (word1, word2)
    bigram_count = bigram_counts.get((word1, word2), 0)
    
    # Get count of the unigram word1
    unigram_count = unigram_counts.get(word1, 0)
    
    # Apply Laplace smoothing formula
    probability = (bigram_count + 1) / (unigram_count + vocabulary_size)
    return probability

# 6. Calculate the requested probabilities

# P(learn|Students)
prob_learn_given_students = laplace_smoothed_bigram_probability('students', 'learn', unigram_freq, bigram_freq, V)
print(f"P(learn|Students) = {prob_learn_given_students:.4f}")

# P(write|Students)
prob_write_given_students = laplace_smoothed_bigram_probability('students', 'write', unigram_freq, bigram_freq, V)
print(f"P(write|Students) = {prob_write_given_students:.4f}")

# P(code|learn)
prob_code_given_learn = laplace_smoothed_bigram_probability('learn', 'code', unigram_freq, bigram_freq, V)
print(f"P(code|learn) = {prob_code_given_learn:.4f}")

# P(Python|teach)
prob_python_given_teach = laplace_smoothed_bigram_probability('teach', 'python', unigram_freq, bigram_freq, V)
print(f"P(Python|teach) = {prob_python_given_teach:.4f}")

# P(NLP|write)
prob_nlp_given_write = laplace_smoothed_bigram_probability('write', 'nlp', unigram_freq, bigram_freq, V)
print(f"P(NLP|write) = {prob_nlp_given_write:.4f}")
