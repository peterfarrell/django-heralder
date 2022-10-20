## TBD (TBD)


## 0.3.0 (10-18-2022)
- Added support for automatic HTML2text support for plain text emails
- Added auto-complete for user in admin
- #74 - Added support for conditional enable/disable to raise error for missing templates `HERALD_RAISE_MISSING_TEMPLATES`
- Updated to use GitHub Actions for CI
- Switched to Black for code formatting
- #4 - Added support for BCC-only (no TO) emails.


## 0.2.1 (06-23-2019)
- Fix bug that could occur sometimes in herald.contrib.auth when reversing the password reset url
- Add feature to automatically delete old notifications after configured period of time
- Don't set base_url to empty string when DEBUG==True
- Fix for attaching files to a notification that may be closed before the notification is sent
- Text view for viewing notification now uses the text/plain content type, and the default charset setting


## 0.2 (08-16-2018)
- Drop official support for django < 1.11 and python 3.2-3.3
- Changed Notification.notification_class and Notification.verbose_name fields to have less restrictive `max_length`
- Added support for django 2.1
- Added support for python 3.7


## 0.1.9 (10-09-2017)
- Changed SentNotification.error_message to a TextField to fix issues when message is longer than 255 characters


## 0.1.8 (09-05-2017)
- Fix for migration bug introduced in 0.1.7


## 0.1.7 (08-31-2017)
- User disabled notifications support


## 0.1.6 (06-30-2017)
- Email attachments support


## 0.1.5 (02-10-2017)
- Added decorator to register notifications
- Fixed issue where an extra migration would get created in django 1.10
- Initial support for django 1.11


## 0.1.4 (01-06-2017)
- Fixed an issue where sending TwilioTextNotifications would fail with an assertion error.


## 0.1.3 (12-22-2016)
- Added a management command to delete old saved notifications
- Fixed an issue when installing herald without django already being installed
- Added django.contrib.auth for sending django's password reset email through herald
- Improved the herald email preview list


## 0.1.2 (07-22-2016)
- Fixed bug finding template for front-end email viewer page.


## 0.1.1 (07-22-2016)
- Fixed bug in initial pypi upload


## 0.1 (07-19-2016)
- Initial release
