"""
Mailer Helper functions
"""


def read_env_file(file_path: str, debug: bool = False) -> dict:
    env_file = open(file_path, 'r')
    lines = env_file.readlines()
    env_dict = {}
    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        # Ignore comment line and empty line
        if line.startswith('#') or line.strip() == '':
            continue
        else:
            line_cleaned = line.strip().replace("\n", '')
            name, value = line_cleaned.split('=')
            env_dict[name] = value
            if debug:
                print("Line{}: {}".format(count, line_cleaned))
                print("Variable name: {}, value: {}".format(name, value))
    return env_dict
