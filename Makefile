lint:
	poetry run flake8

install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

uninstall:
	python3 -m pip uninstall hexlet-code

test:
	poetry run pytest

check:
	poetry run flake8
	poetry run pytest

coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
