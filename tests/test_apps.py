from django.apps import apps
from django.db.utils import OperationalError, ProgrammingError
from django.test import TestCase
from mock import patch

from herald import registry
from herald.apps import register_notifications
from herald.base import EmailNotification
from herald.models import Notification


class TestRegisterNotification(EmailNotification):
    """A test notification class for app registration tests."""

    verbose_name = "Test Register Notification"
    can_disable = True

    @classmethod
    def get_class_path(cls):
        # Make it stable for tests
        return "tests.test_apps.TestRegisterNotification"


class AppsTests(TestCase):
    """Tests for herald.apps."""

    def setUp(self):
        """Set up for tests."""
        # Store the original registry and clear it for isolated testing
        self.original_registry = list(registry._registry)
        registry._registry.clear()

        # Register our test notification
        registry.register(TestRegisterNotification)
        # Clear Notification table before each test
        Notification.objects.all().delete()
        self.sender = apps.get_app_config("herald")

    def tearDown(self):
        """Tear down after tests."""
        # Unregister to not affect other tests
        registry.unregister(TestRegisterNotification)
        # Restore the original registry
        registry._registry = self.original_registry

    def test_register_new_notification(self):
        """
        Test that a new notification from the registry is created in the database.
        """
        # Arrange
        self.assertEqual(Notification.objects.count(), 0)

        # Act
        register_notifications(sender=self.sender)

        # Assert
        self.assertEqual(Notification.objects.count(), 1)
        notification = Notification.objects.first()
        self.assertEqual(
            notification.notification_class, TestRegisterNotification.get_class_path()
        )
        self.assertEqual(notification.verbose_name, "Test Register Notification")
        self.assertTrue(notification.can_disable)

    def test_update_existing_notification(self):
        """
        Test that an existing notification in the database is updated.
        """
        # Arrange
        Notification.objects.create(
            notification_class=TestRegisterNotification.get_class_path(),
            verbose_name="Old Name",
            can_disable=False,
        )
        self.assertEqual(Notification.objects.count(), 1)

        # Act
        register_notifications(sender=self.sender)

        # Assert
        self.assertEqual(Notification.objects.count(), 1)
        notification = Notification.objects.first()
        self.assertEqual(notification.verbose_name, "Test Register Notification")
        self.assertTrue(notification.can_disable)

    def test_operational_error_is_handled(self):
        """
        Test that an OperationalError during registration is handled gracefully.
        """
        # Arrange
        with patch(
            "herald.models.Notification.objects.get_or_create",
            side_effect=OperationalError("mocked error"),
        ) as mock_get_or_create:
            # Act
            try:
                register_notifications(sender=self.sender)
            except OperationalError:
                self.fail("OperationalError was not handled by the function.")

            # Assert
            mock_get_or_create.assert_called_once()

    def test_programming_error_is_handled(self):
        """
        Test that a ProgrammingError during registration is handled gracefully.
        """
        # Arrange
        with patch(
            "herald.models.Notification.objects.get_or_create",
            side_effect=ProgrammingError("mocked error"),
        ) as mock_get_or_create:
            # Act
            try:
                register_notifications(sender=self.sender)
            except ProgrammingError:
                self.fail("ProgrammingError was not handled by the function.")

            # Assert
            mock_get_or_create.assert_called_once()
