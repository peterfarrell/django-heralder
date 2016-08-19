"""
Testing custom commands
"""

from datetime import timedelta

from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone
from django.utils.six import StringIO

from herald.models import SentNotification


MSG = 'Successfully deleted {num} notification(s)'
NOTIFICATION_CLASS = 'tests.notifications.MyNotification'


class DeleteNotificationNoArgs(TestCase):

    def test_delete_today(self):
        SentNotification(
            notification_class=NOTIFICATION_CLASS,
            date_sent=timezone.now()
        ).save()
        SentNotification(
            notification_class=NOTIFICATION_CLASS,
            date_sent=timezone.now()+timedelta(days=1)
        ).save()
        out = StringIO()
        call_command('delnotifs', stdout=out)
        self.assertIn(MSG.format(num=1), out.getvalue())

    def test_do_not_delete_tomorrow(self):
        SentNotification(
            notification_class=NOTIFICATION_CLASS,
            date_sent=timezone.now()+timedelta(days=1)
        ).save()
        out = StringIO()
        call_command('delnotifs', stdout=out)
        self.assertIn(MSG.format(num=0), out.getvalue())

    def test_do_not_delete_yesterday(self):
        SentNotification(
            notification_class=NOTIFICATION_CLASS,
            date_sent=timezone.now() - timedelta(days=1)
        ).save()
        out = StringIO()
        call_command('delnotifs', stdout=out)
        self.assertIn(MSG.format(num=0), out.getvalue())


class DeleteNotificationArgs(TestCase):

    def test_delete_today(self):
        SentNotification(
            notification_class=NOTIFICATION_CLASS,
            date_sent=timezone.now()
        ).save()
        SentNotification(
            notification_class=NOTIFICATION_CLASS,
            date_sent=timezone.now()+timedelta(days=1)
        ).save()
        out = StringIO()
        today = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        call_command('delnotifs', stdout=out, start=str(today))
        self.assertIn(MSG.format(num=1), out.getvalue())

    def test_do_not_delete_tomorrow(self):
        SentNotification(
            notification_class=NOTIFICATION_CLASS,
            date_sent=timezone.now()+timedelta(days=1)
        ).save()
        out = StringIO()
        call_command('delnotifs', stdout=out, start=str(timezone.now().today()))
        self.assertIn(MSG.format(num=0), out.getvalue())

    def test_do_not_delete_yesterday(self):
        SentNotification(
            notification_class=NOTIFICATION_CLASS,
            date_sent=timezone.now() - timedelta(days=1)
        ).save()
        out = StringIO()
        call_command('delnotifs', stdout=out, start=str(timezone.now().today()))
        self.assertIn(MSG.format(num=0), out.getvalue())
