# Hello Venus

A tiny demonstration project that provides a simple greeting function, a command‑line wrapper, unit tests, and a GitHub Actions CI workflow.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m hello "World"
```

## Project layout

```
hello_venus/
├─ hello.py          # greeting function
├─ run_hello.py      # CLI wrapper
├─ test_hello.py     # pytest unit test
├─ requirements.txt   # runtime deps (none beyond stdlib)
├─ .github/
│   └─ workflows/ci.yml   # GitHub Actions CI (ruff + pytest)
└─ README.md
```

## License

MIT – feel free to copy, modify, and publish.
