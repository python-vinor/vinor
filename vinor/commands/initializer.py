import pkg_resources
from .utils import write_json, read_json

VERSION = pkg_resources.get_distribution('vinor').version


class Initializer:
    FILENAME = 'vinor.config.json'

    def __init__(self, project_root: str):
        self.PROJECT_ROOT = project_root
        self.CONFIG_FILE = f"{project_root}/{self.FILENAME}"

    def write_config(self) -> None:
        write_json(file_path=self.CONFIG_FILE, data=self.config_data())

    def read_config(self) -> dict:
        return read_json(self.CONFIG_FILE)

    def config_data(self) -> dict:
        return {
            "name": "Vinor CLI",
            "version": VERSION,
            "project_root": self.PROJECT_ROOT
        }
