import sys
from datetime import datetime

def calc_timespan(t1, t2):
    fmt = '%H:%M'
    return datetime.strptime(t2, fmt) - datetime.strptime(t1, fmt)

def parse_info():
    date = i.split("[")[1].split("]")[0].split(" ")[0].strip()
    time = i.split("[")[1].split("]")[0].split(" ")[1].strip()
    action = i.split("[")[1].split("]")[1].strip()
    return (date, time, action)

if __name__ == '__main__':

    input = sys.stdin.readlines()
    input.sort()

    current_guard_id = ""
    start_sleeping = -1
    sleep_times = dict()
    sleeping_minutes = dict()

    for i in input:

        info = parse_info()

        if current_guard_id != "":
            if "falls" in i:
                start_sleeping = info[1]
            elif "wakes" in i:

                if not current_guard_id in sleep_times.keys():
                    sleep_times[current_guard_id] = 0
                if not current_guard_id in sleeping_minutes.keys():
                    sleeping_minutes[current_guard_id] = []

                time_to_add_in_minutes = int(str(calc_timespan(start_sleeping, info[1])).split(":")[0]) * 60
                time_to_add_in_minutes += int(str(calc_timespan(start_sleeping, info[1])).split(":")[1])
                start = int(start_sleeping.split(":")[1])
                end = int(info[1].split(":")[1]) - 1
                sleeping_minutes[current_guard_id].append(start)
                sleeping_minutes[current_guard_id].append(end)

                for idx in range(start + 1, start + time_to_add_in_minutes - 1):
                    sleeping_minutes[current_guard_id].append(idx % 60)

                current_sleep_time = sleep_times[current_guard_id] + time_to_add_in_minutes
                sleep_times[current_guard_id] = int(current_sleep_time)

        if "#" in info[2]:
            current_guard_id = info[2].split("#")[1].split("begins")[0].strip()

    lazy_guard = max(sleep_times, key = sleep_times.get)

    # min, guard
    strategy1 = [max(sleeping_minutes[lazy_guard], key = sleeping_minutes[lazy_guard].count), int(lazy_guard)]
    # min, count, guard
    strategy2 = [0, 0, 0]

    for i in sleep_times.keys():
        tmp_min = max(sleeping_minutes[i], key = sleeping_minutes[i].count)

        if sleeping_minutes[i].count(tmp_min) > strategy2[1]:
            strategy2[0] = tmp_min
            strategy2[1] = sleeping_minutes[i].count(tmp_min)
            strategy2[2] = i

    print("sol p1: " + str(strategy1[0] * strategy1[1]))
    print("sol p2: " + str(int(strategy2[2]) * strategy2[0]))
