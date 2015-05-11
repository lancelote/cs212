"""
Zebra puzzle
"""

import itertools


HOUSES = [1, 2, 3, 4, 5]
ORDERINGS = list(itertools.permutations(HOUSES))


def right(house1, house2):
    """
    Is house 1 immediately right of house 2
    """
    return house1 - house2 == 1


def next_to(house1, house2):
    """
    Are houses next to each other
    """
    return abs(house1 - house2) == 1


def zebra_puzzle():
    """
    Return a tuple (water, zebra) indicating their house numbers
    """
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((water, zebra)
                for (red, green, ivory, yellow, blue) in orderings
                for (englishman, spaniard, ukranian, japanese,
                     norwegian) in orderings
                for (dog, snails, fox, horse, zebra) in orderings
                for (coffee, tea, milk, orange_juice, water) in orderings
                for (old_gold, kools, chesterfields, luckystrike,
                     parliaments) in orderings
                if englishman is red
                if spaniard is dog
                if coffee is green
                if ukranian is tea
                if right(green, ivory)
                if old_gold is snails
                if kools is yellow
                if milk is middle
                if norwegian is first
                if next_to(chesterfields, fox)
                if next_to(kools, horse)
                if luckystrike is orange_juice
                if japanese is parliaments
                if next_to(norwegian, blue))
