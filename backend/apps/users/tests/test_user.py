import pytest
from django.contrib.auth import get_user_model


@pytest.fixture()
def user_data():
    return {
        "username": "Robert",
        "password": "robert123",
    }


def test_user_data(user_data):
    User = get_user_model()
    user = User(**user_data)
    assert user.username == "Robert"
