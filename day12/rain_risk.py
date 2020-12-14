from os.path import dirname, realpath
from typing import List, Tuple


def move(from_position : dict, instruction : str) -> dict:
    position = {
        "x": from_position["x"], 
        "y": from_position["y"], 
        "dir": from_position["dir"]
    }
    action = instruction[0]
    value = int(instruction[1:])
    if action == "N":
        position["y"] += value
    elif action == "S":
        position["y"] -= value
    elif action == "E":
        position["x"] += value
    elif action == "W":
        position["x"] -= value
    elif action == "R":
        rose = "NESW"
        rose = "_" + rose[rose.index(position["dir"]) + 1:] + rose[:rose.index(position["dir"]) + 1]
        position["dir"] = rose[int(value % 360 / 90)]
    elif action == "L":
        rose = "NWSE"
        rose = "_" + rose[rose.index(position["dir"]) + 1:] + rose[:rose.index(position["dir"]) + 1]
        position["dir"] = rose[int(value % 360 / 90)]
    elif action == "F" and position["dir"] == "N":
        position["y"] += value
    elif action == "F" and position["dir"] == "S":
        position["y"] -= value
    elif action == "F" and position["dir"] == "W":
        position["x"] -= value
    elif action == "F" and position["dir"] == "E":
        position["x"] += value
    return position


def calculate_distance(instructions : List[str]) -> int:
    current_position = {"x": 0, "y": 0, "dir": "E"}
    for instruction in instructions:
        current_position = move(current_position, instruction)

    return abs(current_position["x"]) + abs(current_position["y"])


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        instructions = [row.strip() for row in input_file]
        print(calculate_distance(instructions))