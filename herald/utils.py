from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


def get_sent_notification_model():
    sent_notification = getattr(
        settings, "HERALD_SENT_NOTIFICATION_MODEL", "herald.SentNotification"
    )
    try:
        return django_apps.get_model(sent_notification)
    except ValueError:
        raise ImproperlyConfigured(
            "SENT_NOTIFICATION_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            f"SENT_NOTIFICATION_MODEL refers to model '{sent_notification}' that has not been installed"
        )
