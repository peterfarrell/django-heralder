from herald import registry
from herald.base import EmailNotification


class MyNotification(EmailNotification):
    context = {'hello': 'world'}
    template_name = 'hello_world'
    to_emails = ['test@test.com']


class MyOtherNotification(EmailNotification):
    context = {'hello': 'world'}
    template_name = 'hello_world'
    to_emails = ['test@test.com']


registry.register(MyNotification)
registry.register(MyOtherNotification)
