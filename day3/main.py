import sys

def part_one(square, i, j):
    if square[i][j] == "#":
        square[i][j] = "X"
        return 1
    elif square[i][j] == ".":
        square[i][j] = "#"
    return 0

def claim_iteration(input, square_filled):

    collision_cnt = 0

    for claim in input:
        offsets = claim.strip().split("@")[1].split(":")[0].split(",")
        inches_from_left = int(offsets[0].strip())
        inches_from_top = int(offsets[1].strip())

        dims = claim.strip().split("@")[1].split(":")[1].split("x")
        width = int(dims[0].strip())
        height = int(dims[1].strip())

        overlapping = False
        for i in range(inches_from_top, inches_from_top + height):
            for j in range(inches_from_left, inches_from_left + width):
                if not square_filled:
                    collision_cnt += part_one(square, i, j)
                else:
                    if square[i][j] == "X":
                        overlapping = True
                        break

        if not overlapping and square_filled:
            print("sol p2: " + claim.strip())

    return collision_cnt

if __name__ == '__main__':

    input = sys.stdin.readlines()

    square = []
    for i in range (0, 1000):
        tmp = []
        for j in range (0, 1000):
            tmp.append(".")
        square.append(tmp)

    print("sol p1: " + str(claim_iteration(input, False)))
    claim_iteration(input, True)
