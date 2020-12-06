import os 
from math import floor, ceil
from pprint import pprint


def decode_seat_data(encoded_id : str) -> int:
    encoded_row = encoded_id[:7]
    row_range = [0, 127]
    for char in encoded_row:
        bleh = ceil((row_range[1] - row_range[0]) / 2)
        if char == "F":
            row_range[1] -= bleh
        elif char == "B":
            row_range[0] += bleh
        else:
            raise Exception(f"Unexpected row char {char}")

    encoded_column = encoded_id[-3:]
    column_range = [0, 7]
    for char in encoded_column:
        bleh = ceil((column_range[1] - column_range[0]) / 2)
        if char == "R":
            column_range[0] += bleh
        elif char == "L":
            column_range[1] -= bleh
        else:
            raise Exception(f"Unexpected column char {char}")
    
    return {
        "id": row_range[1] * 8 + column_range[1],
        "row": row_range[1],
        "column": column_range[1],
    }


if __name__ == "__main__":
    data = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        seating_arrangments = [ [0 for i in range(8) ] for j in range(128) ]
        highest_id = None
        for encoded_id in input_file:
            decoded_seat = decode_seat_data(encoded_id.strip())
            if highest_id == None or decoded_seat["id"] > highest_id:
                highest_id = decoded_seat["id"]
            seating_arrangments[decoded_seat["row"]][decoded_seat["column"]] = 1

        print(highest_id)

        for row_number, row in enumerate(seating_arrangments):
            for column_number, column in enumerate(row):
                if column == 0 and seating_arrangments[row_number][column_number - 1] != 0:
                    print(row_number, column_number, row_number * 8 + column_number)


