1. Bump version number in `herald/__init__.py`
2. Verify entry in `CHANGELOG.txt`
3. Run `python setup.py sdist bdist_wheel`
4. Run `twine upload dist/*`
5. Add release on GitHub