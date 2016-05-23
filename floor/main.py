"""
Floor puzzle
"""

# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on
# different floors of a five-floor apartment building.
#
# Hopper does not live on the top floor.
# Kay does not live on the bottom floor.
# Liskov does not live on either the top or the bottom floor.
# Perlis lives on a higher floor than does Kay.
# Ritchie does not live on a floor adjacent to Liskov's.
# Liskov does not live on a floor adjacent to Kay's.
#
# Where does everyone live?
#
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay,
# Liskov, Perlis, and Ritchie.

from itertools import permutations


def adjacent(floor_1, floor_2):
    """
    Check if two floors are adjacent

    :param floor_1: int
    :param floor_2: int
    :return: bool
    """
    return abs(floor_1 - floor_2) == 1


def floor_puzzle():
    """
    Solve floor puzzle
    """
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = list(permutations(floors))
    answer = next((Hopper, Kay, Liskov, Perlis, Ritchie)
                  for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
                  if Hopper is not top
                  if Kay is not bottom
                  if Liskov is not top
                  if Liskov is not bottom
                  if Perlis > Kay
                  if not adjacent(Ritchie, Liskov)
                  if not adjacent(Liskov, Kay))
    return answer


def main():  # pragma: no cover
    """
    Print result
    """
    answer = floor_puzzle()
    print("Hopper: {0}, Kay: {1}, Liskov: {2}, "
          "Perlis: {3}, Ritchie: {4}".format(*answer))

if __name__ == '__main__':  # pragma: no cover
    main()
