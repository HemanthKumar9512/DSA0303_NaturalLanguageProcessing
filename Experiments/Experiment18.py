import re

expression = "Likes(John, Mary)"

match = re.match(r"(\w+)\((.*)\)", expression)

if match:
    predicate = match.group(1)
    arguments = match.group(2).split(",")

    print("Predicate:", predicate)
    print("Arguments:", arguments)
