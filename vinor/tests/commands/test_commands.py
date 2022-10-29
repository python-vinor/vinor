import json
import os
from vinor.commands.initializer import Initializer
from vinor.tests.base_test_case import BaseTestCase


class TestCommonCommands(BaseTestCase):

    def test_command_root(self):
        cmd = ['vinor']
        result = self.call_command(cmd)
        assert result.returncode == 0

    def test_command_init(self):
        cmd = ['vinor', 'init']
        result = self.call_command(cmd)
        assert result.returncode == 0
        assert result.stdout == 'Created configuration file: vinor.config.json\nInitialized as vinor project successfully\n'

    def test_command_init_db(self):
        cmd = ['vinor', 'init-db']
        result = self.call_command(cmd)
        assert result.returncode == 0
        assert result.stdout == 'Initialized the database\n'

    def test_command_drop_db(self):
        cmd = ['vinor', 'drop-db']
        result = self.call_command(cmd)
        assert result.returncode == 0
        assert result.stdout == 'Dropped the database\n'

    def test_command_read_config(self):
        # Prepare: config file
        project_root = os.getcwd()
        initializer = Initializer(project_root=project_root)
        initializer.write_config()

        # Run command: vinor config --show
        cmd = ['vinor', 'config', '--show']
        result = self.call_command(cmd)
        assert result.returncode == 0
        assert json.loads(result.stdout) == initializer.read_config()

    def test_command_new_project(self):
        """
        Create project at current_dir/examples
        """
        project_name = 'academia'
        project_path = f'{os.getcwd()}/examples'

        # Run command: vinor new academia
        cmd = ['vinor', 'new', project_name, '--path', project_path]
        result = self.call_command(cmd)
        assert result.returncode == 0
        assert result.stdout == f'Create project {project_name} successfully.\n'
