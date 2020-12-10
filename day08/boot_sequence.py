from os.path import dirname, realpath
from copy import deepcopy 


def boot(instructions : list, use_exceptions = False) -> int:
    index, accumulator = 0, 0
    executed_instructions = {}
    instructions_length = len(instructions)

    while True:
        if index + 1 >  instructions_length:
            break 

        instruction, value = instructions[index]
        if index in executed_instructions:
            if use_exceptions:
                raise RecursionError("Infinite loop detected")
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


def uno_boot(instructions : list) -> int:
    for index, instruction in enumerate(instructions):
        if instruction[0] == "jmp" or instruction[0] == "nop":
            # note to self:
            # because it's a list of lists shallow copy won't work, so we
            # need to go deep...
            new_instructions = deepcopy(instructions)
            new_instructions[index][0] = "jmpnop".replace(instruction[0], "")
            try:
                return boot(new_instructions, use_exceptions=True)
            except RecursionError:
                continue
    raise Exception("the ultimate failure")


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        instructions = [row.strip().split() for row in input_file]
        print(boot(instructions))
        print(uno_boot(instructions))