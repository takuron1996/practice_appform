SHELL = /bin/bash
CONTAINER_NAME = app
APPLICATION = application
DOCKER = docker exec $(CONTAINER_NAME)
PYLINT = $(DOCKER) poetry run pylint
FORMAT_BLACK = $(DOCKER) poetry run black
FORMAT_ISORT = $(DOCKER) poetry run isort
RUN_DJANGO = $(DOCKER) poetry run python manage.py
LINTRCF	= pylintrc.txt
LINTRST = pylintresult.txt
DOCS = docs
PYCS = $(shell find . -type d -name .venv -prune -o -type d -name "__pycache__" -print)
EXCLUDE = -not -name .coveragerc -not -name .gitignore

lint: format
	@if [ ! -e $(LINTRCF) ]; then $(PYLINT) --generate-rcfile > $(LINTRCF) 2> /dev/null ; fi
	@$(PYLINT) --rcfile=$(LINTRCF) `find . -name "*.py"` > $(LINTRST); \
	less $(LINTRST)

format:
	@$(FORMAT_BLACK) .
	@$(FORMAT_ISORT) .

makemigrations:
	$(RUN_DJANGO) makemigrations

migrate:
	$(RUN_DJANGO) migrate

loaddata:
	$(RUN_DJANGO) loaddata crm.json

install:
	$(DOCKER) poetry install

update:
	$(DOCKER) poetry update

test: format
	$(DOCKER) poetry run pytest --cov -vv --cov-report=html

docs:
	$(DOCKER) poetry run pdoc application --html -o $(DOCS) --force

check: format
	$(DOCKER) poetry run mypy --install-types --non-interactive