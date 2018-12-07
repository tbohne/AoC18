import sys
import copy
import string
from string import ascii_lowercase

def get_names():
    names = dict()
    cnt = 0
    for i in ascii_lowercase:
        if cnt == len(input) - 1:
            break
        names[i.upper()] = []
        cnt += 1
    return names

def delete_item(item):
    for i in names.keys():
        if i == item:
            del names[i]
            break

    for i in names.keys():
        if item in names[i]:
            names[i].remove(item)

def parse_input():
    for i in input:
        before = i.strip().split("must")[0].split("Step")[1].strip()
        after = i.strip().split("can")[0].split("step")[1].strip()
        names[after].append(before)

if __name__ == '__main__':

    input = sys.stdin.readlines()
    names = get_names()
    parse_input()
    order = []

    while len(names) > 0:

        deps = []
        for i in names.keys():
            deps.append(names[i])
        min_list = min(deps)

        for j in names.keys():
            if names[j] == min_list:
                order.append(j)
                delete_item(j)
                break

    print("sol p1: " + "".join(order))
