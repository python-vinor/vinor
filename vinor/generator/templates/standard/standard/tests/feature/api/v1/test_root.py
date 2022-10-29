from fastapi.testclient import TestClient
from standard.tests.helper import exclude_middleware
from standard.main import app

client = TestClient(exclude_middleware(app, 'TrustedHostMiddleware'))


def test_read_root():
    response = client.get("/v1/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Standard API V1!"}
