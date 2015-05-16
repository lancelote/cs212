"""
SetUp environment for BDD tests
"""
from behave import use_step_matcher

# Select default step matcher, possible variants are: ['re', 'parse', 'cfparse']
use_step_matcher('parse')
