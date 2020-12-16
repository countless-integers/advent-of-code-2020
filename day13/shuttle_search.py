from os.path import dirname, realpath


def find_connection(timestamp : int, bus_ids : list) -> dict:
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


def find_special_promotion(bus_ids : list) -> int:
    # for start in bus_ids:
    #     if start != "x":
    #         break
    start = bus_ids[0]

    n = 1
    while True:
        prev = start * n
        for i, id in enumerate(bus_ids[1:]):
            if id == "x":
                continue
            if i + 1 == len(bus_ids):
                break
            if id * n == prev + i + 1:
                prev = id
            else:
                break
        n += 1
        print(n * start)

    return n * start


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        timestamp, bus_ids = [row.strip() for row in input_file]
        bus_ids = [id if id == "x" else int(id) for id in bus_ids.split(",")]
        # timestamp = int(timestamp)
        # connection = find_connection(timestamp, bus_ids)
        # print(connection["id"] * connection["wait"])
        print(find_special_promotion(bus_ids))



