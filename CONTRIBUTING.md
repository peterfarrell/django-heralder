# Contributing

## Development Environment Setup

1. **Fork and clone the repository.**

2. **Install `uv`**
    This project uses `uv` for fast environment and package management.

    If you don't have `uv` installed:
    ```bash
    pip install uv
    ```

3. **Create a virtual environment and install dependencies.**
    This project uses `uv` for fast environment and package management.

    First, create and activate a virtual environment:
    ```bash
    uv venv
    source .venv/bin/activate
    ```

    Next, install all required dependencies and extras for development in editable mode:
    ```bash
    uv sync --all-extras
    ```

4. **Optional: Change Python version**

    You can change the Python version:
    ```bash
    uv python install 3.10
    ```

    List all Python versions:
    ```bash
    uv python list
    ```

## Supported versions for Twilio and html2text

* Twilio (SemVer) is supported till latest major version - 1 (e.g 9.x.x - 1 = version 8.x.x and higher)
* html2text (CalVer) is supported till current calendar year  - 1 (e.g. 2025 - 1 = version 2024.x.x and newer)

## Running Tests

This will run with a SQLite3 in-memory database:

```bash
uv run runtests.py -v 2
```

## Running Server to See Views

You will need to run migrations:
```bash
uv run manage.py migrate
```

Run server:
```bash
uv run manage.py runserver 0.0.0.0:8000
```