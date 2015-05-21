# Turn off (eval-used) pylint error:
# pylint: disable=W0123

"""
Cryptarithmetic puzzle solver
"""

import argparse
import re
from itertools import permutations
from string import ascii_uppercase


def solve(task):  # pragma: no cover
    """
    Solve cryptarithmetic puzzle

    :param task String to solve, ex.: "ODD + ODD == EVEN"
    :type task str
    """
    for formula in fill_in(task):
        if valid(formula):
            print(formula)


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
    solve(task)

if __name__ == '__main__':  # pragma: no cover
    main()
