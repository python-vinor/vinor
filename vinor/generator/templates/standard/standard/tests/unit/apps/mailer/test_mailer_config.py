from standard.apps.mailer.config import mailerConfigs
from standard.configs.app import APP_PATH
from standard.tests.helper import read_env_file


class TestMailerConfig:

    def test_mailer_config(self):
        assert hasattr(mailerConfigs, 'MAIL_PROVIDER')
        assert hasattr(mailerConfigs, 'MAIL_HOST')
        assert hasattr(mailerConfigs, 'MAIL_PORT')
        assert hasattr(mailerConfigs, 'MAIL_TLS')
        assert hasattr(mailerConfigs, 'MAIL_USERNAME')
        assert hasattr(mailerConfigs, 'MAIL_PASSWORD')
        assert hasattr(mailerConfigs, 'MAIL_TEMPLATES_DIR')
        assert hasattr(mailerConfigs, 'MAIL_TEMPLATES')

    def test_read_mailer_config_from_env_file(self):
        end_file_path = APP_PATH + '/.env'
        end_file_data = read_env_file(end_file_path)
        mailer_config_data = mailerConfigs.dict()

        print(mailer_config_data['MAIL_PROVIDER'])
        # print(end_file_data['MAIL_PROVIDER'])

        assert mailer_config_data['MAIL_PROVIDER'] == end_file_data['MAIL_PROVIDER']
        assert mailer_config_data['MAIL_HOST'] == end_file_data['MAIL_HOST']
        assert mailer_config_data['MAIL_PORT'] == end_file_data['MAIL_PORT']
        assert mailer_config_data['MAIL_TLS'] == end_file_data['MAIL_TLS']
        assert mailer_config_data['MAIL_USERNAME'] == end_file_data['MAIL_USERNAME']
        assert mailer_config_data['MAIL_PASSWORD'] == end_file_data['MAIL_PASSWORD']
