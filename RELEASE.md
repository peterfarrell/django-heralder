# How to Release

## Prerequistics

1. Install `setuptools` and `twine`:

    ```bash
    pip install setuptools twine
    ```

## Procedure

1. Bump version number in `herald/__init__.py` and commit to source control.

2. Verify entry in `CHANGELOG.md`.

3. Build distribution:
     
     ```bash
     python setup.py sdist bdist_wheel
     ```

4. Upload the distribution to PyPI and follow the prompts to provide the API token:

    ```bash
    twine upload dist/*
    ```

5. Create a new release and tag on GitHub:
    
    1. Go to [Draft a new release](https://github.com/peterfarrell/django-heralder/releases/new)
    2. Choose tag. If you have not created a tag yet, you can create one "on publish". Use the format of `vX.X.X`.
    3. Set the release title to the version. Ex: `vX.X.X`
    5. In the body for the release, copy the bullets of items from the `CHANGELOG.md`.