# Turn off (eval-used), (bad-builtin) pylint error:
# pylint: disable=W0123, W0141

"""
Cryptarithmetic puzzle solver
"""

import argparse
import re
from itertools import permutations
from string import ascii_uppercase


def fill_in(formula):
    """
    Generate all possible fillings-in of letters in formula with digits

    :param formula: str
    :return: Number-string
    """
    letters = "".join(set(char for char in formula if char in ascii_uppercase))
    for digits in permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(formula):
    """
    Formula is valid if it has no numbers with leading zero and evals true

    :param formula: string represent a formula
    :return: True if formula does not raise an error, False otherwise
    """
    try:
        return not re.search(r'\b0[0-9]', formula) and eval(formula) is True
    except ArithmeticError:
        return False


def solve(task):  # pragma: no cover
    """
    Solve cryptarithmetic puzzle

    :param task String to solve, ex.: "ODD + ODD == EVEN"
    :type task str
    """
    for formula in fill_in(task):
        if valid(formula):
            print(formula)


def compile_word(word):
    """
    Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U + 10*O + 100*Y)'
    Non-uppercase words unchanged: compile_word('+') = > '+'
    """
    if word.isupper():
        terms = ['{0}*{1}'.format(10**i, d) for (i, d) in enumerate(word[::-1])]
        return '(' + ' + '.join(terms) + ')'
    else:
        return word


def compile_formula(formula, verbose=False):
    """
    Compile formula into function. Also returns letters found, as a str, in
    same order as parameters of function. For example, 'YOU == ME**2' returns
    (lambda Y, M, E, U, O: (U + 10*O + 100*Y) == (E + 10*M)**2), 'YMEUO'
    """
    letters = "".join(set(char for char in formula if char in ascii_uppercase))
    first_letters = set(re.findall(r'\b([A-Z])[A-Z]', formula))
    params = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)

    # Keep track for numbers with 0 first
    if first_letters:
        tests = ' and '.join(letter + ' != 0 ' for letter in first_letters)
        body = '{0} and ({1})'.format(tests, body)

    func = 'lambda {0}: {1}'.format(params, body)
    if verbose:  # pragma: no cover
        print(func)
    return eval(func), letters


def faster_solve(formula):  # pragma: no cover
    """
    Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string, output is a digit-filled-in string of None.
    This version pre-compiles the formula, only one eval per formula.
    """
    func, letters = compile_formula(formula)
    for digits in permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if func(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                print(formula.translate(table))
        except ArithmeticError:
            pass


def arg_parse():  # pragma: no cover
    """
    Parse console arguments
    """
    parser = argparse.ArgumentParser(description="Solve cryptarithmetic puzzle")
    parser.add_argument("task", action="store")
    args = parser.parse_args()
    task = args.task
    return task


def main():  # pragma: no cover
    """
    Prints the result to a console
    """
    task = arg_parse()
    faster_solve(task)

if __name__ == '__main__':  # pragma: no cover
    main()
