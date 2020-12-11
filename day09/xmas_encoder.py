from os.path import dirname, realpath


def find_elements(numbers : list, target_sum : int) -> tuple:
    for i, a in enumerate(numbers):
        for b in numbers[i + 1:]:
            if a + b == target_sum:
                return a, b
    return None


def find_error(numbers : list, preamble_len=25) -> int:
    i = preamble_len
    while i < len(numbers):
        elements = find_elements(numbers[i - preamble_len:i], numbers[i])
        if elements:
            i += 1
            continue
        return numbers[i]
    
    raise Exception("Found no error")


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        numbers = [int(row.strip()) for row in input_file]
        print(find_error(numbers))