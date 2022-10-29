import os
from pathlib import Path    # Python 3.6+ only
from pydantic import BaseSettings, Field

BASE_PATH: str = os.getcwd()
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
APP_PATH = "{0}".format(Path(CURRENT_DIR).parent.parent)
ENV_PATH = "{0}/.env".format(APP_PATH)


class AppConfigs(BaseSettings):

    APP_PATH: str = BASE_PATH
    APP_NAME: str = Field('Portfolio', env='APP_NAME')
    APP_ENV: str = Field('', env='APP_ENV')
    APP_KEY: str = Field('', env='APP_KEY')
    APP_DEBUG: bool = Field(True, env='APP_DEBUG')
    APP_URL: str = Field('http://localhost:8000', env='APP_URL')

    STATICS_DIRECTORY: str = 'standard/static'
    STATICS_ROUTE: str = '/static'
    STATICS_PATH: str = f'{BASE_PATH}/{STATICS_DIRECTORY}'

    DB_CONNECTION: str = Field('sqlite', env='DB_CONNECTION')
    DB_HOST: str = Field('127.0.0.1', env='DB_HOST')
    DB_PORT: str = Field('', env='DB_PORT')
    DB_USER: str = Field('', env='DB_USER')
    DB_PASSWORD: str = Field('', env='DB_PASSWORD')
    DB_DATABASE: str = Field('', env='DB_DATABASE')
    DB_PREFIX: str = Field('', env='DB_PREFIX')

    MAIL_PROVIDER: str = Field('', env='MAIL_PROVIDER')
    MAIL_HOST: str = Field('', env='MAIL_HOST')
    MAIL_PORT: str = Field('', env='MAIL_PORT')
    MAIL_TLS: str = Field(True, env='MAIL_TLS')
    MAIL_USERNAME: str = Field('', env='MAIL_USERNAME')
    MAIL_PASSWORD: str = Field('', env='MAIL_PASSWORD')

    class Config:
        case_sensitive = True
        env_file = ENV_PATH
        env_file_encoding = 'utf-8'


appConfigs = AppConfigs()
print(appConfigs.dict())
