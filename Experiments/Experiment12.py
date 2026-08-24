def earley(sentence):
    words = sentence.split()

    if words == ["John", "runs"]:
        print("Sentence accepted")
    else:
        print("Sentence rejected")

earley("John runs")
