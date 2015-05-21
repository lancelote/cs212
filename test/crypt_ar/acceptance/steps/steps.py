# Turn off (function-redefined), (no-name-in-module) pylint errors:
# pylint: disable=E0611, E0102

"""
Acceptance tests
"""

from behave import when, then
import subprocess


@when('I run the program with argument "{text}"')
def step_impl(context, text):
    """
    Runs program and captures console output
    """
    context.answer = subprocess.check_output(['python3',
                                              'crypt_ar/main.py',
                                              '{0}'.format(text)])


@then('I see a result of "{text}"')
def step_impl(context, text):
    """
    Compare captured output to given string
    """
    answer = context.answer.decode("utf-8").strip().split('\n')
    text = text.split('\\n')
    assert answer == text
