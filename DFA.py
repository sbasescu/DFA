"""
Simon Basescu
HW 10
12/5/18
"""
def getDFA():
    DFAdict = dict()
    DFA = []
    state_names = input("State names: ")
    state_names = state_names.replace(" ", "")
    alphabet = input("Alphabet: ")
    alphabet = alphabet.replace(" ", "")
    print("Enter transition table:")
    print("   ", end='')
    for i in range(len(alphabet)):
        print(alphabet[i] + " ", end='')
    print("")
    for state in state_names:
        DFAdict[state] = 0 
        temp = dict()
        list_transitions = (input(state + ": "))
        list_transitions = list_transitions.replace(" ", "")
        if len(list_transitions) > len(alphabet):
            print("Error, too many transitions.")
            return
        for i in range(len(alphabet)):
            temp[i] = list_transitions[i]
        DFAdict[state] = temp

    start = input("Start state: ")
    final = input("Final states: ")
    DFA.append(DFAdict)
    DFA.append(start)
    DFA.append(final)
    return DFA

def simulate(D, str):
    transitions = D[0]
    current = D[1]
    final = D[2]
    for bit in str:
        current = transitions[current][int(bit)]
    for i in range(len(final)):
        if current == final[i]:
            return True
    return False

    
    
    