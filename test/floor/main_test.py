# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111

import unittest
from floor.main import adjacent, floor_puzzle


class TestAdjacent(unittest.TestCase):

    def test_adjacent_returns_correct_result(self):
        self.assertTrue(adjacent(1, 2))
        self.assertTrue(adjacent(4, 5))
        self.assertTrue(adjacent(5, 4))
        self.assertTrue(adjacent(2, 1))
        self.assertFalse(adjacent(1, 3))
        self.assertFalse(adjacent(3, 5))
        self.assertFalse(adjacent(1, 3))
        self.assertFalse(adjacent(5, 3))


class TestFloorPuzzle(unittest.TestCase):

    def test_floor_puzzle_returns_correct_result(self):
        self.assertEqual(floor_puzzle(), (3, 2, 4, 5, 1))
