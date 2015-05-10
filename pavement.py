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

    # Syntax
    sh('pylint zebra/ test/zebra/')


@needs('poker', 'zebra')
@task
def default():
    pass