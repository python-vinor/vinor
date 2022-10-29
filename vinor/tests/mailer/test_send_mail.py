import os
from vinor.mailer.config import MailerConfig
from vinor.mailer.mailer import Mailer

CURRENT_DIR: str = os.getcwd()
ENV_PATH = f"{CURRENT_DIR}/.env"


class TestSendMail:

    def test_send_demo_smtp_mail(self):
        MailerConfig.Config.env_file = ENV_PATH
        mail_configs = MailerConfig()
        assert Mailer().send_demo_smtp_mail(
            host=mail_configs.MAIL_HOST,
            port=mail_configs.MAIL_PORT,
            username=mail_configs.MAIL_USERNAME,
            password=mail_configs.MAIL_PASSWORD,
            tls=mail_configs.MAIL_TLS,
        ) is True
