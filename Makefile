.PHONY: default dev

default: dev

dev:
	PYTHONPATH=api source api/venv/bin/activate && uvicorn api.infra.handlers.main:app --reload
