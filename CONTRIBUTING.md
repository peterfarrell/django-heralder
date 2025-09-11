# Contributing

## Development Environment Setup

1.  **Fork and clone the repository.**

2.  **Set up your Python environment.**
    It's highly recommended to use a tool like `pyenv` to manage Python versions. The error `pyenv: python: command not found` indicates that no version is active. You can fix this by running:

    ```bash
    # Example for Python 3.11
    pyenv local 3.11.0
    ```

3.  **Create a virtual environment and install dependencies.**
    This project uses `uv` for fast environment and package management.

    First, create and activate a virtual environment:
    ```bash
    # This creates a virtual environment in a .venv directory
    uv venv
    source .venv/bin/activate
    ```

    Next, install all required dependencies for development in editable mode:
    ```bash
    # This installs the project and all optional/dev dependencies
    uv sync
    ```
## Supported versions for Twilio and html2text
    Twilio is supported till current SemVer - 1
    html2text is supported till current calendar version - 1

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