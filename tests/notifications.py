from herald.base import EmailNotification, TwilioTextNotification
from herald import registry


class MyNotification(EmailNotification):
    context = {'hello': 'world'}
    template_name = 'hello_world'
    to_emails = ['test@test.com']


registry.register(MyNotification)

class MyOtherNotification(EmailNotification):
    context = {'hello': 'world'}
    template_name = 'hello_world'
    to_emails = ['test@test.com']

registry.register(MyOtherNotification)


class MyTwilioNotification(TwilioTextNotification):
    context = {'hello': 'world'}
    template_name = 'hello_world'
    to_emails = ['test@test.com']

registry.register(MyTwilioNotification)
