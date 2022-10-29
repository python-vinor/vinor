import os

from pydantic import BaseSettings, Field
from vinor.mailer.utils import scandir

MAILER_ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))


class MailerConfig(BaseSettings):

    MAILER_ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))
    MAIL_PROVIDER_SUPPORTED: list = ['smtp']
    MAIL_PROVIDER: str = Field('', env='MAIL_PROVIDER')
    MAIL_TEMPLATES_DIR: str = f'{MAILER_ROOT_DIR}/templates'
    MAIL_TEMPLATES = scandir(MAIL_TEMPLATES_DIR)
    MAIL_APP_NAME: str = Field('Vinor', env='APP_NAME')
    MAIL_HOST: str = Field('', env='MAIL_HOST')
    MAIL_PORT: str = Field('', env='MAIL_PORT')
    MAIL_TLS: bool = Field(True, env='MAIL_TLS')
    MAIL_USERNAME: str = Field('', env='MAIL_USERNAME')
    MAIL_PASSWORD: str = Field('', env='MAIL_PASSWORD')
