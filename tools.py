def read_input_as_string(problem):
    filename = f"./inputs/{problem}_input.txt"
    with open(filename, "r") as file:
        string = file.read()
    return string


def read_input_line_wise(problem):
    filename = f"./inputs/{problem}_input.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines
