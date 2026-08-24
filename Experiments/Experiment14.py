def check(subject, verb):
    if subject == "he" and verb == "runs":
        return True
    if subject == "they" and verb == "run":
        return True
    return False

print(check("he", "runs"))
print(check("they", "runs"))
