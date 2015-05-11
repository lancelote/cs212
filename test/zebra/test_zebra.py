# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111

import unittest
from zebra.main import right


class TestImRight(unittest.TestCase):

    def test_im_right_returns_correct_result(self):
        """
        example house list = [1, 2, 3, 4, 5]
        """
        self.assertFalse(right(1, 2))
        self.assertFalse(right(2, 3))
        self.assertFalse(right(4, 5))
        self.assertFalse(right(5, 1))
        self.assertTrue(right(3, 2))
        self.assertTrue(right(2, 1))
        self.assertTrue(right(5, 4))
