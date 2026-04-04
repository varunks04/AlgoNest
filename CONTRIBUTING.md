# Contributing

Thank you for contributing to AlgoNest.

## Clone and Setup

```bash
git clone https://github.com/varunks04/AlgoNest.git
cd AlgoNest
pip install -e .[dev]
```

## Run Tests

```bash
python -m pytest -q tests
```

## Coding Rules

- Keep implementations deterministic and side-effect aware.
- Preserve existing public API names unless the change explicitly targets API evolution.
- Prefer clear, typed signatures and concise docstrings.
- Add or update tests for any behavior change.

## Pull Request Guidelines

- Keep PR scope focused and explain the motivation clearly.
- Include test coverage for new behavior and edge cases.
- Update documentation when public behavior or usage changes.
- Ensure all tests pass before requesting review.
