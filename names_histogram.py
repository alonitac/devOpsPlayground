
def names_histogram(.....):
    """
    Calculates how frequent each name is
    Hint: use dictionary

    :param names: list of names (strings)
    :param ignore: (Optional) list of names to ignore
    :return: List of tuples in the form ('John', 4)
             Such that 'John' appears 4 times in the list
    """
    pass   # your code here


if __name__ == '__main__':

    with open('names.txt') as file:
        lines = file.readlines()

    hist = names_histogram([line.rstrip() for line in lines], ignore=['Jordi', 'Ram'])
    print('Done')
