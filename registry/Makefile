.DEFAULT_GOAL := install

.PHONY: install
install: venv ## sets up venv and installs the python app to it
	.venv/bin/pip install --upgrade pip setuptools wheel 
	.venv/bin/pip install . 

.PHONY: run
run: install ## start app
	.venv/bin/python app.py

venv:
	python3 -m venv .venv

# Absolutely awesome: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[\.a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; \
			{printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

clean:
	rm -rf .venv || true;
