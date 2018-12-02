import sys

def part_one(input):

    exactly_two = 0
    exactly_three = 0

    for boxID in input:

        letter_count = []

        for letter in boxID:
            letter_count.append(boxID.count(letter))

        if 2 in letter_count:
            exactly_two += 1
        if 3 in letter_count:
            exactly_three += 1

    return exactly_two * exactly_three

def part_two(input):

    common_letters = ""

    for boxID_one in input:
        for boxID_two in input:

            num_of_diff_letters = 0

            if boxID_one != boxID_two:
                for i in range(0, len(boxID_one)):

                    if boxID_one[i] != boxID_two[i]:
                        num_of_diff_letters += 1
                        pos = boxID_one.find(boxID_one[i])
                        common_letters = boxID_one

            if num_of_diff_letters == 1:
                return common_letters[:pos] + common_letters[pos + 1:]

if __name__ == '__main__':

    input = sys.stdin.readlines()

    print("sol p1: " + str(part_one(input)))
    print("sol p2: " + part_two(input))
