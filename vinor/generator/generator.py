import os

from vinor.helpers import camel_to_snake, copy_and_overwrite

GENERATOR_DIR = os.path.abspath(os.path.dirname(__file__))


class Generator:
    PROJECT_PATH: str
    PROJECT_NAME: str
    PROJECT_TEMPLATE: str

    def __init__(self, project_name: str, path: str, template: str = 'standard'):
        self.PROJECT_NAME = project_name
        self.PROJECT_PATH = path
        self.PROJECT_TEMPLATE = camel_to_snake(template)

    def run(self):
        from_path = f'{GENERATOR_DIR}/templates/{self.PROJECT_TEMPLATE}'
        to_path = f'{self.PROJECT_PATH}/{self.PROJECT_NAME}'
        copy_and_overwrite(from_path=from_path, to_path=to_path)
