import sys
import copy
from string import ascii_lowercase

def remove_unit(tmp_input, idx):
    del tmp_input[idx]
    del tmp_input[idx]  

if __name__ == '__main__':

    input = sys.stdin.read().strip()
    polymer_lengths = []

    for c in ascii_lowercase:

        tmp_input = input
        tmp_input = tmp_input.replace(c, "")
        tmp_input = tmp_input.replace(c.upper(), "")
        tmp_input = list(tmp_input)
        something_changed = True

        while something_changed:
            something_changed = False

            for i in range(0, len(tmp_input) - 1):
                if tmp_input[i].islower() and tmp_input[i + 1].isupper():
                    if tmp_input[i].lower() == tmp_input[i + 1].lower():
                        something_changed = True
                        remove_unit(tmp_input, i)
                        break
                elif tmp_input[i].isupper() and tmp_input[i + 1].islower():
                    if tmp_input[i].lower() == tmp_input[i + 1].lower():
                        something_changed = True
                        remove_unit(tmp_input, i)
                        break

        polymer_lengths.append(len(tmp_input))
        # print("sol p1: " + str(len(tmp_input)))

    print("sol p2: " + str(min(polymer_lengths)))
    