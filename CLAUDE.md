# CLAUDE.md

- Use the project virtualenv for everything: `.venv/bin/python hello.py`, `.venv/bin/python -m pytest -v`.
- Don't use the bare `python3`: on the maintainer's machine it resolves to Anaconda Python 3.7, where pytest crashes on startup (exit 132).
- If `.venv` is missing, create it with `/usr/bin/python3 -m venv .venv && .venv/bin/pip install pytest`.
