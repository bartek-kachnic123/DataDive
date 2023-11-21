import pytest
from data_dive.users.models import User

@pytest.mark.django_db
class TestUserManager:

    def test_create_user_without_email(self):
        with pytest.raises(ValueError) as exc_info:
            User.objects.create_user(
                name="",
                email="john_doe",
                password="something-r@nd0m!",
            )
        assert str(exc_info.value) == "The given name must be set"

    def test_create_user(self):
        user = User.objects.create_user(
                name="john_doe",
                email="john@email.com",
                password="something-r@nd0m!",
            )
        assert not user.is_staff
        assert not user.is_superuser
        assert user.check_password("something-r@nd0m!")
        assert user.name == "john_doe"
        assert user.email == "john@email.com"
        assert user.username is None

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            name="admin",
            email="admin@example.com",
            password="something-r@nd0m!",
        )
        assert user.email == "admin@example.com"
        assert user.is_staff
        assert user.is_superuser
        assert user.name == "admin"
        assert user.username is None