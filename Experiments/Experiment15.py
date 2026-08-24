import nltk

grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'John' [0.5] | 'Mary' [0.5]
VP -> 'runs' [0.5] | 'walks' [0.5]
""")

parser = nltk.ViterbiParser(grammar)

for tree in parser.parse("John runs".split()):
    print(tree)
