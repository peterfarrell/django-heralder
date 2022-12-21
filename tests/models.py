from django.db import models

from herald.models import SentNotificationAbstract


class SentNotificationCompany(SentNotificationAbstract):
    company_name = models.CharField(max_length=32)

    class Meta(SentNotificationAbstract.Meta):
        abstract = False
