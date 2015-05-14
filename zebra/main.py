"""
Zebra puzzle
"""

import itertools


HOUSES = [1, 2, 3, 4, 5]
ORDERINGS = list(itertools.permutations(HOUSES))


def right(house1, house2):
    """
    Is house 1 immediately right of house 2

    :type house1 int
    :type house2 int
    :return bool
    """
    return house1 - house2 == 1


def next_to(house1, house2):
    """
    Are houses next to each other

    :type house1 int
    :type house2 int
    :return bool
    """
    return abs(house1 - house2) == 1


def zebra_puzzle():
    """
    Solver for zebra puzzle

    :return a tuple (water, zebra) indicating their house numbers
    """
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    answer = next((water, zebra,
                   (englishman, spaniard, ukranian, japanese, norwegian))
                  for (red, green, ivory, yellow, blue) in orderings
                  if right(green, ivory)
                  for (englishman, spaniard, ukranian, japanese,
                       norwegian) in orderings
                  if englishman is red
                  if norwegian is first
                  if next_to(norwegian, blue)
                  for (dog, snails, fox, horse, zebra) in orderings
                  if spaniard is dog
                  for (coffee, tea, milk, orange_juice, water) in orderings
                  if coffee is green
                  if ukranian is tea
                  if milk is middle
                  for (old_gold, kools, chesterfields, luckystrike,
                       parliaments) in orderings
                  if old_gold is snails
                  if kools is yellow
                  if next_to(chesterfields, fox)
                  if next_to(kools, horse)
                  if luckystrike is orange_juice
                  if japanese is parliaments)
    return answer

if __name__ == "__main__":
    result = zebra_puzzle()
    output = []

    # Who drinks water?
    if result[0] == result[2][0]:
        output.append("Englishman")
    elif result[0] == result[2][1]:
        output.append("Spaniard")
    elif result[0] == result[2][2]:
        output.append("Ukranian")
    elif result[0] == result[2][3]:
        output.append("Japanese")
    elif result[0] == result[2][4]:
        output.append("Norwegian")

    # Who owns the zebra?
    if result[1] == result[2][0]:
        output.append("Englishman")
    elif result[1] == result[2][1]:
        output.append("Spaniard")
    elif result[1] == result[2][2]:
        output.append("Ukranian")
    elif result[1] == result[2][3]:
        output.append("Japanese")
    elif result[1] == result[2][4]:
        output.append("Norwegian")

    print("{0} drinks water\n{1} owns the zebra".format(*output))