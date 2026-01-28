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

## Code Style

### Python Code

To format your code with Black, open a terminal and ensure your virtual environment is activated.

```bash
uv run black .
```

## Running Tests

This will run tests with a SQLite3 in-memory database and coverage:
```bash
uv run coverage run -m django test --settings=tests.settings --pythonpath=. -v 2
```

* `--pythonpath=.` is required to set the context otherwise you will recieve the error `ModuleNotFoundError: No module named 'tests'`
* `-v 3` sets the verbosity high enough to be able to see pre-migrate handlers, migrations, and post-migrate handlers.

Show the coverage report to gain feedback on missing test case coverage:
```bash
uv run coverage report --show-missing
```

### Supported environment variables for tests

| Environment Name | Description | Default Value |
| ----- | ----- | ----- |
| `HERALD_TEST_DB_NAME` | The path and name to the SQLite DB name. | `db.sqlite3` |

## Running Server to See Views

You will need to run migrations:
```bash
uv run manage.py migrate
```

Run server:
```bash
uv run manage.py runserver 0.0.0.0:8000
```

Open a browser to: [http://localhost:8000/](http://localhost:8000)