# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111

import unittest
from crypt_ar.main import valid, fill_in, compile_word, compile_formula


class TestSolve(unittest.TestCase):

    pass


class TestValid(unittest.TestCase):

    def test_valid_returns_correct_result(self):
        self.assertTrue(valid('1 + 1 == 2'))
        self.assertFalse(valid('01 + 1 == 2'))
        self.assertFalse(valid('1 + 1 != 2'))
        self.assertFalse(valid('1 / 0 == 0'))


class TestFillIn(unittest.TestCase):

    def test_fill_in_returns_unique_results(self):
        self.assertEqual(len(set(fill_in('AB'))), 90)

    def test_fill_in_returns_correct_result_for_same_chars(self):
        self.assertIn('22', list(fill_in('AA')))

    def test_fill_in_works_correct_with_non_letters(self):
        self.assertIn('2 == 3', list(fill_in('A == B')))


class TestCompileWord(unittest.TestCase):

    def test_compile_word_returns_correct_result(self):
        self.assertEqual(compile_word('YOU'), '(1*U + 10*O + 100*Y)')

    def test_compile_word_does_not_change_none_letters(self):
        self.assertEqual(compile_word('=='), '==')


class TestCompileFormula(unittest.TestCase):

    def setUp(self):
        formula = 'AC == BD'
        self.func, self.params = compile_formula(formula)

    def test_compile_formula_returns_correct_params(self):
        self.assertEqual(set(self.params), set('BDCA'))

    def test_compile_formula_returns_correct_lambda(self):
        self.assertTrue(self.func(A=1, C=2, B=1, D=2))
        self.assertFalse(self.func(A=1, C=2, B=2, D=2))
