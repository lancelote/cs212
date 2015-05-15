"""
SetUp environment for BDD tests
"""
from behave import use_step_matcher

# Select default step matcher, possible variants are: ['re', 'parse', 'cfparse']
# NOTE: PyCharm understands only 're'
#   issue: https://youtrack.jetbrains.com/issue/PY-14532
use_step_matcher('re')
