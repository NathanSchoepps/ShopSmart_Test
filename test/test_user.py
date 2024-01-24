import pytest
from fastapi.testclient import TestClient
from main import app
from test.conftest import auth_user, create_user

client = TestClient(app)

def test_create_user_success():
    res = client.post("/auth/signup", json={
        "email": "test.user777@gmail.com" , "password": "password777"
    })
    assert res.status_code == 201 

def test_create_user_conflict(create_user):
    res = client.post("/auth/signup", json={
        "email": "test.user777@gmail.com", 'password': "password777"
    })
    assert res.status_code == 409

def test_invalid_user():
    with pytest.raises(ValueError) as e:
        client.post("/auth/signup", json={
            "email": "thisisnotanemailàgmail.com",
            "password": "password"
        })
        assert "Malformed email address string" in str(e.value)

def test_login(create_user):
    response = client.post("auth/login", data={
        "username": "test.user1@gmail.com",
        "password": "password"
    })
    assert response.status_code == 200

def test_invalid_login(create_user):
    response = client.post("auth/login", data={
        "email": "test.user777@gmail.com",
        "password": "password777"
    })
    assert response.status_code == 422

def test_invalid_credentials_login(create_user):
    response = client.post("auth/login", data={
        "username": "test.user777@gmail.com",
        "password": "iforgotmypassword"
    })
    assert response.status_code == 401