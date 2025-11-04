# Supernova Translation Pipeline

A lightweight project to manage translation workflows with CI/CD integration.

## How to run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make test
make build
---

## 🧩 Step 4 — Optional CI (GitHub Actions)

This creates an automatic test workflow on every push:
```bash
cat > .github/workflows/ci.yml <<'EOF'
name: CI
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - run: python -m pip install --upgrade pip
      - run: pip install -r requirements.txt pytest
      - run: pytest -q
