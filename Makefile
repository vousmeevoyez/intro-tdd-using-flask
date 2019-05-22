clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
run:
	flask run
test:
	python -m unittest discover tests/
coverage:
	coverage run --source app/ -m unittest discover tests/
