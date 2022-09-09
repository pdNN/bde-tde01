.ONESHELL:

.PHONY: install test clean

install:
	@python3 -m pip install virtualenv
	@python3 -m virtualenv venv
	@. ./venv/bin/activate
	@pip install -r ./requirements.txt

clean:
	@rm -rf ./venv
	@rm -rf ./test/__pycache__
	@echo "Project cleaned"
