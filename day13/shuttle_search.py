from os.path import dirname, realpath
from typing import List


def find_connection(timestamp : int, bus_ids : List[int]) -> dict:
    connection = {
        "id": None,
        "wait": None
    }
    for id in bus_ids:
        if id == "x":
            continue
        wait = id - timestamp % id
        if wait == id:
            # if % was = 0:
            wait = 0
        if connection["wait"] == None or connection["wait"] > wait:
            connection["id"] = id
            connection["wait"] = wait

    return connection


def find_special_promotion(bus_ids : List[int]) -> int:
    # not going to lie I did not come up with this on my own.
    # There is an excellent explanation over here:
    # @see: https://youtu.be/4_5mluiXF5I?t=378
    timestamp = 0
    step = bus_ids[0]
    bus_ids[0] = "x"
    for offset, id in enumerate(bus_ids):
        if id == "x":
            continue
        while (timestamp + offset) % id != 0:
            timestamp += step
        step *= id

    return timestamp


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        timestamp, bus_ids = [row.strip() for row in input_file]
        bus_ids = [id if id == "x" else int(id) for id in bus_ids.split(",")]
        timestamp = int(timestamp)
        connection = find_connection(timestamp, bus_ids)

        print(connection["id"] * connection["wait"])

        print(find_special_promotion(bus_ids))



