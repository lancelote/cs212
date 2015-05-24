"""
Paver tasks
"""

from paver.tasks import task, needs
from paver.easy import sh


@task
def poker():
    # Unit tests
    sh('py.test --cov-report term-missing --cov poker/ test/poker/')

    # Syntax
    sh('pylint poker/ test/poker/')


@task
def zebra():
    # Unit tests
    sh('py.test --cov-report term-missing --cov zebra/ test/zebra/')

    # Acceptance tests
    sh('behave test/zebra/acceptance/features/')

    # Syntax validation
    sh('pylint zebra/ test/zebra/')


@task
def crypt_ar():
    # Unit tests
    sh('py.test --cov-report term-missing --cov crypt_ar/ test/crypt_ar/')

    # Acceptance tests
    sh('behave test/crypt_ar/acceptance/features/')

    # Syntax validation
    sh('pylint crypt_ar/ test/crypt_ar/')


@task
def floor():
    # Unit tests
    sh('py.test --cov-report term-missing --cov floor/ test/floor/')

    # Acceptance tests
    sh('behave test/floor/acceptance/features/')

    # Syntax validation
    sh('pylint floor/ test/floor/')


@needs('poker', 'zebra', 'crypt_ar', 'floor')
@task
def default():
    pass
