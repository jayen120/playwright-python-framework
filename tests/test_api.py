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