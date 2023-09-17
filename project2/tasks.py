from invoke import task


@task
def lint(c):
    """
    Run linting.
    """
    print("\n -> Running Ruff (Linter)...\n")
    c.run("poetry run ruff check .")
    print("\n -> Running Black (Formatter)...\n")
    c.run("poetry run black --check ./")
    print("\n -> Running mypy (Type Checking)...\n")
    c.run("poetry run mypy --check ./")
    print()


@task
def test(c):
    """
    Run testing.
    """
    c.run("poetry run pytest --cov=./test_project_2 --cov-report=term-missing")
