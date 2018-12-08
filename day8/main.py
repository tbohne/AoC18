import sys
import copy
import string
from string import ascii_lowercase

# 42384 too low

if __name__ == '__main__':

    input = sys.stdin.read().split()
    print(input)

    stack = []
    tree = []
    tmp_input = copy.copy(input)
    open_meta_data = 0
    idx = 0

    while len(tmp_input) > open_meta_data:

        print("len: " + str(len(tmp_input)))
        print("need: " + str(int(input[idx + 1]) + 2))
        print("open meta len: " + str(open_meta_data))

        need = int(input[idx + 1]) + 2

        if need + open_meta_data > len(tmp_input):
            print("DONE")
            break

        node = (input[idx], input[idx + 1], [])

        print("looking at: " + str(node))

        # if len(tmp_input) <= open_meta_data:
        #     print("len of rest: " + str(len(tmp_input)))
        #     print("open meta data: " + str(open_meta_data))
        #     print("current need: " + str(node[1]))
        #     print("DONE")
        #     break

        for i in range(0, len(tmp_input) - 1):
            if tmp_input[i] == node[0] and tmp_input[i + 1] == node[1]:
                tmp_idx = i

        if node[0] == '0':
            print("remove:  " + str(tmp_input[tmp_idx : (tmp_idx + 2 + int(node[1]))]))
            del tmp_input[tmp_idx : (tmp_idx + 2 + int(node[1]))]
        else:
            print("remove:::  " + str(tmp_input[tmp_idx : tmp_idx + 2]))
            del tmp_input[tmp_idx : tmp_idx + 2]

        # no childs
        if node[0] == '0':
            print("handle now")
            print(node)

            for i in range(idx + 2, idx + 2 + int(node[1])):
                node[2].append(input[i])

            tree.append(node)

        else:
            open_meta_data += int(node[1])
            print("append to stack")
            stack.append(node)
            print(node)

        idx += 2
        if node[0] == '0':
            idx += int(node[1])

    print("TODO: " + str(tmp_input))

    for i in stack:
        node = (i[0], i[1], [])

        for j in range(0, int(i[1])):   
            node[2].append(tmp_input[j])
        del tmp_input[0 : int(i[1])]
        tree.append(node)

    res = 0
    for i in tree:
        res += sum([int(x) for x in i[2]])

    print("sol p1: " + str(res))

            
