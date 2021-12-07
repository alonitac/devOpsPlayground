# install by: pip install matplotlib
import matplotlib.pyplot as plt
import pandas
from collections import Counter

names = ['adham','adham','basel','samer','aatef','basel','karam','hasan']
def names_histogram(names,ignore=['hasan', 'aatef']):
    """
    Calculates how frequent each name is
    Hint: use dictionary

    :param names: list of names (strings)
    :param ignore: (Optional) list of names to ignore
    :return: List of tuples in the form ('John', 4)
             Such that 'John' appears 4 times in the list
    """
    freq = {}
    for item in names:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    # for key, value in freq.items():
    #     print(key, value)
    return freq
def draw_first(hist,n=8):
    lists = sorted(hist.items())
    x, y = zip(*lists)
    plt.plot(x, y)
    plt.show()

hist1 = names_histogram(names)
print(hist1)
draw_first(hist1)


