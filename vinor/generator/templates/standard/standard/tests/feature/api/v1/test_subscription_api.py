from pytest_schema import schema, Or
from faker import Faker
from fastapi.testclient import TestClient
from standard.tests.helper import exclude_middleware
from standard.main import app

client = TestClient(exclude_middleware(app, 'TrustedHostMiddleware'))

fake = Faker()


subscription_list_structure = {
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
                "email": Or(None, str),
                "type": Or(None, str),
                "schedule": Or(None, str),
                "is_active": bool,
                "created_at": Or(None, str),
                "updated_at": Or(None, str),
            }
        ]
    }
}

subscription_detail_structure = {
    "message": Or(None, str),
    "data": {
        "id": int,
        "name": str,
        "email": Or(None, str),
        "type": Or(None, str),
        "schedule": Or(None, str),
        "is_active": bool,
        "created_at": Or(None, str),
        "updated_at": Or(None, str),
    }
}


class TestsubscriptionApi:

    def test_read_subscription_list(self):
        response = client.get("/v1/subscriptions")
        data = response.json()
        assert response.status_code == 200
        assert schema(subscription_list_structure) == data

    def test_create_subscription_without_duplicate(self):
        payload = {
            "name": fake.uuid4(),
            "email": fake.uuid4(),
            "type": fake.text(100),
            "schedule": fake.text(100),
            "is_active": True
        }
        response = client.post("/v1/subscriptions/", json=payload)
        response_data = response.json()

        assert response.status_code == 201
        assert response_data['data']['is_active'] == payload['is_active']
        assert response_data['data']['name'] == payload['name']
        assert schema(subscription_detail_structure) == response.json()

    def test_update_subscription(self):
        payload = {
            "name": fake.uuid4(),
            "email": fake.uuid4(),
            "type": fake.text(100),
            "schedule": fake.text(100),
            "is_active": True
        }

        # Create subscription the first times
        response = client.post("/v1/subscriptions/", json=payload)
        created_obj = response.json()['data']

        # Update subscription
        payload['type'] = 'my type'
        response = client.put(f"/v1/subscriptions/{created_obj['id']}", json=payload)
        updated_obj = response.json()['data']

        assert response.status_code == 200
        assert updated_obj['type'] == 'my type'

    def test_delete_subscription(self):
        payload = {
            "name": fake.uuid4(),
            "email": fake.uuid4(),
            "type": fake.text(100),
            "schedule": fake.text(100),
            "is_active": True
        }
        response = client.post("/v1/subscriptions/", json=payload)
        created_obj = response.json()['data']
        print(created_obj)

        # Delete subscription
        response = client.delete(f"/v1/subscriptions/{created_obj['id']}")
        assert response.status_code == 200

        # Get subscription
        response = client.get(f"/v1/subscriptions/{created_obj['id']}")
        assert response.status_code == 404
