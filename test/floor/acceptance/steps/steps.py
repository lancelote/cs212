# Turn off (function-redefined), (no-name-in-module) pylint errors:
# pylint: disable=E0611, E0102

"""
Acceptance tests
"""

from behave import when, then
import subprocess


@when('I run the floor program')
def step_impl(context):
    """
    Runs floor program and captures console output
    """
    context.answer = subprocess.check_output(["python3", "floor/main.py"])


@then('I see a result of "{text}"')
def step_impl(context, text):
    """
    Compare captured output to given string
    """
    print(text)
    print(context.answer.decode("utf-8"))
    assert context.answer.decode("utf-8").strip() == text
