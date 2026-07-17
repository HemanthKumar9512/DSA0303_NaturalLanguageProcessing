transition = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}

start_state = 'q0'
final_states = ['q2']

string = input("Enter String: ")

current = start_state
path = [current]

for ch in string:
    if ch not in ['a', 'b']:
        print("Invalid Symbol")
        exit()

    current = transition[current][ch]
    path.append(current)

print("Transition Path:")
print(" -> ".join(path))

if current in final_states:
    print("Accepted")
else:
    print("Rejected")