
def names_histogram(.....):
    ......


if __name__ == '__main__':

    with open('names.txt') as file:
        lines = file.readlines()

    hist = names_histogram([line.rstrip() for line in lines], ignore_names=['Jordi', 'Ram'])
    print('Done')
