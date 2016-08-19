from django.core import mail
from django.test import TestCase, override_settings
from mock import patch

from herald.base import NotificationBase, EmailNotification, TwilioTextNotification
from herald.models import SentNotification
from .notifications import MyNotification


class BaseNotificationTests(TestCase):
    def test_get_context_data(self):
        with override_settings(DEBUG=True):
            self.assertDictEqual(
                MyNotification().get_context_data(),
                {'hello': 'world', 'base_url': '', 'subject': None}
            )

        self.assertDictEqual(
            MyNotification().get_context_data(),
            {'hello': 'world', 'base_url': 'http://example.com', 'subject': None}
        )

    def test_get_recipients(self):
        self.assertRaises(NotImplementedError, NotificationBase().get_recipients)

    def test_get_extra_data(self):
        self.assertDictEqual(NotificationBase().get_extra_data(), {})

    def test_get_sent_from(self):
        self.assertRaises(NotImplementedError, NotificationBase().get_sent_from)

    def test_get_subject(self):
        self.assertIsNone(NotificationBase().get_subject())

    def test_get_demo_args(self):
        self.assertListEqual(NotificationBase.get_demo_args(), [])

    def test_private_send(self):
        self.assertRaises(NotImplementedError, NotificationBase()._send, [])

    def test_send(self):
        with patch.object(MyNotification, 'resend') as mocked_resend:
            MyNotification().send()
            mocked_resend.assert_called_once()
            obj = mocked_resend.call_args[0][0]
            self.assertEqual(obj.recipients, 'test@test.com')

    def test_real_send(self):
        MyNotification().send()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].to, ['test@test.com'])

    def test_render_no_type(self):
        class DummyNotification(NotificationBase):
            pass

        with self.assertRaises(AssertionError):
            DummyNotification().render('text', {})

    def test_render_invalid_template(self):
        class DummyNotification(NotificationBase):
            render_types = ['text']
            template_name = 'does_not_exist'

        self.assertIsNone(DummyNotification().render('text', {}))

    def test_render_invalid(self):
        class DummyNotification(NotificationBase):
            render_types = ['text']
            template_name = 'hello_world'

        self.assertEqual(DummyNotification().render('text', {}), 'Hello World')

    def test_resend_error(self):
        notification = SentNotification()

        with patch.object(NotificationBase, '_send') as mocked__send:
            mocked__send.side_effect = Exception
            result = NotificationBase.resend(notification)
            self.assertFalse(result)

    def test_resend_error_raise(self):
        notification = SentNotification()

        with patch.object(NotificationBase, '_send') as mocked__send:
            mocked__send.side_effect = Exception
            self.assertRaises(Exception, NotificationBase.resend, notification, raise_exception=True)

    def test_resend(self):
        notification = SentNotification()

        with patch.object(NotificationBase, '_send') as mocked__send:
            result = NotificationBase.resend(notification)
            self.assertTrue(result)


class EmailNotificationTests(TestCase):
    def test_get_recipients(self):
        self.assertListEqual(MyNotification().get_recipients(), ['test@test.com'])

    def test_get_sent_from(self):
        class TestNotification(EmailNotification):
            from_email = 'bob@example.com'

        self.assertEqual(TestNotification().get_sent_from(), 'bob@example.com')

    def test_get_sent_from_default(self):
        class TestNotification(EmailNotification):
            from_email = None

        with override_settings(DEFAULT_FROM_EMAIL='default@example.com'):
            self.assertEqual(TestNotification().get_sent_from(), 'default@example.com')

    def test_get_subject(self):
        class TestNotification(EmailNotification):
            subject = 'test subject'

        self.assertEqual(TestNotification().get_subject(), 'test subject')

    def test_get_extra_data_none(self):
        self.assertDictEqual(EmailNotification().get_extra_data(), {})

    def test_get_extra_data(self):
        class TestNotification(EmailNotification):
            bcc = 'bcc@test.com'
            cc = 'cc@test.com'
            headers = {'HEADER': 'test'}
            reply_to = 'reply_to@test.com'

        self.assertDictEqual(TestNotification().get_extra_data(), {
            'bcc': 'bcc@test.com',
            'cc': 'cc@test.com',
            'headers': {'HEADER': 'test'},
            'reply_to': 'reply_to@test.com',
        })


class TwilioNotificationTests(TestCase):
    def test_get_recipients(self):
        class TestNotification(TwilioTextNotification):
            to_number = '1231231234'

        self.assertListEqual(TestNotification().get_recipients(), ['1231231234'])

    def test_get_sent_from(self):
        class TestNotification(TwilioTextNotification):
            from_number = '1231231234'

        self.assertEqual(TestNotification().get_sent_from(), '1231231234')

    def test_get_sent_from_default(self):
        class TestNotification(TwilioTextNotification):
            from_email = None

        with override_settings(TWILIO_DEFAULT_FROM_NUMBER='1231231234'):
            self.assertEqual(TestNotification().get_sent_from(), '1231231234')

    def test_get_sent_from_default_error(self):
        class TestNotification(TwilioTextNotification):
            from_email = None

        self.assertRaisesMessage(
            Exception,
            'TWILIO_DEFAULT_FROM_NUMBER setting is required for sending a TwilioTextNotification',
            TestNotification().get_sent_from
        )
