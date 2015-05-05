# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111

import unittest
from poker.stat import deal, hand_names


class TestDeal(unittest.TestCase):

    def setUp(self):
        self.ranks = "23456789TJQKA"
        self.suits = "SHDC"
        self.hands = deal(2, 6)

    def test_error_raised_if_too_many_hands(self):
        self.assertRaises(IndexError, deal, 100)

    def test_given_number_of_hands_created(self):
        self.assertEqual(len(self.hands), 2)

    def test_each_hand_has_a_given_number_of_cards(self):
        for hand in self.hands:
            self.assertEqual(len(hand), 6)

    def test_hands_are_random(self):
        self.assertNotEqual(deal(1), deal(1))

    def test_all_cards_in_all_hands_are_valid(self):
        for hand in self.hands:
            for card in hand:
                rank, suit = card[0], card[1]
                self.assertIn(rank, self.ranks)
                self.assertIn(suit, self.suits)

    def test_all_cars_are_unique(self):
        hands = deal(13, 4)  # Use all 52 cards
        used_cards = [card for hand in hands for card in hand]
        self.assertEqual(len(set(used_cards)), 52)


class TestHandNames(unittest.TestCase):

    def test_hand_names_returns_correct_hand_name(self):
        self.assertEqual(hand_names(0), "high card")
        self.assertEqual(hand_names(1), "pair")
        self.assertEqual(hand_names(2), "two pairs")
        self.assertEqual(hand_names(3), "3 of a kind")
        self.assertEqual(hand_names(4), "straight")
        self.assertEqual(hand_names(5), "flush")
        self.assertEqual(hand_names(6), "full house")
        self.assertEqual(hand_names(7), "4 of a kind")
        self.assertEqual(hand_names(8), "straight flush")
