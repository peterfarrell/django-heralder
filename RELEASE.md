# How to Build and Publish the Package to PyPi

Django Heralder uses UV to build and publish the package.

## How to Choose a Version Number

This library uses [Semantic Versioning (semver)](https://semver.org/), meaning versions follow the `MAJOR.MINOR.PATCH` format.

```
1.2.3
^ ^ ^
| | |
| | | ------- Patch
| | --------- Minor
```

Given a version number MAJOR.MINOR.PATCH, increment the:

| Version Type | Example Version | Compatibility | Description |
| ----- | ----- | ----- | ----- |
| **PATCH** | `1.2.4` | Backward-compatible | Increment for bug fixes and minor, **backward-compatible** improvements. This includes documentation updates. |
| **MINOR** | `1.3.0`| Backward-compatible | Increment for new features or improvements in a **backward-compatible** manner. |
| **MAJOR** | `2.0.0` | Breaking changes (incompatible) | Increment for **breaking changes (incompatible)** that require engineers to modify their applications. This signals a significant release.|

When incrementing the:

* **MAJOR:** Reset the both **MINOR** to` 0` and **PATCH** to `0`
    * Ex: `1.8.9` becomes `2.0.0`
* **MINOR:** Reset the **PATCH** to `0`
    * Ex: `1.8.9` becomes `1.9.0`

## Publish Package Using UV

### Manual

1. Update the `CHANGELOG.md` file.  Move any `[Unreleased]` items into a version using an appropriate SemVer version (see above).
2. Bump the version number in the `pyproject.toml` using the `uv version` command below by providing a positional arugment. This is update the `pyproject.toml` file.

    ```bash
    uv version 0.5.1
    >> Resolved 31 packages in 346ms
    >>     Built django-heralder @ file:///Users/django/Projects/django-heralder
    >> Prepared 1 package in 725ms
    >> Uninstalled 1 package in 1ms
    >> Installed 1 package in 3ms
    >> - django-heralder==0.5.0 (from file:///Users/django/Projects/django-heralder)
    >> + django-heralder==0.5.1 (from file:///Users/django/Projects/django-heralder)
    >> django-heralder 0.5.0 => 0.5.1
    ```

    * Read more about the [`uv version`](https://docs.astral.sh/uv/guides/package/#updating-your-version) command.

3. Commit the file changes to `main` and push to GitHub.

4. Build the package:

    ```bash
    rm -rf dist/
    uv build --no-sources
    ```

    * Use `--no-sources` when building to publish per [recommendatation from UV](https://docs.astral.sh/uv/guides/publish/#building-your-package)

5. Publish the package to `pypi` (production), or `testpypi` (test) package repository:

    ```bash
    uv publish --index [pypi|testpypi]
    ```

    Follow the prompts for a API username `__token__` and password (API token). You can configure an API token in your PyPI account or Test PyPI account.

6. Create a new release and tag on GitHub:
    
    1. Go to [Draft a new release](https://github.com/peterfarrell/django-heralder/releases/new)
    2. Choose tag. If you have not created a tag yet, you can create one "on publish". Use the format of `vX.X.X`.
    3. Set the release title to the version. Ex: `vX.X.X`
    5. In the body for the release, copy the bullets of items from the `CHANGELOG.md`.


### Using GithHub Trusted Publisher

TODO: See [#39 - Enhance publishing using GitHub Actions and PyPI Trusted Publishers](https://github.com/peterfarrell/django-heralder/issues/39)
