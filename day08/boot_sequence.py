from os.path import dirname, realpath


def boot(instructions : list) -> int:
    index, accumulator = 0, 0
    executed_instructions = {}

    while True:
        instruction, value = instructions[index]
        if index in executed_instructions:
            break
        executed_instructions[index] = 1
        if instruction == "nop":
            index += 1
            continue
        if instruction == "acc":
            accumulator += int(value)
            index += 1
            continue
        if instruction == "jmp":
            index += int(value)
            continue

    return accumulator


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        print(boot([row.strip().split() for row in input_file]))