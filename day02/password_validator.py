import os 


def validate_password(policy : str, password : str) -> bool:
    char_range, char = policy.split(" ")
    bottom_range, top_range = (int(numeric) for numeric in char_range.split("-"))
    char_count = 0
    for letter in sorted(password):
        if letter > char:
            break
        if letter != char:
            continue
        char_count += 1 
        if char_count > top_range:
            return False

    return char_count >= bottom_range


def validate_password_method_2(policy : str, password : str) -> bool:
    char_range, char = policy.split(" ")
    first_position, second_position = (int(numeric) for numeric in char_range.split("-"))
    
    return int(password[first_position - 1] == char) + int(password[second_position - 1] == char) == 1


if __name__ == "__main__":
    data = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        data = [row.strip().split(": ") for row in input_file]

    valid_count = 0
    for policy, password in data:
        if validate_password(policy, password):
            valid_count += 1

    print(valid_count)

    valid_count = 0
    for policy, password in data:
        if validate_password_method_2(policy, password):
            valid_count += 1

    print(valid_count)