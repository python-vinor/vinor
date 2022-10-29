import pytest
from standard.services.mail_service import MailService


class TestMailService:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.mailService = MailService()

    def test_send_user_registered(self):
        assert self.mailService.send_user_registered(fullname='Ethan V', email="ethanvu.dev@gmail.com")

    def test_send_newsletter(self):
        assert self.mailService.send_newsletter(fullname='Ethan V', email="ethanvu.dev@gmail.com")

    def test_send_order_created(self):
        assert self.mailService.send_order_created(fullname='Ethan V', email="ethanvu.dev@gmail.com")
