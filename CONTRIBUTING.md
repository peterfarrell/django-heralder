# Contrinbuting

## Running Tests

This will run with a SQLite3 in-memory database:

```bash
python runtests.py -v 2
```

## Running Server to See Views

You will need to run migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver 0.0.0.0:8000
```