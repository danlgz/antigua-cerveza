.PHONY: default dev

default: dev

dev:
	source api/venv/bin/activate && cd api && uvicorn main:app --reload
