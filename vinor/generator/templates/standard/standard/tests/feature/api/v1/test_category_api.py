from pytest_schema import schema, Or
from faker import Faker
from fastapi.testclient import TestClient
from standard.tests.helper import exclude_middleware
from standard.main import app

client = TestClient(exclude_middleware(app, 'TrustedHostMiddleware'))

fake = Faker()


category_list_structure = {
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
                "title": str,
                "slug": Or(None, str),
                "icon": Or(None, str),
                "image": Or(None, str),
                "description": Or(None, str),
                "is_active": bool,
                "created_at": Or(None, str),
                "updated_at": Or(None, str),
            }
        ]
    }
}

category_detail_structure = {
    "message": Or(None, str),
    "data": {
        "id": int,
        "title": str,
        "slug": str,
        "icon": Or(None, str),
        "image": Or(None, str),
        "description": Or(None, str),
        "is_active": bool,
        "created_at": Or(None, str),
        "updated_at": Or(None, str),
    }
}


class TestCategoryApi:

    def test_read_category_list(self):
        response = client.get("/v1/categories")
        data = response.json()
        assert response.status_code == 200
        assert schema(category_list_structure) == data

    def test_create_category_without_duplicate(self):
        payload = {
            "title": fake.uuid4(),
            "slug": fake.uuid4(),
            "icon": fake.text(100),
            "image": fake.text(100),
            "description": fake.text(100),
            "is_active": True
        }
        response = client.post("/v1/categories", json=payload)
        response_data = response.json()

        assert response.status_code == 201
        assert response_data['data']['is_active'] == payload['is_active']
        assert response_data['data']['title'] == payload['title']
        assert schema(category_detail_structure) == response.json()

    def test_create_category_with_duplicated(self):
        payload = {
            "title": fake.uuid4(),
            "slug": fake.uuid4(),
            "icon": fake.text(100),
            "image": fake.text(100),
            "description": fake.text(100),
            "is_active": True
        }

        # Create category the first times
        response = client.post("/v1/categories", json=payload)

        # Create category the second times
        response = client.post("/v1/categories", json=payload)

        assert response.status_code == 400
        assert response.json() == {"detail": "Name already exists"}

    def test_update_category(self):
        payload = {
            "title": fake.uuid4(),
            "slug": fake.uuid4(),
            "icon": fake.text(100),
            "image": fake.text(100),
            "description": fake.text(100),
            "is_active": True
        }

        # Create category the first times
        response = client.post("/v1/categories", json=payload)
        created_obj = response.json()['data']

        # Update category
        payload['icon'] = 'my icon'
        response = client.put(f"/v1/categories/{created_obj['id']}", json=payload)
        updated_obj = response.json()['data']

        assert response.status_code == 200
        assert updated_obj['icon'] == 'my icon'

    def test_delete_category(self):
        payload = {
            "title": fake.uuid4(),
            "icon": fake.text(100),
            "description": fake.text(100),
            "is_active": True
        }
        response = client.post("/v1/categories", json=payload)
        created_obj = response.json()['data']

        # Delete category
        response = client.delete(f"/v1/categories/{created_obj['id']}")
        assert response.status_code == 200

        # Get category
        response = client.get(f"/v1/categories/{created_obj['id']}")
        assert response.status_code == 404
