def sentence_probability(sentence):
    # Define the PCFG rules and their probabilities
    pcfg_rules = {
        'S': {'NP VP': 1.0},
        'NP': {
            'John': 0.6,
            'Mary': 0.4
        },
        'VP': {
            'runs': 0.5,
            'walks': 0.5
        }
    }

    words = sentence.split()

    # A valid sentence for this grammar must have exactly two words
    if len(words) != 2:
        return 0.0

    np_word = words[0]
    vp_word = words[1]

    # Get NP probability
    p_np = pcfg_rules['NP'].get(np_word, 0.0)

    # Get VP probability
    p_vp = pcfg_rules['VP'].get(vp_word, 0.0)

    # If either NP or VP word is not in the grammar, the sentence cannot be generated
    if p_np == 0.0 or p_vp == 0.0:
        return 0.0

    # Calculate sentence probability: P(S->NP VP) * P(NP) * P(VP)
    # P(S->NP VP) is always 1.0 in this specific grammar
    p_s_np_vp = pcfg_rules['S'].get('NP VP', 0.0)

    if p_s_np_vp == 0.0:
        return 0.0 # Should not happen with the given grammar

    return p_s_np_vp * p_np * p_vp

# Test Cases
test_cases = [
    ("John runs", 0.30),
    ("John walks", 0.30),
    ("Mary runs", 0.20),
    ("Mary walks", 0.20),
    ("Peter runs", 0.00)
]

print("\nPCFG Sentence Probability Test Results:")
print("---------------------------------------")
for i, (sentence, expected_prob) in enumerate(test_cases):
    calculated_prob = sentence_probability(sentence)
    # Use a small tolerance for floating-point comparison
    status = "PASS" if abs(calculated_prob - expected_prob) < 1e-9 else "FAIL"
    print(f"Test Case {i+1}: Sentence='{sentence}', Expected={expected_prob:.2f}, Got={calculated_prob:.2f} [{status}]")
print("---------------------------------------")
