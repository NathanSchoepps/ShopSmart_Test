import pytest
from fastapi.testclient import TestClient
from main import app
from test.conftest import auth_user

client = TestClient(app)

def test_get_lists(auth_user):
    res = client.get("/lists",headers={
        "Authorization": f"Bearer {auth_user['access_token']}",
        }
    )
    assert res.status_code == 200

def test_post_lists(auth_user):
    res = client.post("/lists", headers={
        "Authorization": f"Bearer {auth_user['access_token']}",
    }, json={
        "category": "Legume",
        "items": [
            {
                "name": "1Legume",
                "quantity": 2
            }
        ]
    })
    assert res.status_code == 200

def test_get_lists_category(auth_user):
    res = client.get("/lists/{category}",headers={
        "Authorization": f"Bearer {auth_user['access_token']}",
        }
    )
    assert res.status_code == 200

def test_post_lists_category(auth_user):
    res = client.post("/lists/{category}", headers={
        "Authorization": f"Bearer {auth_user['access_token']}",
    }, json={
        "name": "Boeuf",
        "quantity": 5
    })
    assert res.status_code == 200

def test_patch_lists_category(auth_user):
    res = client.patch("/lists/{category}", headers={
        "Authorization": f"Bearer {auth_user['access_token']}",
    })
    assert res.status_code == 200

def test_delete_lists_category(auth_user):
    res = client.delete("/lists/{category}", headers={
        "Authorization": f"Bearer {auth_user['access_token']}",
    })
    assert res.status_code == 200

def test_patch_lists_category_items(auth_user):
    res = client.patch("/lists/{category}/items/{item_name}", headers={
        "Authorization": f"Bearer {auth_user['access_token']}",
    })
    assert res.status_code == 200

def test_delete_lists_category_items(auth_user):
    res = client.delete("/lists/{category}/items/{item_name}", headers={
        "Authorization": f"Bearer {auth_user['access_token']}",
    })
    assert res.status_code == 200






