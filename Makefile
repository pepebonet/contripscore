install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black scripts/*.py

lint:
	pylint --disable=R,C scripts/*.py
	
test:
	python -m pytest -vv test.py
	
all: install lint test