from pytest_schema import schema, Or
from faker import Faker
from fastapi.testclient import TestClient
from standard.tests.helper import exclude_middleware
from standard.main import app

client = TestClient(exclude_middleware(app, 'TrustedHostMiddleware'))

fake = Faker()


setting_list_structure = {
    "message": Or(None, str),
    "data": {
        "total": int,
        "limit": int,
        "skip": int,
        "total_page": int,
        "next_page_link": Or(None, str),
        "items": [
            {
                "id": int,
                "name": str,
                "key": Or(None, str),
                "value": Or(None, str),
                "created_at": Or(None, str),
                "updated_at": Or(None, str),
            }
        ]
    }
}

setting_detail_structure = {
    "message": Or(None, str),
    "data": {
        "id": int,
        "name": str,
        "key": Or(None, str),
        "value": Or(None, str),
        "created_at": Or(None, str),
        "updated_at": Or(None, str),
    }
}


class TestSettingApi:

    def test_read_setting_list(self):
        response = client.get("/v1/settings")
        data = response.json()
        assert response.status_code == 200
        assert schema(setting_list_structure) == data

    def test_create_setting_without_duplicate(self):
        payload = {
            "name": fake.text(50) + fake.uuid4(),
            "key": fake.text(50),
            "value": fake.text(100),
        }
        response = client.post("/v1/settings", json=payload)
        response_data = response.json()
        assert response.status_code == 201
        assert response_data['data']['value'] == payload['value']
        assert response_data['data']['name'] == payload['name']
        assert schema(setting_detail_structure) == response.json()

    def test_create_setting_with_duplicated(self):
        payload = {
            "name": fake.text(50) + fake.uuid4(),
            "key": fake.text(50),
            "value": fake.text(100),
        }

        # Create setting the first times
        response = client.post("/v1/settings", json=payload)

        # Create setting the second times
        response = client.post("/v1/settings", json=payload)

        assert response.status_code == 400

    def test_update_setting(self):
        payload = {
            "name": fake.text(50) + fake.uuid4(),
            "key": fake.text(50),
            "value": fake.text(100),
        }

        # Create setting the first times
        response = client.post("/v1/settings", json=payload)
        created_obj = response.json()['data']

        # Update setting
        payload['value'] = 'my value'
        response = client.put(f"/v1/settings/{created_obj['id']}", json=payload)
        updated_obj = response.json()['data']

        assert response.status_code == 200
        assert updated_obj['value'] == 'my value'

    def test_delete_setting(self):
        payload = {
            "name": fake.text(50) + fake.uuid4(),
            "key": fake.text(50),
            "value": fake.text(100),
        }
        response = client.post("/v1/settings", json=payload)
        created_obj = response.json()['data']

        # Delete setting
        response = client.delete(f"/v1/settings/{created_obj['id']}")
        assert response.status_code == 200

        # Get setting
        response = client.get(f"/v1/settings/{created_obj['id']}")
        assert response.status_code == 404
