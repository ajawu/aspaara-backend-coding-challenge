.PHONY: build clean down up shell migrate bootstrap
check:
				pre-commit run --all-files

test:
				pytest --cov=app --cov-report=term-missing app/tests

mypy:
				mypy app/*
