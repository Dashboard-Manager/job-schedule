#!/bin/bash
echo "Start tests and linter configuration"

if [ $PWD == "/src" ]; then
    echo "Run pytest"
    pytest -s -v --no-migrations
    echo "End pytest"

    echo "Run coverage"
    pytest --cov=apps --cov=config --cov-config=.coveragerc && coverage html
    echo "End coverage"

    echo "Run mypy"
    mypy . --config-file mypy.ini
    echo "End mypy"

    cd ..
    echo "Run flake8"
    flake8 /src --config=setup.cfg
    echo "End flake8"

    echo "Run isort"
    isort /src --settings-path=.isort.cfg
    echo "End isort"
else
    echo "Run pytest"
    pipenv run pytest -s -v --no-migrations
    echo "End pytest"

    echo "Run coverage"
    pipenv run pytest --cov=apps --cov=config --cov-config=.coveragerc && coverage html
    echo "End coverage"

    echo "Run mypy"
    pipenv run mypy . --config-file mypy.ini
    echo "End mypy"
    cd ..
    echo "Run flake8"
    flake8 . --config=setup.cfg
    echo "End flake8"

    echo "Run isort"
    isort . --settings-path=.isort.cfg
    echo "End isort"
fi

echo "End of tests and linter configuration"
