from herald.base import EmailNotification
from herald import registry


class MyNotification(EmailNotification):
    context = {'hello': 'world'}
    template_name = 'hello_world'

registry.register(MyNotification)
