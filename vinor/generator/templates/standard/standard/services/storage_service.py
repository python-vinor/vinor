from os import path
from uuid import uuid4
from fastapi import UploadFile
from standard.configs.app import appConfigs


class StorageService:

    @staticmethod
    async def put(file: UploadFile, directory: str = None):
        directory = directory + '/' if directory is not None else ''
        file_name = str(uuid4())
        _, file_extension = path.splitext(file.filename)
        file_path = f'{appConfigs.STATICS_PATH}/{directory}{file_name}{file_extension}'
        file_url = f'{appConfigs.STATICS_ROUTE}/{directory}{file_name}{file_extension}'
        file_mimetype = file.content_type
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
            f.close()
        return file_path, file_url, file_name, file_extension.replace('.', ''), file_mimetype

    @staticmethod
    async def url(file_path: str):
        if path.exists(file_path):
            return f'{appConfigs.STATICS_ROUTE}/{path.basename(file_path)}'
        return None
