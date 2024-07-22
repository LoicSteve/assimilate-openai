install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py oalib/*.py \
		# streamlit-apps/uberDemo.py

refactor: format lint

lint:
	pylint --disable=R,C,no-value-for-parameter --ignore-patterns=test_.*?py *.py oalib/*.py 

all: install lint test