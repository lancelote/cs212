"""
Assignment 2

# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. The
# black joker, '?B', can be used as any spade or club
# and the red joker, '?R', can be used as any heart
# or diamond.
"""

import itertools
from poker.main import hand_rank
from poker.ps1 import best_hand


def best_wild_hand(hand):
    """
    From a 7-card hand, return the best 5 card hand.
    """

    # Your code here
    hands = [best_hand(cards) for cards in
             itertools.product(*[replace_joker(card) for card in hand])]

    return max(hands, key=hand_rank)


def replace_joker(card):
    """
    :return: a list of the possible replacement of a card
    """
    red_deck = [r+s for r in '23456789TJQKA' for s in 'HD']
    black_deck = [r+s for r in '23456789TJQKA' for s in 'SC']

    if card == "?R":
        return red_deck
    elif card == "?B":
        return black_deck
    else:
        return [card]
