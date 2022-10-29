from standard.apps.mailer.mailer import Mailer


class TestSendMail:

    def test_send_demo_smtp_mail(self):
        assert Mailer().send_demo_smtp_mail() is True
