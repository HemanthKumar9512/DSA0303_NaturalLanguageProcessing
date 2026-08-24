def fsa(s):
    return s.endswith("ab")

for s in ["ab", "aab", "abab", "abc"]:
    print(s, fsa(s))
