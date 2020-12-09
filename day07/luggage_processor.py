from os.path import dirname, realpath
from re import findall


def parse_row(row : str) -> dict:
    matches = findall(r"(\d+ )?([a-z ]*?)bags?", row)
    # matches = [match.strip() for match in matches]
    if matches[1][1].strip() == "contain no other":
        return {matches[0][1].strip(): {}}
    return {matches[0][1].strip(): {k.strip(): int(v) for v, k in matches[1:]}}


def find_bags_containing(target : str, bags : dict) -> set:
    seen_in = set()
    def find(target : str):
        for bag in bags:
            if target in bags[bag]:
                seen_in.add(bag)
                find(bag)
    find(target)

    return seen_in


def count_bags_in_bags(target : str, bags : dict) -> int:
    def count_bags(target : str) -> int:
        count = 1
        for bag in bags[target]:
            count += bags[target][bag] * count_bags(bag)
        return count

    return count_bags(target) - 1


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))

    bags = {}
    with open(dir_path + "/input.txt") as input_file:
        for row in input_file:
            if not row:
                continue
            bags.update(parse_row(row))

    print(len(find_bags_containing('shiny gold', bags)))
    print(count_bags_in_bags('shiny gold', bags))
