import pytest
from fastapi.testclient import TestClient
from starter-code import app

client = TestClient(app)

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2

def test_get_item_success():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Apple"

def test_get_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404

def test_create_item_success():
    new_item = {"id": 3, "name": "Orange", "price": 1.25}
    response = client.post("/items", json=new_item)
    assert response.status_code == 201
    assert response.json()["name"] == "Orange"

def test_create_item_duplicate_id():
    duplicate_item = {"id": 1, "name": "Grape", "price": 2.00}
    response = client.post("/items", json=duplicate_item)
    assert response.status_code == 400
