import os
from vinor.mailer.config import MailerConfig
from vinor.mailer.helper import read_env_file

CURRENT_DIR: str = os.getcwd()


class TestMailerConfig:

    def test_mailer_config(self):
        mailerConfigs = MailerConfig()
        assert hasattr(mailerConfigs, 'MAIL_TEMPLATES_DIR')
        assert hasattr(mailerConfigs, 'MAIL_TEMPLATES')
        assert hasattr(mailerConfigs, 'MAIL_PROVIDER')
        assert hasattr(mailerConfigs, 'MAIL_HOST')
        assert hasattr(mailerConfigs, 'MAIL_PORT')
        assert hasattr(mailerConfigs, 'MAIL_TLS')
        assert hasattr(mailerConfigs, 'MAIL_USERNAME')
        assert hasattr(mailerConfigs, 'MAIL_PASSWORD')

    def test_read_mailer_config_from_env_file(self):
        ENV_PATH = f"{CURRENT_DIR}/.env.sample"
        MailerConfig.Config.env_file = ENV_PATH
        mailerConfigs = MailerConfig()
        mailer_config_data = mailerConfigs.dict()

        end_file_path = ENV_PATH
        end_file_data = read_env_file(file_path=end_file_path)

        assert mailer_config_data['MAIL_PROVIDER'] == end_file_data['MAIL_PROVIDER']
        assert mailer_config_data['MAIL_HOST'] == end_file_data['MAIL_HOST']
        assert mailer_config_data['MAIL_PORT'] == end_file_data['MAIL_PORT']
        assert mailer_config_data['MAIL_USERNAME'] == end_file_data['MAIL_USERNAME']
        assert mailer_config_data['MAIL_PASSWORD'] == end_file_data['MAIL_PASSWORD']
        assert mailer_config_data['MAIL_TLS'] == bool(end_file_data['MAIL_TLS'])
