install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

package-install:
	pip install --user --force-reinstall dist/*.whl

# publish:
# 	poetry publish --dry-run

stylish:
	poetry run gendiff --f stylish ./tests/fixtures/json/file1_flat.json ./tests/fixtures/json/file2_flat.json
	poetry run gendiff --format stylish ./tests/fixtures/json/file1_nested.json ./tests/fixtures/json/file2_nested.json

plain:
	poetry run gendiff --f plain ./tests/fixtures/json/file1_flat.json ./tests/fixtures/json/file2_flat.json
	poetry run gendiff --format plain ./tests/fixtures/json/file1_nested.json ./tests/fixtures/json/file2_nested.json