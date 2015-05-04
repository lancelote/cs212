# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111

import unittest
from poker.main import poker, hand_rank, card_ranks, straight, flush, kind


class TestKind(unittest.TestCase):

    def setUp(self):
        self.k4 = card_ranks("9D 9H 9S 9C 7D".split())  # four kind

    def test_kind_returns_correct_rank(self):
        self.assertEqual(kind(4, self.k4), 9)
        self.assertIsNone(kind(3, self.k4))
        self.assertIsNone(kind(2, self.k4))
        self.assertEqual(kind(1, self.k4), 7)


class TestStraight(unittest.TestCase):

    def setUp(self):
        self.st = [6, 5, 4, 3, 2]  # straight
        self.no = [7, 5, 4, 3, 2]  # nothing

    def test_straight_returns_true_if_straight_else_false(self):
        self.assertTrue(straight(self.st))
        self.assertFalse(straight(self.no))


class TestFlush(unittest.TestCase):

    def setUp(self):
        self.fl = "2C 3C 5C 6C 7C".split()  # flush
        self.no = "2C 3C 5C 6C 7D".split()  # nothing

    def test_flush_returns_true_if_flush_else_false(self):
        self.assertTrue(flush(self.fl))
        self.assertFalse(flush(self.no))


class TestCardRanks(unittest.TestCase):

    def setUp(self):
        self.sf = "6C 7C 8C 9C TC".split()  # straight flush
        self.k4 = "9D 9H 9S 9C 7D".split()  # four kind
        self.fh = "TD TC TH 7C 7D".split()  # full house

    def test_card_ranks_returns_correct_list_of_ranks(self):
        self.assertListEqual(card_ranks(self.sf), [10, 9, 8, 7, 6])
        self.assertListEqual(card_ranks(self.k4), [9, 9, 9, 9, 7])
        self.assertListEqual(card_ranks(self.fh), [10, 10, 10, 7, 7])


class TestHandRank(unittest.TestCase):

    def setUp(self):
        self.sf = "6C 7C 8C 9C TC".split()  # straight flash
        self.fk = "9D 9H 9S 9C 7D".split()  # four kind
        self.fh = "TD TC TH 7C 7D".split()  # full house
        self.fl = "5C 7C 8C 9C AC".split()  # flush
        self.st = "5D 6C 7C 8C 9C".split()  # straight
        self.k3 = "5C 5D 5H 3C TD".split()  # kind tree
        self.tp = "5C 5D 6C 6D 7C".split()  # two pairs
        self.k2 = "5C 5D 3C 7C 9C".split()  # two kind
        self.no = "3C 4C 6C 8C AD".split()  # nothing

    def test_hand_rank_returns_correct_tuple(self):
        self.assertEqual(hand_rank(self.sf), (8, 10))
        self.assertEqual(hand_rank(self.fk), (7, 9, 7))
        self.assertEqual(hand_rank(self.fh), (6, 10, 7))
        self.assertEqual(hand_rank(self.fl), (5, [14, 9, 8, 7, 5]))
        self.assertEqual(hand_rank(self.st), (4, 9))
        self.assertEqual(hand_rank(self.k3), (3, 5, [10, 5, 5, 5, 3]))
        self.assertEqual(hand_rank(self.tp), (2, [6, 5], [7, 6, 6, 5, 5]))
        self.assertEqual(hand_rank(self.k2), (1, 5, [9, 7, 5, 5, 3]))
        self.assertEqual(hand_rank(self.no), (0, [14, 8, 6, 4, 3]))


class TestPoker(unittest.TestCase):

    def setUp(self):
        self.sf = "6C 7C 8C 9C TC".split()  # straight flush
        self.k4 = "9D 9H 9S 9C 7D".split()  # four kind
        self.fh = "TD TC TH 7C 7D".split()  # full house
        self.tp = "5S 5D 9H 9C 6S".split()  # two pairs
        self.s1 = "AS 2S 3S 4S 5C".split()  # straight from ace
        self.s2 = "2C 3S 4S 5S 6S".split()  # simple straight
        self.ah = "AS 2S 3S 4S 6C".split()  # ace high
        self.sh = "2S 3S 4S 6C 7D".split()  # seven high

    def test_poker_returns_best_hand(self):
        self.assertEqual(poker([self.s1, self.s2, self.ah, self.sh]), [self.s2])
        self.assertEqual(poker([self.sf, self.k4, self.fh]), [self.sf])
        self.assertEqual(poker([self.k4, self.fh]), [self.k4])
        self.assertEqual(poker([self.fh, self.fh]), [self.fh, self.fh])

        # If there is only one hand
        self.assertEqual(poker([self.fh]), [self.fh])

        # If there are 100 hand
        self.assertEqual(poker([self.sf] + [self.fh]*99), [self.sf])
