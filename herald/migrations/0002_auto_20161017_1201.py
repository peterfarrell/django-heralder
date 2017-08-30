# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('herald', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notification_class', models.CharField(max_length=80)),
                ('can_disable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('disabled_notifications', models.ManyToManyField(to='herald.Notification')),
            ],
        ),
        migrations.AddField(
            model_name='sentnotification',
            name='user',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='sentnotification',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, b'Pending'), (1, b'Success'), (2, b'Failed'), (3, b'User Disabled')]),
        ),
    ]
