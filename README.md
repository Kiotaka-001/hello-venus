# Hello Venus

[![Build Status](https://github.com/Kiotaka-001/hello-venus/actions/workflows/ci.yml/badge.svg)](https://github.com/Kiotaka-001/hello-venus/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A minimal yet fully‑featured Python greeting library that demonstrates:

- clean package layout,
- a reusable `greet` function,
- a command‑line entry point,
- unit testing with pytest,
- linting with ruff,
- continuous integration via GitHub Actions,
- optional Flask‑based web API.

**Use case:** Tiny utilities, teaching demos, or as a starter template for new Python packages.

**Inspiration:** Classic “Hello, World!” examples expanded with modern tooling.

## Quick start

```bash
# Clone the repo (or copy the folder)
git clone https://github.com/Kiotaka-001/hello-venus.git
cd hello-venus

# Create a virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the CLI
python -m hello "World"
```

## Project layout

```
hello-venus/
├─ hello.py          # greeting function
├─ run_hello.py      # CLI wrapper
├─ test_hello.py     # pytest unit test
├─ api.py            # optional Flask API (demo)
├─ requirements.txt   # dependencies (ruff, pytest, Flask)
├─ pyproject.toml     # package metadata
├─ .github/
│   └─ workflows/ci.yml   # CI workflow (ruff + pytest + mypy)
├─ .github/ISSUE_TEMPLATE/bug_report.md
├─ .github/ISSUE_TEMPLATE/feature_request.md
├─ README.md
└─ LICENSE
```


## License

MIT – feel free to copy, modify, and publish.
