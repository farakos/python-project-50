lint:
	poetry run flake8

install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

uninstall:
	python3 -m pip uninstall hexlet-code

check:
	poetry run flake8
	poetry run pytest

coverage:
	poetry run pytest --cov-report xml tests/
