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


def count_paths(adapters : list) -> dict:
    # starting point is always 1, ending doesn't matter
    # because it can only be reached in one way from 
    # the last adapter:
    paths = {0: 1}
    adapters = sorted(adapters)
    for adapter in adapters:
        # initialise 3 keys to avoid errors:
        for i in range(1, 4):
            if adapter - i not in paths:
                paths[adapter - i] = 0
        # add all possible paths leading to the adapter:
        paths[adapter] = paths[adapter - 1] + paths[adapter - 2] + paths[adapter - 3]
    
    # adapter will be the last value from iterator:
    return paths[adapter]



if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        adapters = [int(row.strip()) for row in input_file]
        differences = get_differences(adapters)
        print(differences[1] * differences[3])
        print(count_paths(adapters))
