.PHONY: build clean down up shell migrate bootstrap
check:
				pre-commit run --all-files

test:
				pytest app/tests

mypy:
				mypy .

remove-db:
				rm data.db

init:  remove-db
				PYTHONPATH=. alembic upgrade head && PYTHONPATH=. python app/initial_data.py
