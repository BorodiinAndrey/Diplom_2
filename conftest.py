import pytest
from helper.helper_user import create_fake_name, create_fake_email, create_fake_password
from methods.create_user import CreateUser


@pytest.fixture
def create_user():
    payload = {
        "email": create_fake_email(),
        "password": create_fake_password(),
        "name": create_fake_name()
    }
    status_code, response_body, token = CreateUser.post_create_user(payload=payload)
    yield {
        "status_code": status_code,
        "response_body": response_body,
        "token": token,
        "payload": payload
    }
    CreateUser.delete_create_user(token)

