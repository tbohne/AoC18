import sys
import copy
from string import ascii_lowercase

def step_time(letter, sample):
    if not sample:
        return 60 + ord(letter) - 64
    else:
        return ord(letter) - 64

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

def get_waiting_lists(names):
    waiting_lists = []
    for i in names.keys():
        waiting_lists.append((names[i], i))
    return waiting_lists

def get_admissible_item(waiting_lists):

    tmp = copy.copy(waiting_lists)
    valid = False

    while not valid:
        valid = True
        if len(tmp) == 0:
            return None
        tmp_best = min(tmp)

        if len(tmp_best[0]) == 0:
            for w in workers:
                if w[2] == tmp_best[1]:
                    valid = False
        else:
            valid = False

        if not valid:
            tmp.remove(tmp_best)

    return tmp_best[1]

if __name__ == '__main__':

    input = sys.stdin.readlines()
    num_of_workers = 5
    sample = False
    names = get_names()
    workers = []

    for i in range(0, num_of_workers):
        # (idx, available, working item, time_left)
        workers.append((i, True, "", 0))

    for i in input:
        before = i.strip().split("must")[0].split("Step")[1].strip()
        after = i.strip().split("can")[0].split("step")[1].strip()
        names[after].append(before)

    time = 0

    while len(names.keys()) > 0:

        for w in workers:
            # worker available
            if w[1]:
                waiting_lists = get_waiting_lists(names)
                item = get_admissible_item(waiting_lists)
                if item == None:
                    pass
                    # print("no item available for worker" + str(w[0]))
                else:
                    workers[workers.index(w)] = (w[0], False, item, step_time(item, sample))
                    # print("time " + str(time) + " worker" + str(w[0]) + " starts to work on item " + str(item) + " needs time: " + str(step_time(item, sample)))
            # worker busy
            else:
                time_left = w[3] - 1
                if time_left != 0:
                    workers[workers.index(w)] = (w[0], False, w[2], time_left)
                else:
                    delete_item(str(w[2]))
                    # print("time " + str(time) + " worker" + str(w[0]) + " finished working on item " + str(w[2]))

                    waiting_lists = get_waiting_lists(names)
                    item = get_admissible_item(waiting_lists)

                    if item == None:
                        workers[workers.index(w)] = (w[0], True, "", 0)
                        # print("no item available for worker" + str(w[0]))
                    else:
                        workers[workers.index(w)] = (w[0], False, item, step_time(item, sample))
                        # print("time " + str(time) + " worker" + str(w[0]) + " starts to work on item " + str(item) + " needs time: " + str(step_time(item, sample)))

                    continue

        time += 1

    print("sol p2: " + str(time - 1))
