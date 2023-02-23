PYCS = $(shell find . -type d -name .venv -prune -o -type d -name "__pycache__" -print)

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

prod_build:
	docker-compose -f docker-compose.prod.yml build

prod_up:
	docker-compose -f docker-compose.prod.yml up -d

prod_down:
	docker-compose -f docker-compose.prod.yml down

clean:
	@if [ -d ./data/db ]; then echo "rm -rf ./data/db/*"; rm -rf ./data/db/*; fi
	@if [ -d ./static/* ]; then echo "rm -rf ./static/*"; rm -rf ./static/*; fi
	@for each in ${PYCS} ; do echo "rm -rf $${each}" ; rm -rf $${each} ; done
