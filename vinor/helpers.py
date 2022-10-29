import os
import re
import json
import shutil


def camel_to_snake(str) -> str:
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def copy_and_overwrite(from_path: str, to_path: str):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)


def read_json(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path: str, data: dict) -> dict:
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=2)
