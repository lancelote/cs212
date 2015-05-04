"""
Assignment 1

Write a function best_hand(hand) that takes a seven
card hand as input and returns the best possible 5
card hand. The itertools library has some functions
that may help you solve this problem.
"""

import itertools
from poker.main import hand_rank


def best_hand(hand):
    """
    From a 7-card hand, return the best 5 card hand.
    """

    # Your code here
    return sorted(max(itertools.combinations(hand, 5), key=hand_rank))
