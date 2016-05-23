# Turn off (function-redefined), (no-name-in-module) pylint errors:
# pylint: disable=E0611, E0102

"""
Acceptance tests
"""

import subprocess
from behave import when, then


@when('I run the zebra program')
def step_impl(context):
    """
    Runs zebra program and captures console output
    """
    context.answer = subprocess.check_output(["python3", "zebra/main.py"])


@then('I see a result of "{text}"')
def step_impl(context, text):
    """
    Compare captured output to given string
    """
    assert context.answer.decode("utf-8").strip() == text
