lint:
	uv run ruff check .

install:
	uv sync

check:
	uv run ruff check .
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml