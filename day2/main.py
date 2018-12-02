import sys

def part_one(input):
    exactly_two = 0
    exactly_three = 0

    for boxID in input:
        letter_count = [boxID.count(letter) for letter in boxID]

        if 2 in letter_count:
            exactly_two += 1
        if 3 in letter_count:
            exactly_three += 1

    return exactly_two * exactly_three

def part_two(input):

    common_letters = ""

    for boxID_one in input:
        for boxID_two in input:
            if boxID_one != boxID_two:

                equal_letters = [l1 for l1, l2 in zip(boxID_one, boxID_two) if l1 == l2]

                if len(boxID_one) - len(equal_letters) == 1:
                    return "".join(equal_letters).strip()

if __name__ == '__main__':
    input = sys.stdin.readlines()
    print("sol p1: " + str(part_one(input)))
    print("sol p2: " + part_two(input))
