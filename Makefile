.PHONY: default dev

default: dev

dev-api:
	PYTHONPATH=api source api/venv/bin/activate && uvicorn api.infra.handlers.main:app --reload

test:
	python -m coverage run -m unittest discover api/
	python -m coverage report

test-report:
	make test
	python -m coverage html
	open htmlcov/index.html

dev-web:
	cd web && pnpm dev

dev:
	make -j 2 dev-api dev-web
