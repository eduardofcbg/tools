import copy
from itertools import zip_longest
from random import shuffle


def zip_pad(*args):
    return zip_longest(*args, fillvalue=None)


def shuffled(iter):
    list_copy = copy.copy(list(iter))
    shuffle(list_copy)

    return list_copy
