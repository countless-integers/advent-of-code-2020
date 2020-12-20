from os.path import dirname, realpath
from typing import List, Tuple
from re import match


def encode(mask : str, value : int) -> str:
    and_mask = int(mask.replace("X", "1"), 2)
    or_mask = int(mask.replace("X", "0"), 2)
    return (value | or_mask) & and_mask


def encode_address(mask : str, address : int) -> List[int]:
    address_bin = list("{0:b}".format(address).zfill(36))

    for i, c in enumerate(mask):
        if c == "1":
            address_bin[i] = "1"
        elif c == "X":
            address_bin[i] = "X"

    def combine(address_pool : List[str]) -> List[str]:
        new_address_pool = []
        for n in address_pool:
            if "X" not in n:
                return address_pool
            new_address_pool.append(n.replace("X", "1", 1))
            new_address_pool.append(n.replace("X", "0", 1))
        return combine(new_address_pool)

    return [int(addr, 2) for addr in combine(["".join(address_bin)])]


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        memory = {}
        recollections = {}
        mask = ""
        for line in input_file:
            mask_match = match(r"^mask = (?P<mask>[01X]+)", line)
            if mask_match:
                mask = mask_match["mask"]
                continue
            value_match = match(r"^mem\[(?P<address>\d+)\] = (?P<value>\d+)", line)
            if value_match:
                value = int(value_match["value"])
                address = int(value_match["address"])

                memory[address] = encode(mask, value)

                for addr in encode_address(mask, address):
                    recollections[addr] = value
        
        print(sum(memory.values()))
        print(sum(recollections.values()))
