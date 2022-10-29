from os import path
from pytest_schema import schema, Or
from faker import Faker
from fastapi.testclient import TestClient
from standard.configs.app import appConfigs
from standard.tests.helper import exclude_middleware, clean_uploaded_image
from standard.main import app

client = TestClient(exclude_middleware(app, 'TrustedHostMiddleware'))

fake = Faker()


file_list_structure = {
    "message": Or(None, str),
    "data": {
        "total": int,
        "limit": int,
        "skip": int,
        "total_page": int,
        "next_page_link": Or(None, str),
        "items": [
            {
                "id": str,
                "name": Or(None, str),
                "mimetype": Or(None, str),
                "path": Or(None, str),
                "url": Or(None, str),
                "extension": Or(None, str),
                "created_at": Or(None, str),
                "updated_at": Or(None, str),
            }
        ]
    }
}

file_detail_structure = {
    "message": Or(None, str),
    "data": {
        "id": str,
        "name": Or(None, str),
        "mimetype": Or(None, str),
        "path": Or(None, str),
        "url": Or(None, str),
        "extension": Or(None, str),
        "created_at": Or(None, str),
        "updated_at": Or(None, str),
    }
}


class TestFileApi:

    def test_read_file_list(self):
        response = client.get("/v1/files")
        data = response.json()
        print(data)
        assert response.status_code == 200
        assert schema(file_list_structure) == data

    def test_upload_file(self):
        payload = {}
        files = [
            ('file', ('walpaper-1.jpg', open('/home/super/Pictures/Wallpapers/walpaper-1.jpg', 'rb'), 'image/jpeg'))
        ]
        response = client.post("/v1/files/upload/", json=payload, files=files)
        response_data = response.json()

        real_file_path = appConfigs.STATICS_PATH + '/' + response_data['data']['url'].replace('/static/', '')
        is_file_exist = path.exists(real_file_path)

        clean_uploaded_image(real_file_path)

        assert response.status_code == 201
        assert schema(file_detail_structure) == response.json()
        assert is_file_exist is True

    def test_read_file_detail(self):
        # First, upload a file
        demo_file_path = appConfigs.APP_PATH + '/logo.png'
        demo_file_name = path.basename(demo_file_path)
        payload = {}
        files = [
            ('file', (demo_file_name, open(demo_file_path, 'rb'), 'image/jpeg'))
        ]
        response = client.post("/v1/files/upload/", json=payload, files=files)
        response_data = response.json()

        real_file_path = appConfigs.STATICS_PATH + '/' + response_data['data']['url'].replace('/static/', '')
        clean_uploaded_image(real_file_path)

        assert response.status_code == 201
        assert schema(file_detail_structure) == response.json()

    def test_delete_file(self):
        # First, upload a file
        demo_file_path = appConfigs.APP_PATH + '/logo.png'
        demo_file_name = path.basename(demo_file_path)
        payload = {}
        files = [
            ('file', (demo_file_name, open(demo_file_path, 'rb'), 'image/jpeg'))
        ]
        response = client.post("/v1/files/upload/", json=payload, files=files)
        response_data = response.json()
        assert response.status_code == 201

        # Delete file
        response = client.delete(f"/v1/files/{response_data['data']['id']}")
        assert response.status_code == 204
