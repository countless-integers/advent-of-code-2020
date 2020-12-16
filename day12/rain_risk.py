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


def move_to_waypoint(from_position : dict, instruction : str) -> dict:
    position = {
        "x": from_position["x"],
        "y": from_position["y"],
        "waypoint": {
            "x": from_position["waypoint"]["x"],
            "y": from_position["waypoint"]["y"],
        }
    }
    action = instruction[0]
    value = int(instruction[1:])
    if action == "N":
        position["waypoint"]["y"] += value
    elif action == "S":
        position["waypoint"]["y"] -= value
    elif action == "E":
        position["waypoint"]["x"] += value
    elif action == "W":
        position["waypoint"]["x"] -= value
    elif action == "F":
        position["y"] += position["waypoint"]["y"] * value
        position["x"] += position["waypoint"]["x"] * value
    elif action == "L" and value % 360 == 90 or action == "R" and value % 360 == 270:
        position["waypoint"]["y"] = from_position["waypoint"]["x"]
        position["waypoint"]["x"] = -from_position["waypoint"]["y"]
    elif action == "L" and value % 360 == 270 or action == "R" and value % 360 == 90:
        position["waypoint"]["y"] = -from_position["waypoint"]["x"]
        position["waypoint"]["x"] = from_position["waypoint"]["y"]
    elif action == "L" and value % 360 == 180 or action == "R" and value % 360 == 180:
        position["waypoint"]["y"] = -from_position["waypoint"]["y"]
        position["waypoint"]["x"] = -from_position["waypoint"]["x"]

    return position


def calculate_distance_with_waypoint(instructions : List[str]) -> int:
    current_position = {
        "x": 0,
        "y": 0,
        "waypoint": {
            "x": 10,
            "y": 1
        }
    }
    for instruction in instructions:
        current_position = move_to_waypoint(current_position, instruction)

    return abs(current_position["x"]) + abs(current_position["y"])

if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        instructions = [row.strip() for row in input_file]
        print(calculate_distance(instructions))
        print(calculate_distance_with_waypoint(instructions))