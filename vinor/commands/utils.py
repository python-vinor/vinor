import re
import json


def camel_to_snake(str) -> str:
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def read_json(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path: str, data: dict) -> dict:
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=2)
