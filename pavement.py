from paver.tasks import task, needs
from paver.easy import sh


@task
def poker():
    # Unit tests
    sh('py.test --cov-report term-missing --cov poker/ test/')

    # Syntax
    sh('pylint --msg-template="{path}:{line}:[{msg_id}({symbol}), {obj}] {msg}"'
       ' poker/ test/ > pylint.txt')


@needs('poker')
@task
def default():
    pass