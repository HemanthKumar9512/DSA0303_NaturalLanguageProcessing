def check_agreement(subject, verb):
    # Define feature structures for subjects
    subject_features = {
        'he': {'number': 'singular', 'person': 'third'},
        'she': {'number': 'singular', 'person': 'third'},
        'it': {'number': 'singular', 'person': 'third'},
        'they': {'number': 'plural', 'person': 'third'}
    }

    # Define feature structures for verbs
    verb_features = {
        'runs': {'number': 'singular'},
        'writes': {'number': 'singular'},
        'run': {'number': 'plural'},
        'write': {'number': 'plural'}
    }

    # Convert inputs to lowercase for case-insensitivity
    subject_lower = subject.lower()
    verb_lower = verb.lower()

    # Check if subject and verb are recognized
    if subject_lower not in subject_features or verb_lower not in verb_features:
        print(f"Error: Unrecognized subject '{subject}' or verb '{verb}'.")
        return False

    # Get features for the given subject and verb
    sub_feat = subject_features[subject_lower]
    verb_feat = verb_features[verb_lower]

    # Check for agreement: number must match
    if sub_feat['number'] == verb_feat['number']:
        return True
    else:
        return False

# Test Cases
test_cases = [
    ('he', 'runs', True),
    ('he', 'run', False),
    ('they', 'run', True),
    ('they', 'writes', False),
    ('she', 'writes', True)
]

print("\nSubject-Verb Agreement Checker Test Results:")
print("------------------------------------------")
for i, (subject, verb, expected) in enumerate(test_cases):
    result = check_agreement(subject, verb)
    status = "PASS" if result == expected else "FAIL"
    print(f"Test Case {i+1}: Subject='{subject}', Verb='{verb}', Expected={expected}, Got={result} [{status}]")
print("------------------------------------------")
