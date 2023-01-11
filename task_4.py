import json

INPUT_FILE = "output.csv"


def csv_to_list_dict(filename="", delimiter=",", new_line="\n") -> list[dict]:
    new_list = []
    with open(filename) as f:
        for first_line in f:
            first_list_line = list((first_line.rstrip(new_line)).split(delimiter))
            for line_ in f:
                list_line = list((line_.rstrip(new_line)).split(delimiter))
                dict_ = {first_list_line[i]: list_line[i] for i in range(len(first_list_line))}
                new_list.append(dict_)
    return new_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
# пустая строка