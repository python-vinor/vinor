from standard.configs.app import APP_PATH, AppConfigs
from standard.tests.helper import read_env_file


class TestAppConfigFile:

    def test_read_env_file(self):
        end_file_path = APP_PATH + '/.env'
        end_file_data = read_env_file(end_file_path)

        appConfigs = AppConfigs()
        app_config_data = appConfigs.dict()

        for key, value in app_config_data.items():
            if hasattr(end_file_data, key):
                assert value == end_file_data[key]

    def test_read_env_local_sample_file(self):
        end_file_path = APP_PATH + '/.env.sample'
        end_file_data = read_env_file(end_file_path)

        AppConfigs.Config.env_file = end_file_path
        appConfigs = AppConfigs()
        app_config_data = appConfigs.dict()

        assert app_config_data['APP_ENV'] == 'local'

        for key, value in appConfigs.dict().items():
            if hasattr(end_file_data, key):
                assert value == end_file_data[key]

    def test_read_env_prod_sample_file(self):
        end_file_path = APP_PATH + '/.env.prod.sample'
        end_file_data = read_env_file(end_file_path)

        AppConfigs.Config.env_file = end_file_path
        appConfigs = AppConfigs()
        app_config_data = appConfigs.dict()

        assert app_config_data['APP_ENV'] == 'production'

        for key, value in appConfigs.dict().items():
            if hasattr(end_file_data, key):
                assert value == end_file_data[key]
