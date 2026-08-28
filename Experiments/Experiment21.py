import nltk

sentence = "The smart boy plays football"

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det Adj N
VP -> V NP
NP -> Det N
Det -> 'The'
Adj -> 'smart'
N -> 'boy' | 'football'
V -> 'plays'
""")

parser = nltk.ChartParser(grammar)

for tree in parser.parse(sentence.split()):
    print(tree)
