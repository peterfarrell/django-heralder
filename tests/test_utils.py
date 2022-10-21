from django.test import TestCase, override_settings
from django.core.exceptions import ImproperlyConfigured

from herald.utils import get_sent_notification_model
from tests.models import SentNotificationCompany


class UtilsTests(TestCase):
    @override_settings(HERALD_SENT_NOTIFICATION_MODEL="tests.SentNotificationCompany")
    def test_get_sent_notification_model(self):
        self.assertEqual(get_sent_notification_model(), SentNotificationCompany)

    @override_settings(HERALD_SENT_NOTIFICATION_MODEL="fake.Model")
    def test_fake_model(self):
        with self.assertRaisesMessage(
            ImproperlyConfigured,
            "SENT_NOTIFICATION_MODEL refers to model 'fake.Model' that has not been installed",
        ):
            get_sent_notification_model()

    @override_settings(HERALD_SENT_NOTIFICATION_MODEL="really.Long.Path.Model")
    def test_improper_model_string(self):
        with self.assertRaisesMessage(
            ImproperlyConfigured,
            "SENT_NOTIFICATION_MODEL must be of the form 'app_label.model_name'",
        ):
            get_sent_notification_model()
