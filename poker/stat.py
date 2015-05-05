"""
Calculate simple statistics about poker hands probability
"""

import random
from poker.main import hand_rank


def deal(hands_num, cards_num=5):
    """
    Creates a given number hands with given number of random cards in each

    :param hands_num: number of hands
    :param cards_num: number of cards in hand
    :return: list of hands full of list of cards
    """
    # Check if there are enough cards
    if hands_num*cards_num > 52:
        raise IndexError("Not enough cards to fill all hands")

    deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
    random.shuffle(deck)
    return [deck[cards_num*i:cards_num*(i + 1)] for i in range(hands_num)]


def hand_names(rank):
    """
    :param rank: hand rank
    :return: hand name
    """
    if rank == 8:
        name = "straight flush"
    elif rank == 7:
        name = "4 of a kind"
    elif rank == 6:
        name = "full house"
    elif rank == 5:
        name = "flush"
    elif rank == 4:
        name = "straight"
    elif rank == 3:
        name = "3 of a kind"
    elif rank == 2:
        name = "two pairs"
    elif rank == 1:
        name = "pair"
    else:
        name = "high card"
    return name


def hand_percentage(hand_num=7*10**5):  # pragma: no cover
    """
    Sample hand_num random hands and print a table of percentages for each type
    of hand

    :param hand_num: number of sample hand
    """
    # ToDo : add test coverage
    counts = [0]*9
    for i in range(int(hand_num/10)):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print("%14s: %6.3f %%" % (hand_names(i), 100*counts[i]/hand_num))
