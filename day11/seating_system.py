from os.path import dirname, realpath
from typing import List


def run(state : List[str]) -> List[str]:
    new_state = []
    # go over seats:
    for y, row in enumerate(state):
        new_row = ""
        for x, seat in enumerate(row):
            s_occupied = 0
            if seat == ".":
                new_row += seat
                continue
            # check surrounding
            for s_y in (y - 1, y, y + 1):
                for s_x in (x - 1, x, x + 1):
                    if (
                        s_y < 0
                        or s_x < 0
                        or s_y >= len(state)
                        or s_x >= len(row)
                    ): 
                        # out-of-bounds
                        continue
                    if s_y == y and s_x == x:
                        # skip the seat we're checking in outer loop:
                        continue
                    if state[s_y][s_x] == "#":
                        s_occupied += 1
            # check for seat state change:
            if seat == "L" and s_occupied == 0:
                new_row += "#"
            elif seat == "#" and s_occupied >= 4:
                new_row += "L"
            else:
                new_row += seat
        new_state.append(new_row)
    
    if new_state == state:
        return state
    
    return run(new_state)


def count_occupied(state : List[str]) -> int:
    count = 0
    for row in state:
        for seat in row:
            if seat == "#":
                count += 1
    return count


def run_again(state : List[str]) -> List[str]:
    new_state = []
    # go over seats:
    for y, row in enumerate(state):
        new_row = ""
        for x, seat in enumerate(row):
            s_occupied = 0
            if seat == ".":
                new_row += seat
                continue

            # check surrounding
            i = 1
            line_of_sight = [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0],
            ]
            # loop until all lines of sight are blocked
            while line_of_sight != [[1,1,1],[1,1,1],[1,1,1]]:
                for d_y, s_y in enumerate((y - i, y, y + i)):
                    for d_x, s_x in enumerate((x - i, x, x + i)):
                        if line_of_sight[d_y][d_x] != 0:
                            # line of sight is blocked:
                            continue

                        if (
                            s_y < 0
                            or s_x < 0
                            or s_y >= len(state)
                            or s_x >= len(row)
                        ): 
                            # out-of-bounds
                            # block line of sight
                            line_of_sight[d_y][d_x] = 1
                            continue

                        if state[s_y][s_x] == "#":
                            s_occupied += 1
                            # block line of sight
                            line_of_sight[d_y][d_x] = 1
                        if state[s_y][s_x] == "L":
                            # block line of sight
                            line_of_sight[d_y][d_x] = 1

                i += 1

            # check for seat state change:
            if seat == "L" and s_occupied == 0:
                new_row += "#"
            elif seat == "#" and s_occupied >= 5:
                new_row += "L"
            else:
                new_row += seat
        new_state.append(new_row)
    
    if new_state == state:
        return state
    
    return run_again(new_state)

if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        initial_state = [row.strip() for row in input_file]

        print(count_occupied(run(initial_state)))
        print(count_occupied(run_again(initial_state)))