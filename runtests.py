#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line


def runtests():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
    os.environ.setdefault("HERALD_TEST_DB_NAME", ":memory:")
    argv = sys.argv[:1] + ["test"] + sys.argv[1:]
    execute_from_command_line(argv)


if __name__ == "__main__":
    runtests()
