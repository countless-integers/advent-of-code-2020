import os


def count_trees(map_of_the_land, slope : tuple) -> int:
    tree_count = 0
    position = 0 
    length = None
    for row in map_of_the_land[::slope[1]]:
        if length == None:
            length = len(row)
            continue
        position += slope[0]
        if position >= length:
            position = position - length
        if row[position] == "#":
            tree_count += 1

    return tree_count


if __name__ == "__main__":
    data = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        data = [row.strip() for row in input_file]
        
    print(count_trees(data, (3, 1)))

    print(
        count_trees(data, (1, 1)) 
        * count_trees(data, (3, 1)) 
        * count_trees(data, (5, 1)) 
        * count_trees(data, (7, 1)) 
        * count_trees(data, (1, 2)) 
    )


