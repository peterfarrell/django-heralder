import django
from django.core.management import call_command
from django.test import TestCase

from mock import patch


class MigrationTests(TestCase):
    def test_no_migrations_created(self):
        with patch('sys.exit') as exit_mocked:
            if django.VERSION < (1, 10):
                # django < 1.10 uses an "exit" param that works the opposite from django > 1.10's check param
                call_command('makemigrations', 'herald', dry_run=True, exit=True, verbosity=0)
                exit_mocked.assert_called_with(1)
            else:
                call_command('makemigrations', 'herald', dry_run=True, check=True, verbosity=0)
                exit_mocked.assert_not_called()
