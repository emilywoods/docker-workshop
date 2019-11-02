.DEFAULT_GOAL := help

.PHONY: install
install: venv ## sets up venv and installs the python app to it
	.venv/bin/pip install --upgrade pip setuptools wheel 
	.venv/bin/pip install . 

.PHONY: run
run: install ## start app
	.venv/bin/python app.py


.PHONY: help
help:
	@echo ""
	@echo "Available targets:"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

.PHONY: clean
clean: ## clean up afterwards
	rm -rf .venv || true;

venv:
	python3 -m venv .venv
