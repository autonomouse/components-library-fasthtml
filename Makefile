UV_VERSION?=0.8.3
UV?=uvx uv@$(UV_VERSION)

# Colours
RED="\033[0;31m"
YELLOW="\033[0;33m"
GREEN="\033[0;32m"
CYAN="\033[36m"
NC="\033[0m"

## help: Prints the names and descriptions of all targets
help:
	@grep -E '## .*$$' $(MAKEFILE_LIST) | grep -v '@grep' | awk 'BEGIN {FS = ": "}; {sub(/^## /, "", $$1); printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

## check-uv: Check if uv package manager is installed
check-uv:
	@which uv >/dev/null || { \
		echo $(RED)"Error: uv not found. https://docs.astral.sh/uv/getting-started/installation/"; \
		echo "You can install the latest with 'make install-uv'"$(NC); \
		exit 1; \
	}

## install-uv: Install the uv package manager
install-uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh

uv.lock: check-uv
	$(UV) lock

## install: Install project dependencies as specified in the lock file
.PHONY: install
install: uv.lock
	$(UV) sync

## update: Update project dependencies
.PHONY: update
update: uv.lock
	$(UV) sync
	@echo Dont forget to commit the updated lock file after testing

## format: Format code with ruff (alias: fmt)
.PHONY: format fmt
format:
	$(UV) run ruff check --fix --unsafe-fixes --exit-zero . || true
	$(UV) run ruff format .

fmt: format

## lint: Run linting and type checking (alias: check)
.PHONY: lint check
lint:
	$(UV) run ruff check .  || true
	$(UV) run ruff format --check . || true
	$(UV) run mypy .

check: lint

## test: Run unit tests
.PHONY: test unit
test:
	$(UV) run pytest tests/

unit: test

## test-coverage: Run tests with coverage report
.PHONY: test-coverage
test-coverage:
	$(UV) run coverage run -m pytest tests/
	$(UV) run coverage report
	$(UV) run coverage html

## build: Build the package
.PHONY: build
build:
	$(UV) build

## clean: Remove build artifacts
.PHONY: clean
clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

## install-editable: Install package in editable mode for development
.PHONY: install-editable
install-editable:
	$(UV) pip install -e .

## publish: Publish package to PyPI (requires UV_PUBLISH_* env vars)
.PHONY: publish
publish: build
	$(UV) publish

## showcase: Run the component showcase server (Storybook-like)
.PHONY: showcase
showcase:
	$(UV) run python showcase.py
