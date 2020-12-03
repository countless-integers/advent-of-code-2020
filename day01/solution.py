import os 


def solve_first(data : list, target_value : int) -> int:
    data.sort(reverse=True)
    for index, number in enumerate(data):
        if number > target_value:
            continue

        for number_2 in data[:index:-1]:
            total = number + number_2
            if (total > target_value):
                break
            if (total == target_value):
                return number * number_2


def solve_second(data : list, target_value : int) -> int:
    data.sort(reverse=True)
    for index, number in enumerate(data):
        if number > target_value:
            continue

        for index_2, number_2 in enumerate(data[:index:-1]):
            if (number + number_2 > target_value):
                break

            for number_3 in data[:index:-1][1:]:
                total = number + number_2 + number_3
                if (total > target_value):
                    break
                if (total == target_value):
                    return number * number_2 * number_3


if __name__ == "__main__":
    data = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        data = [int(row) for row in input_file]

    print(solve_first(data, 2020))
    print(solve_second(data, 2020))