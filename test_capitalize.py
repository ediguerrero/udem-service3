import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/roleUsers/Z2Y2X3')
    assert response.status_code == 200