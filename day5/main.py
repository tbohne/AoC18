import sys
import copy
from string import ascii_lowercase

def remove_unit(tmp_input, idx):
    del tmp_input[idx]
    del tmp_input[idx]

def react_polymer(tmp_input):

    modified = True

    while modified:
        modified = False

        for i in range(0, len(tmp_input) - 1):
            if tmp_input[i] != tmp_input[i + 1] and tmp_input[i].lower() == tmp_input[i + 1].lower():
                modified = True
                remove_unit(tmp_input, i)
                break
    return tmp_input

if __name__ == '__main__':
    input = sys.stdin.read().strip()
    polymer_lengths = []

    print("sol p1: " + str(len(react_polymer(list(input)))))

    for unit_type in ascii_lowercase:

        tmp_input = list(input.replace(unit_type, "").replace(unit_type.upper(), ""))
        tmp_input = react_polymer(tmp_input)
        polymer_lengths.append(len(tmp_input))

    print("sol p2: " + str(min(polymer_lengths)))
