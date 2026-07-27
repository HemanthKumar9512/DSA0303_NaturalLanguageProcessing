from nltk import CFG
from nltk.parse.chart import ChartParser

# 1. Define a Context-Free Grammar (CFG)
# This is a very simple grammar for demonstration purposes.
# S -> Sentence (start symbol)
# NP -> Noun Phrase
# VP -> Verb Phrase
# Det -> Determiner
# N -> Noun
# V -> Verb
# P -> Preposition
# C -> Conjunction

grammar_str = """
S -> NP VP
NP -> Det N | N | NP PP
VP -> V NP | VP PP
PP -> P NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'park' | 'telescope'
V -> 'saw' | 'ate' | 'walked'
P -> 'in' | 'with'
"""
grammar = CFG.fromstring(grammar_str)

print("--- Defined Grammar ---")
print(grammar)

# 2. Define a sample sentence and tokenize it
sentence = "the cat saw a dog in the park"
sentence_tokens = sentence.split()

print("\n--- Sentence Tokens ---")
print(sentence_tokens)

# 3. Create a parser and parse the sentence
# ChartParser is a common type of parser for CFGs.
parser = ChartParser(grammar)

print("\n--- Generated Parse Trees ---")
# Iterate through all possible parse trees for the sentence
for tree in parser.parse(sentence_tokens):
    print(tree)
    # You can also visualize the tree, if running in an environment that supports it
    # tree.pretty_print()

# Example of an ambiguous sentence (if the grammar allows)
ambiguous_sentence = "the cat saw a dog with a telescope"
ambiguous_sentence_tokens = ambiguous_sentence.split()

print("\n--- Parse Trees for an Ambiguous Sentence ---")
for tree in parser.parse(ambiguous_sentence_tokens):
    print(tree)
