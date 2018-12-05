import sys
import copy

def parse_info(claim):
    offsets = claim.strip().split("@")[1].split(":")[0].split(",")
    inches_from_left = int(offsets[0].strip())
    inches_from_top = int(offsets[1].strip())

    dims = claim.strip().split("@")[1].split(":")[1].split("x")
    width = int(dims[0].strip())
    height = int(dims[1].strip())

    return (inches_from_left, inches_from_top, width, height)

def part_one(square, input):
    collision_cnt = 0

    for claim in input:
        info = parse_info(claim)

        for i in range(info[1], info[1] + info[3]):
            for j in range(info[0], info[0] + info[2]):
                if square[i][j] == "#":
                    square[i][j] = "X"
                    collision_cnt += 1
                elif square[i][j] == ".":
                    square[i][j] = "#"

    print("sol p1: " + str(collision_cnt))
    return square

def part_two(filled_square, input):
    for claim in input:
        info = parse_info(claim)
        overlapping = False

        for i in range(info[1], info[1] + info[3]):
            if overlapping:
                break
            for j in range(info[0], info[0] + info[2]):
                if filled_square[i][j] == "X":
                    overlapping = True
                    break

        if not overlapping:
            print("sol p2: " + claim.split("#")[1].split("@")[0].strip())

if __name__ == '__main__':
    input = sys.stdin.readlines()
    lst = ["." for _ in range(0, 1000)]
    square = [copy.copy(lst) for _ in range(0, 1000)]

    filled_square = part_one(square, input)
    part_two(filled_square, input)
