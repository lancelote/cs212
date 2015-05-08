from paver.tasks import task, needs
from paver.easy import sh


@task
def unit_tests():
    sh('py.test --cov-report term-missing --cov poker/ test/')


@task
def pylint():
    sh('pylint --msg-template="{path}:{line}:[{msg_id}({symbol}), {obj}] {msg}"'
       ' poker/ test/ > pylint.txt')


@needs('unit_tests', 'pylint')
@task
def default():
    pass