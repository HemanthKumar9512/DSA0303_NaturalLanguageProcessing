import collections

def parse_cfg(sentence):
    tokens = sentence.lower().split()
    # Define the grammar rules
    grammar = {
        'S': [['NP', 'VP']],
        'NP': [['Det', 'N']],
        'VP': [['V', 'NP']],
        'Det': ['the', 'a'],
        'N': ['student', 'teacher', 'book'],
        'V': ['reads', 'likes']
    }

    # Use a mutable list to hold the current token index
    # This allows recursive functions to modify the same index
    current_token_index = [0]

    def parse_symbol(symbol_type):
        start_index = current_token_index[0]

        # Case for non-terminals that derive specific terminal words (Det, N, V)
        if symbol_type in ['Det', 'N', 'V']:
            if start_index < len(tokens) and tokens[start_index] in grammar[symbol_type]:
                matched_word = tokens[start_index]
                current_token_index[0] += 1
                return {'type': symbol_type, 'value': matched_word}
            else:
                return None

        # Case for non-terminals that derive other non-terminals (S, NP, VP)
        if symbol_type in grammar: # This covers 'S', 'NP', 'VP'
            for rule in grammar[symbol_type]:
                # Store the current index to backtrack if a rule fails
                prev_token_index = current_token_index[0]
                children = []
                rule_succeeded = True

                for component in rule:
                    child_tree = parse_symbol(component) # Recursive call
                    if child_tree:
                        children.append(child_tree)
                    else:
                        rule_succeeded = False
                        # Backtrack: reset the token index for the next rule attempt
                        current_token_index[0] = prev_token_index
                        break
                
                if rule_succeeded:
                    return {'type': symbol_type, 'children': children}
        return None

    parse_tree = parse_symbol('S')
    
    # Check if all tokens were consumed and parsing was successful
    if parse_tree is not None and current_token_index[0] == len(tokens):
        return parse_tree
    else:
        return "Invalid Sentence"

# Helper function to print the parse tree for better readability
def print_tree(node, level=0):
    indent = "  " * level
    if isinstance(node, str):
        return node
    elif 'value' in node:
        return f"{indent}{node['type']}: {node['value']}"
    else:
        children_str = "\n".join([print_tree(child, level + 1) for child in node['children']])
        return f"{indent}{node['type']}\n{children_str}"

# Test Cases
test_cases = [
    "the student reads a book",
    "a teacher likes the book",
    "student reads book",
    "the book likes a teacher",
    "reads the student book"
]

print("CFG Parser Test Results:")
print("-------------------------")
for i, sentence in enumerate(test_cases):
    print(f"\nTest Case {i+1}: '{sentence}'")
    result = parse_cfg(sentence)
    if result == "Invalid Sentence":
        print("Result: Invalid Sentence")
    else:
        print("Result: Valid Parse Tree")
        # To display the full tree, uncomment the next line
        # print(print_tree(result))
    print("-------------------------")
