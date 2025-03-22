
install:
	pip install -e .[dev,docs]
	pre-commit install

dev:
	uv sync --all-extras
	uv pip install -e .
	uv run pre-commit install

test:
	uv run pytest -s

cov:
	uv run pytest --cov=gvtt

mypy:
	uv run mypy . --ignore-missing-imports

pylint:
	uv run pylint gvtt

ruff:
	ruff --fix gvtt/*.py

git-rm-merged:
	git branch -D `git branch --merged | grep -v \* | xargs`

update:
	pur

update-pre:
	pre-commit autoupdate --bleeding-edge

git-rm-merged:
	git branch -D `git branch --merged | grep -v \* | xargs`

release:
	git push
	git push origin --tags

build:
	rm -rf dist
	pip install build
	python -m build

jupytext:
	jupytext docs/**/*.ipynb --to py

notebooks:
	jupytext docs/**/*.py --to ipynb


docs:
	jb build docs

.PHONY: drc doc docs
