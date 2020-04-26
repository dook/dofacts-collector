from invoke import task


@task
def isort(c):
    c.run(f"isort -rc .")


@task
def black(c):
    c.run(f"black .")


@task
def reformat(c):
    isort(c)
    black(c)


@task
def lint(c):
    c.run(f"flake8")
