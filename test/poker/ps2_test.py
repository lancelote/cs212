# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111

import unittest
from poker.ps2 import best_wild_hand


class TestBestHand(unittest.TestCase):

    def setUp(self):
        self.h1 = "6C 7C 8C 9C TC 5C ?B".split()
        self.h2 = "TD TC 5H 5C 7C ?R ?B".split()
        self.h3 = "JD TC TH 7C 7D 7S 7H".split()

    def test_best_hand_returns_best_card_combination(self):
        self.assertEqual(best_wild_hand(self.h1),
                         ['7C', '8C', '9C', 'JC', 'TC'])
        self.assertEqual(best_wild_hand(self.h2),
                         ['7C', 'TC', 'TD', 'TH', 'TS'])
        self.assertEqual(best_wild_hand(self.h3),
                         ['7C', '7D', '7H', '7S', 'JD'])
