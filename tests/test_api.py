import pytest
from api.api_client import APIClient

@pytest.mark.api
def test_get_products():
    client = APIClient("https://fakestoreapi.com")

    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_product = data[0]

    assert "title" in first_product
    assert "price" in first_product
    assert isinstance(first_product["price"], (int, float))

@pytest.mark.api
def test_create_product():
    client = APIClient("https://fakestoreapi.com")

    payload = {
        "title" : "Test Product",
        "price" : 100,
        "description": "Test Description",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    }

    response = client.post("/products", payload)

    assert response.status_code == 200 or response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["price"] == payload["price"]