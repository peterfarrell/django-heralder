"""
Notification classes. Used for sending texts and emails
"""
__version__ = '0.1.3'

default_app_config = 'herald.apps.HeraldConfig'


class NotificationRegistry(object):
    """
    Stores the notification classes that get registered.
    """

    def __init__(self):
        self._registry = []

    def register(self, kls):
        """
        Register a notificaion class
        """

        self._registry.append(kls)

    def unregister(self, kls):
        """
        Unregister a notification class
        """

        self._registry.remove(kls)


registry = NotificationRegistry()  # pylint: disable=C0103


def autodiscover():
    """
    Auto discover notification registrations in any file called "notifications" in any app.
    """
    from django.utils.module_loading import autodiscover_modules

    autodiscover_modules('notifications', register_to=registry)
