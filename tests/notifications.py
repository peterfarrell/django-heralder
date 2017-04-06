from herald.base import EmailNotification
from herald import registry
from email.mime.image import MIMEImage

class MyNotification(EmailNotification):
    context = {'hello': 'world'}
    template_name = 'hello_world'
    to_emails = ['test@test.com']

    def get_attachments(self):
        fp = open('python.jpeg', 'rb')
        img = MIMEImage(fp.read())
        img.add_header('Content-ID', '<{}>'.format('python.jpg'))

        raw_data = 'Some Report Data'

        return [
            ('Report.txt', raw_data, 'text/plain'),
            img,
        ]

registry.register(MyNotification)
