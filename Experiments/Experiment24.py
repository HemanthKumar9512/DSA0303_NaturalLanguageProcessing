def dialog_act(sentence):
    if sentence.endswith("?"):
        return "Question"
    if sentence.lower().startswith(("yes", "okay", "sure")):
        return "Answer/Agreement"
    if sentence.lower().startswith(("please", "do")):
        return "Request"
    return "Statement"

dialog = [
    "What is your name?",
    "My name is John.",
    "Please help me."
]

for s in dialog:
    print(s, "->", dialog_act(s))
