# Turn off (function-redefined), (no-name-in-module) pylint errors:
# pylint: disable=E0611, E0102

"""
Acceptance tests
"""

from behave import when, then
from subprocess import check_output


@when('I run the long_pal program with "{argument}"')
def step_impl(context, argument):
    """
    Runs long_pal program and captures console output
    """
    context.answer = check_output(["python3", "long_pal/main.py", argument])


@then('I see a result of "{result}"')
def step_impl(context, result):
    """
    Compare captured output to given string
    """
    print(context.answer.decode("utf-8").strip())
    print(result)
    assert context.answer.decode("utf-8").strip() == result
