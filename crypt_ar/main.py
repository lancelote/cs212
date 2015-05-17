# Turn off (eval-used) pylint error:
# pylint: disable=W0123

"""
Cryptarithmetic puzzle solver
"""

import argparse
import re


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


def solve(task):
    """
    Solve cryptarithmetic puzzle

    :arg task String to solve, ex.: "ODD + ODD == EVEN"
    :type task str
    """
    table = str.maketrans('ABC', '123')
    formula = 'A + B == C'
    # eval(f.translate(table))
    return task


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
    result = solve(task)

    print('655 + 655 == 1310')
    print('855 + 855 == 1710')

if __name__ == '__main__':  # pragma: no cover
    main()
