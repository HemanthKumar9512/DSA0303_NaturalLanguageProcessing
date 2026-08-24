grammar = {
    "S": ["NP VP"],
    "NP": ["John", "Mary"],
    "VP": ["runs", "walks"]
}

def parse(sentence):
    words = sentence.split()

    if words[0] in grammar["NP"] and words[1] in grammar["VP"]:
        print("Sentence accepted")
    else:
        print("Sentence rejected")

parse("John runs")
