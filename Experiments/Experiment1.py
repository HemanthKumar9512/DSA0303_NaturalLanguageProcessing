import re

text = "My phone number is 9876543210"

print(re.search(r"\d+", text).group())
print(re.findall(r"\d+", text))
