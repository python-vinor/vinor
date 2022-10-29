import pytest
from pytest_schema import schema, Or
from faker import Faker
from fastapi.testclient import TestClient
from standard.tests.helper import exclude_middleware
from standard.main import app

client = TestClient(exclude_middleware(app, 'TrustedHostMiddleware'))
fake = Faker()

post_list_structure = {
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
                "image": Or(None, str),
                "content": Or(None, str),
                "category_id": int,
                "is_active": bool,
                "created_at": Or(None, str),
                "updated_at": Or(None, str),
            }
        ]
    }
}

post_detail_structure = {
    "message": Or(None, str),
    "data": {
        "id": int,
        "title": str,
        "slug": Or(None, str),
        "image": Or(None, str),
        "content": Or(None, str),
        "category_id": int,
        "is_active": bool,
        "created_at": Or(None, str),
        "updated_at": Or(None, str),
    }
}


class TestPostApi:

    CATEGORY_ID: int = 0

    @pytest.fixture(autouse=True)
    def setup_category_for_post(self):
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
        self.CATEGORY_ID = response_data['data']['id']

    def test_read_post_list(self):
        response = client.get("/v1/posts")
        data = response.json()
        print(data)
        assert response.status_code == 200
        assert schema(post_list_structure) == data

    def test_create_post_without_duplicate(self):
        payload = {
            "title": fake.uuid4(),
            "slug": fake.uuid4(),
            "image": fake.text(100),
            "content": fake.uuid4(),
            "category_id": self.CATEGORY_ID,
            "is_active": True
        }
        response = client.post("/v1/posts", json=payload)
        response_data = response.json()

        assert response.status_code == 201
        assert response_data['data']['is_active'] == payload['is_active']
        assert response_data['data']['title'] == payload['title']
        assert schema(post_detail_structure) == response.json()

    def test_create_post_with_duplicated(self):
        payload = {
            "title": fake.uuid4(),
            "slug": fake.uuid4(),
            "image": fake.text(100),
            "content": fake.text(100),
            "category_id": self.CATEGORY_ID,
            "is_active": True
        }

        # Create record the first times
        response = client.post("/v1/posts", json=payload)

        # Create record the second times
        response = client.post("/v1/posts", json=payload)

        assert response.status_code == 400
        assert response.json() == {"detail": "Title already exists"}

    def test_update_post(self):
        payload = {
            "title": fake.uuid4(),
            "slug": fake.uuid4(),
            "image": fake.text(100),
            "content": fake.text(100),
            "category_id": self.CATEGORY_ID,
            "is_active": True
        }

        # Create record the first times
        response = client.post("/v1/posts", json=payload)
        created_obj = response.json()['data']

        # Update record
        payload['content'] = 'my content'
        response = client.put(f"/v1/posts/{created_obj['id']}", json=payload)
        updated_obj = response.json()['data']

        assert response.status_code == 200
        assert updated_obj['content'] == 'my content'

    def test_delete_post(self):
        payload = {
            "title": fake.uuid4(),
            "slug": fake.uuid4(),
            "image": fake.text(100),
            "content": fake.text(100),
            "category_id": self.CATEGORY_ID,
            "is_active": True
        }
        response = client.post("/v1/posts", json=payload)
        created_obj = response.json()['data']

        # Delete record
        response = client.delete(f"/v1/posts/{created_obj['id']}")
        assert response.status_code == 200

        # Get record
        response = client.get(f"/v1/posts/{created_obj['id']}")
        assert response.status_code == 404
