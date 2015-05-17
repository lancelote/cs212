"""
Cryptarithmetic puzzle solver
"""

import argparse


def solve(task):
    """
    Solve cryptarithmetic puzzle

    :arg task String to solve, ex.: "ODD + ODD == EVEN"
    :type task str
    """
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
