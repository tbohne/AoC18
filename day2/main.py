import sys

def part_one(input):

    exactly_two = 0
    exactly_three = 0

    for boxID in input:

        locked_two = False
        locked_three = False

        for letter in boxID:

            if boxID.count(letter) == 2 and not locked_two:
                exactly_two += 1
                locked_two = True

            if boxID.count(letter) == 3 and not locked_three:
                exactly_three += 1
                locked_three = True

    checksum = exactly_two * exactly_three
    return checksum

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
