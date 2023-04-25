def get_todos(filepath):
    """Read a text file and return" the list of
        to-dos list """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    """Write todos list into the text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


FREEZING_POINT = 0
BOILING_POINT = 100


def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"


if __name__ == "main":
    print("Hello")
