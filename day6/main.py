import sys
import copy
from string import ascii_lowercase

def manhattan_dist(c1, c2):
    return abs(c1[1] - c2[1]) + abs(c1[0] - c2[0])

def part_two():

    total = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            sum = 0
            for c in coord_by_name.keys():
                sum += manhattan_dist((j, i), coord_by_name[c])
            if sum < 10000:
                total += 1

    print("sol p2: " + str(total))

def part_one():

    for i in range(0, 1000):
        for j in range(0, 1000):

            if square[i][j] == ".":
                min_dist = 99999
                name = ""
                collision_dist = min_dist
                for coords in list_of_coords:
                    distance = abs(i - coords[1]) + abs(j - coords[0])
                    if distance < min_dist:
                        min_dist = distance
                        name = coordinate_names[coords].lower()
                    elif distance == min_dist:
                        collision_dist = min_dist

                if collision_dist == min_dist:
                    square[i][j] = "."
                else:
                    square[i][j] = name

    area_cnt = dict()

    y_min = 2000
    x_min = 2000
    x_max = 0
    y_max = 0
    x_min_remove = []
    x_max_remove = []
    y_min_remove = []
    y_max_remove = []

    for c in list_of_coords:
        if c[0] <= x_min:
            x_min = c[0]
            x_min_remove.append(coordinate_names[c])
            for i in x_min_remove:
                if coord_by_name[i][0] > x_min:
                    x_min_remove.remove(i)
        if c[0] >= x_max:
            x_max = c[0]
            x_max_remove.append(coordinate_names[c])
            for i in x_max_remove:
                if coord_by_name[i][0] < x_max:
                    x_max_remove.remove(i)
        if c[1] <= y_min:
            y_min = c[1]
            y_min_remove.append(coordinate_names[c])
            for i in y_min_remove:
                if coord_by_name[i][1] > y_min:
                    y_min_remove.remove(i)
        if c[1] >= y_max:
            y_max = c[1]
            y_max_remove.append(coordinate_names[c])
            for i in y_max_remove:
                if coord_by_name[i][1] < y_max:
                    y_max_remove.remove(i)

    for i in coordinate_names.values():

        dist = abs(coord_by_name[i][1] - x_max)
        man_dists = []
        for j in coordinate_names.values():
            if coord_by_name[j][1] == x_max:
                man_dist = manhattan_dist((coord_by_name[i][0], x_max), coord_by_name[j])
                man_dists.append(man_dist)
        if min(man_dists) > dist:
            x_max_remove.append(i)

        dist = abs(coord_by_name[i][1] - x_min)
        man_dists = []
        for j in coordinate_names.values():
            if coord_by_name[j][1] == x_min:
                man_dist = manhattan_dist((coord_by_name[i][0], x_min), coord_by_name[j])
                man_dists.append(man_dist)
        if min(man_dists) > dist:
            x_min_remove.append(i)

        dist = abs(coord_by_name[i][0] - y_max)
        man_dists = []
        for j in coordinate_names.values():
            if coord_by_name[j][0] == y_max:
                man_dist = manhattan_dist((y_max, coord_by_name[i][1]), coord_by_name[j])
                man_dists.append(man_dist)
        if min(man_dists) > dist:
            y_max_remove.append(i)

        dist = abs(coord_by_name[i][0] - y_min)
        man_dists = []
        for j in coordinate_names.values():
            if coord_by_name[j][0] == y_min:
                man_dist = manhattan_dist((y_min, coord_by_name[i][1]), coord_by_name[j])
                man_dists.append(man_dist)
        if min(man_dists) > dist:
            y_min_remove.append(i)

        area_cnt[i] = 0

    for i in range(0, 1000):
        for j in range(0, 1000):

            if square[i][j].islower():
                if square[i][j].upper() not in x_max_remove and square[i][j].upper() not in x_min_remove and square[i][j].upper() not in y_max_remove and square[i][j].upper() not in y_min_remove:
                    area_cnt[square[i][j].upper()] += 1

    max = 0
    caused_by = ""
    for i in area_cnt.keys():
        cnt = 0
        if i != 0:
            cnt = area_cnt[i] + 1

        if cnt > max:
            max = cnt
            caused_by = i

    print(caused_by + ": " + str(max))

if __name__ == '__main__':

    input = sys.stdin.readlines()

    test = dict()
    tmp_cnt = 0

    for c in ascii_lowercase:
        test[tmp_cnt] = c.upper()
        tmp_cnt += 1

    rest = len(input) - 26

    for c in ascii_lowercase:
        if rest > 0:
            rest -= 1
            test[tmp_cnt] = c.upper() + c.upper()
            tmp_cnt += 1

    cnt = 0
    lst = ["." for _ in range(0, 1000)]
    square = [copy.copy(lst) for _ in range(0, 1000)]

    list_of_coords = []
    coordinate_names = dict()
    coord_by_name = dict()

    for i in input:
        coords = (int(i.strip().split(",")[0]), int(i.strip().split(",")[1].strip()))
        list_of_coords.append(coords)
        square[coords[1]][coords[0]] = test[cnt]
        coordinate_names[coords] = test[cnt]
        coord_by_name[test[cnt]] = (coords[1], coords[0])
        cnt += 1

    part_one()
    part_two()
