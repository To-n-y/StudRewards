test:
	pytest -s -v

.PHONY: test

run:
	python StudRewards/manage.py runserver

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt