from fastapi import FastAPI
from starlette.middleware import Middleware
from standard.services.image_service import ImageService


def exclude_middleware(app: FastAPI, target: str) -> FastAPI:
    new_middlewares: list[Middleware] = []
    for middleware in app.user_middleware:
        if not middleware.cls.__name__ == target:
            new_middlewares.append(middleware)
    app.user_middleware = new_middlewares
    app.middleware_stack = app.build_middleware_stack()
    return app


def objectKeyExist(key, dict_json):
    if key in dict_json:
        return True
    return False


def clean_uploaded_image(real_file_path: str):
    ImageService().clean_resize_images(real_file_path)


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
