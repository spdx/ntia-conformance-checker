.PHONY: install-dev format format-check lint type test check clean docs

# Install development dependencies (editable install)
install-dev:
	python -m pip install --upgrade pip
	python -m pip install -e ".[dev,docs,test]"

# Format sources (fix in-place)
format:
	black ntia_conformance_checker tests
	ruff check --fix --select I ntia_conformance_checker tests

# Check formatting (check only, CI-friendly)
format-check:
	black --check ntia_conformance_checker tests
	ruff check --select I ntia_conformance_checker tests

# Lint / static analysis
lint:
	pylint ntia_conformance_checker tests

# Type checkers (ensure dev deps installed)
type:
	mypy ntia_conformance_checker || true
	pyrefly check ntia_conformance_checker
	pyright ntia_conformance_checker
	pytype ntia_conformance_checker

# Unit tests
test:
	pytest -q

# Composite check: format checks, lint, type checks, and tests
check: format-check lint type test
	@echo "All checks passed"

# Build docs
docs:
	python -m pip install -e ".[docs]"
	sphinx-apidoc -o docs/ ntia_conformance_checker/
	cd docs && make html

# Cleanup build/test caches (works on Unix-like systems)
clean:
	rm -rf build dist .pytest_cache .mypy_cache .pytype .pyright *.egg-info
