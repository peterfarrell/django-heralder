# django-heralder

[![Latest PyPI version](https://badge.fury.io/py/django-heralder.svg)](https://pypi.python.org/pypi/django-heralder)
[![Tests](https://github.com/peterfarrell/django-heralder/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/peterfarrell/django-heralder/actions/workflows/ci.yml)
[![Black](https://github.com/peterfarrell/django-herald/actions/workflows/black.yml/badge.svg)](https://github.com/peterfarrell/django-heralder/actions/workflows/black.yml)
[![codecov](https://codecov.io/gh/peterfarrell/django-heralder/branch/main/graph/badge.svg?token=PZKJH2G5IN)](https://codecov.io/gh/peterfarrell/django-heralder)

[![Logo](https://github.com/peterfarrell/django-heralder/raw/main/logo.png)](https://github.com/peterfarrell/django-heralder)

A Django messaging library that features:

- Class-based declaration and registry approach, like Django Admin
- Supports multiple transmission methods (Email, SMS, Slack, etc) per message
- Browser-based previewing of messages
- Maintains a history of messaging sending attempts and can view these messages
- Disabling notifications per user
- Auto conversion of HTML emails to text versions

## History

Django-Heralder is a fork of the legacy [Django-Herald](https://github.com/worthwhile/django-herald).

The `v0.3.0` release of Django-Herald has the same features and is equal to Django-Heralder `v0.3.0`.

As of Django-Heralder `v0.4.0`, Django-Heralder has diverged from original project with new features and bug fixes.

## Installation

### Supported Django / Python Versions

We try to make Heralder support all versions of django that django supports + all versions in between. 

For python, Heralder supports all versions of python that the above versions of django support.

As of Heralder v0.4.0, we support:

| Django | Python `3.9` | Python `3.10` | Python `3.11` | Python `3.12` | Python `3.13` |
| --- | --- | --- | --- | --- | --- |
| `3.2.x` | **Y** | **Y** | - | - | - |
| `4.2.x` | **Y** | **Y** | **Y** | **Y** | - |
| `5.2.x` | - | **Y** | **Y** | **Y** | **Y** |

### Installation

1. Install Django-Heralder using your favority packagement management tool (e.g. `pip`, `uv`, etc.)

    ```bash
    pip install django-heralder
    ```

2. In your `settings.py` file, add `herald` and `django.contrib.sites` to `INSTALLED_APPS`:

    ```python
    # ... other settings ...

    INSTALLED_APPS = [
        # ... other apps ...
        'herald',
        'django.contrib.sites',
    ]   
    ```

3. In your main project `urls.py` file, add Heralder's URL routes:

    ```python
    from django.conf import settings
    from django.conf.urls import url, include

    urlpatterns = []

    if settings.DEBUG:
        urlpatterns = [
            url(r'^herald/', include('herald.urls')),
    ] + urlpatterns
    ```

## Example Usage

1. Create a `notifications.py` file in any django app. This is where your notification classes will live. Add a class like this:

    ```python
    from herald import registry
    from herald.base import EmailNotification


    class WelcomeEmail(EmailNotification):  # extend from EmailNotification for emails
        template_name = 'welcome_email'  # name of template, without extension
        subject = 'Welcome'  # subject of email

        def __init__(self, user):  # optionally customize the initialization
            self.context = {'user': user}  # set context for the template rendering
            self.to_emails = [user.email]  # set list of emails to send to

        @staticmethod
        def get_demo_args():  # define a static method to return list of args needed to initialize class for testing
            from users.models import User
            return [User.objects.order_by('?')[0]]

    registry.register(WelcomeEmail)  # finally, register your notification class

    # Alternatively, a class decorator can be used to register the notification:

    @registry.register_decorator()
    class WelcomeEmail(EmailNotification):
        # ... more code ...
    ```

2. Create templates for rendering the email using this file structure:

    ```text
    templates/
        herald/
            text/
                welcome_email.txt
            html/
                welcome_email.html
    ```

3. Test how your email looks by navigating to `/herald/`.

4. Additionally, preview your email before you send:

    ```python
    WelcomeEmail().preview(render_type="html")
    ```

5. Send your email wherever you need in your code:

    ```python
    WelcomeEmail(user).send()
    ```

6. View the sent emails in django admin and even be able to resend it.

## Setting template names

There's three different ways to specify `templatename`:

1. A string without any slash, e.g. `"welcome_email"` and Herald will expect your file structure to be:

    ```text
    templates/
        herald/
            text/
                welcome_email.txt
            html/
                welcome_email.html
    ```

2. A string with slashes, e.g. `"path/to/welcome_email"` and Herald will expect your file structure to be:

    ```text
    templates/
        path/
            to/
                welcome_email.txt
                welcome_email.html
    ```

3. A dictionary with `text` and/or `html` keys with the path to the templates:

    ```python
    {
        "text": "path/to/welcome_email_t.txt",
        "html": "path/to/welcome_email_h.html",
    }
    ```

    and Herald will expect your file structure to be:

    ```text
    templates/
        path/
            to/
                welcome_email_t.txt
                welcome_email_h.html
    ```

## Email options

The following options can be set on the email notification class. For Example:

```python
class WelcomeEmail(EmailNotification):
    cc = ['test@example.com']
```

- `from_email`: (`str`, default: `settings.DEFAULT_FROM_EMAIL`) email address of sender
- `subject`: (`str`, default: ) email subject
- `to_emails`: (`List[str]`, default: `None`) list of email strings to send to
- `bcc`: (`List[str]`, default: `None`) list of email strings to send as bcc
- `cc`: (`List[str]`, default: `None`) list of email strings to send as cc
- `headers`: (`dict`, default: `None`) extra headers to be passed along to the `EmailMultiAlternatives` object
- `reply_to`: (`List[str]`, default: `None`) list of email strings to send as the Reply-To emails
- `attachments`: (`list`) list of attachments. See "Email Attachments" below for more info

## Automatically Deleting Old Notifications

Herald can automatically delete old notifications whenever a new notification is sent.

To enable this, set the `HERALD_NOTIFICATION_RETENTION_TIME` setting to a timedelta instance.

For example:

```python
HERALD_NOTIFICATION_RETENTION_TIME = timedelta(weeks=8)
```

Will delete all notifications older than 8 weeks every time a new notification is sent.

## Manually Deleting Old Notifications

The `delnotifs` command is useful for purging the notification history.

The default usage will delete everything from sent during today:

```bash
python manage.py delnotifs
```

However, you can also pass arguments for `start` or `end` dates. `end` is up to, but not including that date.
- if only `end` is specified, delete anything sent before the end date.
- if only `start` is specified, delete anything sent since the start date.
- if both `start` and `end` are specified, delete anything sent in between, not including the end date.

```bash
python manage.py delnotifs --start='2016-01-01' --end='2016-01-10'
```

## Asynchronous Email Sending

If you are sending slightly different emails to a large number of people, it might take quite a while to process. By default, Django will process this all synchronously. For asynchronous support, we recommend django-celery-email. It is very straightfoward to setup and integrate: https://github.com/pmclanahan/django-celery-email

## Custom SentNotification Model

To create a custom `SentNotification` model, inherit `SentNotificationAbstract`. From there you can add fields and methods as desired. To use this model through Heralder, set `HERALD_SENT_NOTIFICATION_MODEL` in your `settings.py` to the `app.ModelName` path. Then use `get_sent_notification_model` in `herald.utils` to retrieve the model.

Note that using a custom model should be implemented as early as possible, ideally at the beginning of the project. Otherwise data may be split between the default table and the newly created custom table. To mitigate this, data will have to either be dropped or migrated to the new table. 

Example:

```python
from herald.models import SentNotificationAbstract

class SentNotificationCompany(SentNotificationAbstract):
   company_name = models.CharField(max_length=32)
   
   class Meta(SentNotificationAbstract.Meta):
      abstract = False
```

In `settings.py`:

```python
HERALD_SENT_NOTIFICATION_MODEL = "mpapp.SentNotificationCompany"
```

Using throughout your app:

```python
from herald.utils import get_sent_notification_model

SentNotification = get_sent_notification_model()
```

## herald.contrib.auth

Django has built-in support for sending password reset emails. If you would like to send those emails using herald, you can use the notification class in herald.contrib.auth.

First, add `herald.contrib.auth` to `INSTALLED_APPS` (in addition to `herald`).

Second, use the `HeraldPasswordResetForm` in place of django's built in `PasswordResetForm`. This step is entirely dependant on your project structure, but it essentially just involves changing the form class on the password reset view in some way:

```python
# you may simply just need to override the password reset url like so:
url(r'^password_reset/$', password_reset, name='password_reset', {'password_reset_form': HeraldPasswordResetForm}),

# of if you are using something like django-authtools:
url(r'^password_reset/$', PasswordResetView.as_view(form_class=HeraldPasswordResetForm), name='password_reset'),

# or you may have a customized version of the password reset view:
class MyPasswordResetView(FormView):
    form_class = HeraldPasswordResetForm  # change the form class here

# or, you may have a custom password reset form already. In that case, you will want to extend from the HeraldPasswordResetForm:
class MyPasswordResetForm(HeraldPasswordResetForm):
    ...

# alternatively, you could even just send the notification wherever you wish, seperate from the form:
PasswordResetEmail(some_user).send()
```

Third, you may want to customize the templates for the email. By default, herald will use the `registration/password_reset_email.html` that is provided by django for both the html and text versions of the email. But you can simply override `herald/html/password_reset.html` and/or `herald/text/password_reset.txt` to suit your needs.

## User Disabled Notifications

If you want to disable certain notifications per user, add a record to the UserNotification table and
add notifications to the disabled_notifications many to many table.

For example:

```python
user = User.objects.get(id=user.id)

notification = Notification.objects.get(notification_class=MyNotification.get_class_path())

# disable the notification
user.usernotification.disabled_notifications.add(notification)
```

By default, notifications can be disabled.  You can put can_disable = False in your notification class and the system will populate the database with this default.  Your Notification class can also override the verbose_name by setting it in your inherited Notification class.  Like this:

```python
class MyNotification(EmailNotification):
    can_disable = False
    verbose_name = "My Required Notification"
```

## Email Attachments

To send attachments, assign a list of attachments to the attachments attribute of your EmailNotification instance, or override the get_attachments() method.

Each attachment in the list can be one of the following:

1. A tuple which consists of the filename, the raw attachment data, and the mimetype. It is up to you to get the attachment data. Like this:

    ```python
    raw_data = get_pdf_data()

    email.attachments = [
        ('Report.pdf', raw_data, 'application/pdf'),
        ('report.txt', 'text version of report', 'text/plain')
    ]
    email.send()
    ```

2. A MIMEBase object. See the documentation for attachments under EmailMessage Objects/attachments in the Django documentation.

3. A django `File` object.

### Inline Attachments

Sometimes you want to embed an image directly into the email content.  Do that by using a MIMEImage assigning a content id header to a MIMEImage, like this:

```python
email = WelcomeEmail(user)
im = get_thumbnail(image_file.name, '600x600', quality=95)
my_image = MIMEImage(im.read()) # MIMEImage inherits from MIMEBase
my_image.add_header('Content-ID', '<{}>'.format(image_file.name))
```

You can refer to these images in your html email templates using the Content ID (cid) like this:

```html
<img src="cid:{{image_file.name}}" />
```

You would of course need to add the "image_file" to your template context in the example above.  You can also accomplish this using file operations.  In this example we overrode the get_attachments method of an EmailNotification.

```python
class MyNotification(EmailNotification):
    context = {'hello': 'world'}
    template_name = 'welcome_email'
    to_emails = ['somebody@example.com']
    subject = "My email test"
        
    def get_attachments(self):
        fp = open('python.jpeg', 'rb')
        img = MIMEImage(fp.read())
        img.add_header('Content-ID', '<{}>'.format('python.jpeg'))
        return [
            img,
        ]
```

And in your template you would refer to it like this, and you would not need to add anything to the context:

```html
<img src="cid:python.jpeg" />
```

### Missing Templates

By default, Heralder will raise an exception if a template is missing when true (default).

```python
HERALD_RAISE_MISSING_TEMPLATES = True
```

If you do not want this behavior, set this setting to False.

```python
HERALD_RAISE_MISSING_TEMPLATES = False
```

### HTML2Text Support

Django Herald can auto convert your HTML emails to plain text when installed with `hmtl2text` optional package.  Any email without a plain text version will be auto converted if you enable this feature.

1. Install Heralder with `html2text` support:

    ```bash
    pip install django-heralder[html2text]
    ```

2. Follow the regular installation instructions.

3.  In your `settings.py` file, add this configuration setting to enable the `html2text` feature:

    ```python
    HERALD_HTML2TEXT_ENABLED = True
    ```

4. You can customize the output of HTML2Text by setting a configuration dictionary. See [HTML2Text Configuration](https://github.com/Alir3z4/html2text/blob/master/docs/usage.md) for options:

    ```python
    HERALD_HTML2TEXT_CONFIG = {
        # Key / value configuration of html2text 
        'ignore_images': True  # Ignores images in conversion
    }
    ```

### Twilio

Heralder supports Twilio as a notification provider when the optional package is installed.

1. Install Heralder with `twilio` support:

    ```bash
    pip install django-heralder[twilio]
    ```

2. Follow the regular installation instructions.

3. In your `settings.py` file, set your Twilio account SID, token, and default "from number". You can retrieve these values on [Twilio Console](https://twilio.com/console).  Security best practices recommend to NOT hard coding your SID or token in your source code. The example below:

    ```python
    # Twilio configurations
    # values taken from `twilio console`
    TWILIO_ACCOUNT_SID = "your_account_sid"
    TWILIO_AUTH_TOKEN = "your_auth_token"
    TWILIO_DEFAULT_FROM_NUMBER = "+1234567890"
    ```

For reference, Twilio has some great tutorials for Python: [Twilio Python Tutorial](https://www.twilio.com/docs/sms/quickstart/python)

### Other MIME attachments

You can also attach any MIMEBase objects as regular attachments, but you must add a content-disposition header, or they will be inaccessible:  

```python
my_image.add_header('Content-Disposition', 'attachment; filename="python.jpg"')
```

Attachments can cause your database to become quite large, so you should be sure to run the management commands to purge the database of old messages.