from django.conf import settings


SENT_NOTIFICATION_MODEL = getattr(settings, 'HERALD_SENT_NOTIFICATION_MODEL', 'herald.SentNotification')
