from http import HTTPStatus

from fastapi.testclient import TestClient

from app.core.config import settings


def test_read_products(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/items")
    products = response.json()
    assert response.status_code == HTTPStatus.OK
    assert len(products) > 0

