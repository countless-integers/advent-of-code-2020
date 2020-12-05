import os 
from re import match

def validate_passport(passport_data : dict) -> bool:
    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    ]
    return all(field in passport_data for field in required_fields)


def validate_passport_throughly(passport_data : dict) -> bool:
    if int(passport_data["byr"]) < 1920 or int(passport_data["byr"]) > 2002:
        return False
    if int(passport_data["iyr"]) < 2010 or int(passport_data["iyr"]) > 2020:
        return False
    if int(passport_data["eyr"]) < 2020 or int(passport_data["eyr"]) > 2030:
        return False

    unit = passport_data["hgt"][-2:]
    if unit != "in" and unit != "cm":
        return False
    height = int(passport_data["hgt"][:-2])
    if unit == "in" and (height < 59 or height > 76):
        return False
    if unit == "cm" and (height < 150 or height > 193):
        return False

    if passport_data["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if not match(r"^#[a-z0-9]{6}$", passport_data["hcl"]):
        return False
    
    if not match(r"^[0-9]{9}$", passport_data["pid"]):
        return False

    return True


def format_passport_data(passport_data : str) -> dict:
    passport_data = passport_data.replace("\n", " ").split(" ")
    passport_data = [row.split(":") for row in passport_data if row != ""]
    return {entry[0]: entry[1] for entry in passport_data}

if __name__ == "__main__":
    data = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        valid_passports_count = 0
        valid_passports_for_realz_count = 0

        # before reading any further turn on:
        # @see: https://youtu.be/8WEtxJ4-sh4
        passport_data = ""
        for row in input_file:
            if row.strip():
                passport_data += row
            else:
                formatted_data = format_passport_data(passport_data)
                if validate_passport(formatted_data):
                    valid_passports_count += 1
                    if validate_passport_throughly(formatted_data):
                        valid_passports_for_realz_count += 1
                passport_data = ""
        

        if passport_data:
            formatted_data = format_passport_data(passport_data)
            if validate_passport(formatted_data):
                valid_passports_count += 1
                if validate_passport_throughly(formatted_data):
                    valid_passports_for_realz_count += 1

        print(valid_passports_count)
        print(valid_passports_for_realz_count)
