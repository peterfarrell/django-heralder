#!/usr/bin/env python
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "herald"))
os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
from django.core import management

if __name__ == "__main__":
    management.execute_from_command_line()
