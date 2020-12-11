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


def find_error_elements(numbers : list, error : int) -> list:
    for i, a in enumerate(numbers):
        rolling_sum = a
        for b in numbers[i + 1:]:
            rolling_sum += b
            if rolling_sum > error:
                break
            if rolling_sum == error:
                return numbers[i:numbers.index(b) + 1]
    
    raise Exception("Oh no, oh no, oh no no no no no, rembember...")


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        numbers = [int(row.strip()) for row in input_file]
        error = find_error(numbers)
        print(error)
        error_elements = find_error_elements(numbers[:numbers.index(error)], error)
        print(min(error_elements) + max(error_elements))