# django-herald

[![Latest PyPI version](https://badge.fury.io/py/django-herald.svg)](https://pypi.python.org/pypi/django-herald)
[![Build Status](https://travis-ci.org/worthwhile/django-herald.svg?branch=master)](https://travis-ci.org/worthwhile/django-herald)
[![Coverage Status](https://coveralls.io/repos/github/worthwhile/django-herald/badge.svg?branch=master)](https://coveralls.io/github/worthwhile/django-herald?branch=master)

[![Logo](https://github.com/worthwhile/django-herald/blob/master/logo.png)](https://github.com/worthwhile/django-herald)

Django library for separating the message content from transmission method

# Installation

1. `pip install django-herald`
2. Add `herald` and `django.contrib.sites` to `INSTALLED_APPS`.
3. Add herald's URLS:

        if settings.DEBUG:
            urlpatterns = [
                url(r'^herald/', include('herald.urls')),
            ] + urlpatterns

# Usage

1. Create a `notifications.py` file in any django app. This is where your notification classes will live. Add a class like this:

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

2. Create templates for rendering the email using this file structure:

        templates/
            herald/
                text/
                    welcome_email.txt
                html/
                    welcome_email.html

3. Test how your email looks by navigating to `/herald/`.

4. Send your email wherever you need in your code:

        WelcomeEmail(user).send()

5. View the sent emails in django admin and even be able to resend it.

## Asynchronous Email Sending

If you are sending slightly different emails to a large number of people, it might take quite a while to process. By default, Django will process this all synchronously. For asynchronous support, we recommend django-celery-email. It is very straightfoward to setup and integrate: https://github.com/pmclanahan/django-celery-email

## Email Attachments

To send attachments, assign a list of tuples to the attachments attribute of your EmailNotification instance. The tuples should consist of the filename, the raw attachment data, and the mimetype.  It is up to you to get the attachment data.  Like this:

    from sorl.thumbnail import get_thumbnail

    email = WelcomeEmail(user)

    im = get_thumbnail(image_file.name, '600x600', quality=95)
    my_image = MIMEImage(im.read())
    my_image.add_header('Content-ID', '<{}>'.format('coupon.jpg'))

    raw_data = get_pdf_data()

    email.attachments = [
        ('Report.pdf', raw_data, 'application/pdf'),
        my_image,
    ]
    email.send()

You may also use email.MIMEBase.MIMEBase instances as your data.  See the documentation for attachments under EmailMessage Objects/attachments in the Django documentation.

If you use MIMEImages, you can refer to them in your email templates using the Content ID (cid) like this:

    <img src="cid:{{image_file.name}}" />

# Running Tests

	python runtests.py
