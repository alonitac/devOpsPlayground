
def get_names_list():
    with open('names.txt') as file:
        lines = file.readlines()
    return [line.rstrip() for line in lines]
