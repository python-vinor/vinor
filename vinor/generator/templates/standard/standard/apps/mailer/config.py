import os

from pydantic import BaseSettings
from .utils import scandir
from standard.configs.app import appConfigs

MAILER_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class MailerConfig(BaseSettings):

    MAILER_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    MAIL_APP_NAME = appConfigs.APP_NAME
    MAIL_PROVIDER_SUPPORTED = ['gmail', 'yandex', 'ses', 'smtp']
    MAIL_PROVIDER = appConfigs.MAIL_PROVIDER
    MAIL_TEMPLATES_DIR = f'{MAILER_ROOT_DIR}/templates'
    MAIL_TEMPLATES = scandir(MAIL_TEMPLATES_DIR)
    MAIL_HOST = appConfigs.MAIL_HOST
    MAIL_PORT = appConfigs.MAIL_PORT
    MAIL_TLS = appConfigs.MAIL_TLS
    MAIL_USERNAME = appConfigs.MAIL_USERNAME
    MAIL_PASSWORD = appConfigs.MAIL_PASSWORD


mailerConfigs = MailerConfig()
