def register_notification():
    """
    Registers the given notification with Django Herold

    """

    from herald import registry
    from herald.base import NotificationBase

    def _notification_wrapper(notification_class):

        if not issubclass(notification_class, NotificationBase):
            raise ValueError('Notification must subclass NotificationBase.')

        registry.register(notification_class)

        return notification_class
    return _notification_wrapper
