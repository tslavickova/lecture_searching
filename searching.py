import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open (file_path, "r") as file_obj:
        data = json.load(file_obj)
    if field in data.keys():
        return data[field]
    else:
        print(f"Field {field} not exist!")
        return None


def linear_search(list_of_numbers, number):
    list_of_idxs = []
    for idx, element in enumerate(list_of_numbers):
        if element == number:
            list_of_idxs.append(idx)
        else:
            pass
    return {"positions": list_of_idxs, "count": len(list_of_idxs)}


def pattern_search(sequence, pattern):
    set_of_idxs = set()
    pattern_length = len(pattern)
    for idx in range(0, len(sequence) - pattern_length):
        pattern_similarity = 0
        for idx_pattern, pattern_element in enumerate(pattern):
            if sequence[idx + idx_pattern] == pattern_element:
                pattern_similarity = pattern_similarity + 1
            else:
                break
        if pattern_similarity == pattern_length:
            set_of_idxs.add(idx + pattern_length // 2 - 1)
        else:
            pass
    return set_of_idxs

def pattern_search_while(sequence, pattern):
    pos = set()
    index = 0
    while index < len(sequence) - len(pattern):
        if sequence[index:index + len(pattern)] == pattern:
            pos.add(index)
        index = index + 1
    return pos





def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    found_numbers_linear = linear_search(sequential_data, 0)
    print(found_numbers_linear)
    sequential_pattern = pattern_search("sequential.json", "dna_sequence")


if __name__ == '__main__':
    main()
    sequence = [54, 2, 18, 5, 3, 31, 20, 65, -10, 300, 17, 5]
    wanted_numbers = [31, 20]
    found_pattern = pattern_search(sequence, wanted_numbers)
