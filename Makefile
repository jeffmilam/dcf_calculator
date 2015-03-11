all:setup

setup:
	@echo ">>> Setting up virtualenv"
	virtualenv .venv && source .venv/bin/activate
	@echo ">>> Installing dependancies from requirements.txt"
	.venv/bin/pip install -r requirements.txt

tests:
	nosetests

.PHONY: all setup tests
