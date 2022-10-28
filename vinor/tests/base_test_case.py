import subprocess


class BaseTestCase:

    def call_command(self, cmd: list):
        result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
        return result
