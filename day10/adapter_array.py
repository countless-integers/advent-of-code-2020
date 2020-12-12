from os.path import dirname, realpath


def sort_adapters(adapters : list) -> list:
    pass


def get_differences(adapters : list) -> dict:
    adapters = sorted(adapters)
    differences = {
        1: 0,
        2: 0,
        3: 1, # because last adapter is alway +3
    }
    for i, adapter in enumerate(adapters):
        if i == 0:
            last = 0
        else:
            last = adapters[i - 1]
        
        differences[adapter - last] += 1

    return differences


def count_arrangements(adapters : list) -> dict:
    pass


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        adapters = [int(row.strip()) for row in input_file]
        differences = get_differences(adapters)
        print(differences[1] * differences[3])
