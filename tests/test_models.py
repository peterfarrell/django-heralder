from mock import patch

from django.test import TestCase, override_settings

from herald.models import SentNotification, Notification
from herald.utils import get_sent_notification_model
from tests.notifications import MyNotification
from tests.models import SentNotificationCompany


class SentNotificationTests(TestCase):
    def test_str(self):
        notification = SentNotification(
            notification_class="tests.notifications.MyNotification"
        )
        self.assertEqual(str(notification), "tests.notifications.MyNotification")

    def test_get_recipients(self):
        notification = SentNotification(recipients="test@test.com,example@example.com")
        self.assertListEqual(
            notification.get_recipients(), ["test@test.com", "example@example.com"]
        )

    def test_get_extra_data_none(self):
        notification = SentNotification()
        self.assertDictEqual(notification.get_extra_data(), {})

    def test_get_extra_data(self):
        notification = SentNotification(extra_data='{"something":["one","two"]}')
        self.assertDictEqual(
            notification.get_extra_data(), {"something": ["one", "two"]}
        )

    def test_resend(self):
        notification = SentNotification(
            notification_class="tests.notifications.MyNotification"
        )
        with patch.object(MyNotification, "resend") as mocked_resend:
            notification.resend()
            mocked_resend.assert_called_once_with(notification)


class SwappedSentNotificationTests(TestCase):
    def test_swapped_model(self):
        notification = SentNotificationCompany(
            notification_class="tests.notifications.MyNotification",
            company_name="My Company",
        )
        self.assertEqual(notification.company_name, "My Company")

    @override_settings(HERALD_SENT_NOTIFICATION_MODEL="tests.SentNotificationCompany")
    def test_get_sent_notification_model(self):
        self.assertEqual(
            get_sent_notification_model(), SentNotificationCompany
        )


class NotificationTests(TestCase):
    def test_str(self):
        notification = Notification(
            notification_class="tests.notifications.MyNotification"
        )
        self.assertEqual(str(notification), "tests.notifications.MyNotification")
