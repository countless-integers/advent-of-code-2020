from os.path import dirname, realpath
from typing import List, Tuple
from re import match


def encode(mask : str, value : int) -> str:
    and_mask = int(mask.replace("X", "1"), 2)
    or_mask = int(mask.replace("X", "0"), 2)
    return (value | or_mask) & and_mask


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        memory = {}
        mask = ""
        for line in input_file:
            mask_match = match(r"^mask = (?P<mask>[01X]+)", line)
            if mask_match:
                mask = mask_match["mask"]
                continue
            value_match = match(r"^mem\[(?P<address>\d+)\] = (?P<value>\d+)", line)
            if value_match:
                memory[value_match["address"]] = encode(mask, int(value_match["value"]))
        
        print(sum(memory.values()))
