import sys

if __name__ == '__main__':

    input = sys.stdin.readlines()
    curr_freq = 0
    reached_twice = False
    list_of_freqs = []

    while not reached_twice:

        for change in input:

            sign = change[0]
            change = int(change.replace(sign, ""))

            if (sign == "+"):
                curr_freq += change
            else:
                curr_freq -= change

            if curr_freq in list_of_freqs:
                reached_twice = True
                print("sol p2: " + str(curr_freq))
                break
            else:
                list_of_freqs.append(curr_freq)

        if len(list_of_freqs) == len(input):
            print("sol p1: " + str(curr_freq))
