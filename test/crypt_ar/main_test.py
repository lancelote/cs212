# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111

import unittest
from crypt_ar.main import solve, valid


class TestSolve(unittest.TestCase):

    pass


class TestValid(unittest.TestCase):

    def test_valid_returns_correct_result(self):
        self.assertTrue(valid('1 + 1 == 2'))
        self.assertFalse(valid('01 + 1 == 2'))
        self.assertFalse(valid('1 + 1 != 2'))
        self.assertFalse(valid('1 / 0 == 0'))
