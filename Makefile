SHELL := /bin/bash

# this is the default
.PHONY: run
run: venv
	./venv/bin/python GMEPriceBot.py

.PHONY: german
german: venv
	./venv/bin/python german_exchanges.py

venv: venv/touchfile

venv/touchfile: requirements.txt
	echo "###########################################"
	echo "Setting up virtualenv with dependencies..."
	echo "###########################################"
	python3 -m virtualenv -p $(shell which python3.8) venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r "requirements.txt"
	touch venv/touchfile

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
