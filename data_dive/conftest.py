import pytest
from .users.models import User
from .users.tests.factories import UserFactory


@pytest.fixture
def user(db) -> User:
    return UserFactory()
