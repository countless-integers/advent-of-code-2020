from os.path import dirname, realpath
from typing import List
from itertools import chain
from re import match, findall


class TicketValidator:
    rules = {}


    def addRule(self, rule : str) -> None:
        field, ranges = rule.split(":")
        ranges = findall(r"\d+-\d+", ranges)
        ranges = [r.split("-") for r in ranges]
        self.rules[field] = [[int(v) for v in r] for r in ranges]


    def addRules(self, rules : List[str]) -> None:
        for rule in rules:
            self.addRule(rule)


    def validate_all(self, values : List[int]) -> dict:
        result = {
            "invalid_values": [],
        }
        for v in values:
            is_valid = False
            for field_ranges in self.rules.values():
                for min_val, max_val in field_ranges:
                    if v >= min_val and v <= max_val:
                        is_valid = True
                        break
                if is_valid == True:
                    break
            if not is_valid:
                result["invalid_values"].append(v)
        return result


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        ignore = [
            "\n",
            "your ticket:\n",
            "nearby tickets:\n",
        ]
        ignored = 0
        sum_of_invalid = 0
        validator = TicketValidator()
        for line in input_file:
            if line in ignore:
                ignored += 1
                continue
            if ignored == 0:
                validator.addRule(line)
            elif ignored > 0:
                result = validator.validate_all([int(v) for v in line.split(",")])
                sum_of_invalid += sum(result["invalid_values"])

        print(sum_of_invalid)
