from os.path import dirname, realpath


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        common_positive_answers = None
        common_positive_answers_count = 0
        positive_answers_count = 0
        group_answers = ""
        for row in input_file:
            row = row.strip()
            if row:
                group_answers += row
                if common_positive_answers == None:
                    common_positive_answers = set(row)
                else:
                    common_positive_answers = common_positive_answers & set(row)
            else:
                positive_answers = set(group_answers)
                positive_answers_count += len(positive_answers)
                common_positive_answers_count += len(common_positive_answers)
                group_answers = ""
                common_positive_answers = None

        if group_answers:
            positive_answers = set(group_answers)
            positive_answers_count += len(positive_answers)
            common_positive_answers_count += len(common_positive_answers)

        print(positive_answers_count)
        print(common_positive_answers_count)
