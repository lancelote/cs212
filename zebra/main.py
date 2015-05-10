"""
Zebra puzzle
"""

import itertools


HOUSES = [1, 2, 3, 4, 5]
ORDERINGS = list(itertools.permutations(HOUSES))


def im_right(h1, h2):
    """
    Is house 1 immediately right of house 2
    """
    return h1 - h2 == 1


def next_to(h1, h2):
    """
    Are houses next to each other
    """
    return abs(h1 - h2) == 1


for (red, green, ivory, yellow, blue) in ORDERINGS:
    for (englishman, spaniard, ukranian, japanese, norwegian) in ORDERINGS:
        for (dog, snails, fox, horse, zebra) in ORDERINGS:
            for (coffee, tea, milk, oj, water) in ORDERINGS:
                for (old_gold, kools, chesterfields, luckystrike,
                     parliaments) in ORDERINGS:
                    if (englishman is red):
                        print("TaDa")
