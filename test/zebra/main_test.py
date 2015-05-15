# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111

import unittest
from zebra.main import right, next_to, zebra_puzzle


class TestImRight(unittest.TestCase):

    def test_im_right_returns_correct_result(self):
        """
        Example house list = [1, 2, 3, 4, 5]
        """
        self.assertTrue(right(3, 2))
        self.assertTrue(right(2, 1))
        self.assertTrue(right(5, 4))
        self.assertFalse(right(1, 2))
        self.assertFalse(right(2, 3))
        self.assertFalse(right(4, 5))
        self.assertFalse(right(5, 1))

    def test_next_to_returns_correct_result(self):
        """
        Example house list = [1, 2, 3, 4, 5]
        """
        self.assertTrue(next_to(1, 2))
        self.assertTrue(next_to(3, 4))
        self.assertTrue(next_to(4, 5))
        self.assertTrue(next_to(2, 1))
        self.assertFalse(next_to(1, 5))
        self.assertFalse(next_to(5, 1))
        self.assertFalse(next_to(2, 4))

    def test_zebra_puzzle_solves_the_problem(self):
        self.assertEqual(zebra_puzzle(), (1, 5, (3, 4, 2, 5, 1)))
