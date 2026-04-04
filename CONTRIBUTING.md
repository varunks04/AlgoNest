# Contributing Guide

Thank you for contributing to algonest.

## Setup

1. Use Python 3.8+.
2. Install dev dependencies:

```bash
pip install -e .[dev]
```

3. Run tests:

```bash
python -m pytest -q tests
```

## Pull Request Checklist

- Follow phase scope in Agent Docs.
- Add or update tests for every behavior change.
- Keep public imports in `algonest/__init__.py` consistent.
- Keep docstrings and complexity notes up to date.

## Coding Standards

- Use clear naming.
- Prefer iterative solutions where phase rules require it.
- Avoid hidden side effects and input mutation unless documented.
