# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111

import unittest
from long_pal.main import longest_subpalindrome_slice as longest


class TestLongest(unittest.TestCase):

    def test_longest_returns_correct_result(self):
        self.assertEqual(longest('racecar'), (0, 7))
        self.assertEqual(longest('Racecar'), (0, 7))
        self.assertEqual(longest('RacecarX'), (0, 7))
        self.assertEqual(longest('Race carr'), (7, 9))
        self.assertEqual(longest(''), (0, 0))
        self.assertEqual(longest('something rac e car going'), (8, 21))
        self.assertEqual(longest('xxxxx'), (0, 5))
        self.assertEqual(longest('Mad am I ma dam.'), (0, 15))
