import sys
from datetime import datetime

def calc_timespan(t1, t2):
    FMT = '%H:%M'
    return datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)

if __name__ == '__main__':

    input = sys.stdin.readlines()
    input.sort()

    current_guard_id = ""
    start_sleeping = -1
    sleep_times = dict()
    sleeping_minutes = dict()

    for i in input:
        date = i.split("[")[1].split("]")[0].split(" ")[0].strip()
        time = i.split("[")[1].split("]")[0].split(" ")[1].strip()
        action = i.split("[")[1].split("]")[1].strip()

        if current_guard_id != "":
            if "falls" in i:
                start_sleeping = time
            elif "wakes" in i:
                if not current_guard_id in sleep_times.keys():
                    sleep_times[current_guard_id] = 0
                if not current_guard_id in sleeping_minutes.keys():
                    sleeping_minutes[current_guard_id] = []

                time_to_add_in_minutes = int(str(calc_timespan(start_sleeping, time)).split(":")[0]) * 60
                time_to_add_in_minutes += int(str(calc_timespan(start_sleeping, time)).split(":")[1])

                start = int(start_sleeping.split(":")[1])
                end = int(time.split(":")[1]) - 1

                sleeping_minutes[current_guard_id].append(start)
                sleeping_minutes[current_guard_id].append(end)

                for idx in range(start + 1, start + time_to_add_in_minutes - 1):
                    sleeping_minutes[current_guard_id].append(idx % 60)

                current_sleep_time = sleep_times[current_guard_id] + time_to_add_in_minutes
                sleep_times[current_guard_id] = int(current_sleep_time)

        if "#" in action:
            current_guard_id = action.split("#")[1].split("begins")[0].strip()

    lazy_guard_s1 = max(sleep_times, key = sleep_times.get)

    lazy_min = 0
    lazy_min_cnt = 0
    lazy_guard_s2 = 0

    list_of_lazy_mins = []

    for i in sleep_times.keys():
        tmp_min = max(sleeping_minutes[i], key = sleeping_minutes[i].count)
        cnt = sleeping_minutes[i].count(tmp_min)
        if cnt > lazy_min_cnt:
            lazy_min = tmp_min
            lazy_min_cnt = cnt
            lazy_guard_s2 = i

    print("sol p1: " + str(int(lazy_guard_s1) * max(sleeping_minutes[lazy_guard_s1], key = sleeping_minutes[lazy_guard_s1].count)))
    print("sol p2: " + str(int(lazy_guard_s2) * lazy_min))
