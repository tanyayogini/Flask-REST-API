from unittest.mock import MagicMock

import pytest
from dao.model.user import User
from dao.user import UserDAO
from service.user import UserService

from setup_db import db

user = User()


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(db.session)
    test_user1 = User(id=1, email='test_email1', password='password1', name='', surname='', favorite_genre='')
    test_user2 = User(id=2, email='test_email2', password='password2', name='', surname='', favorite_genre='')
    user_dao.get_by_email = MagicMock(return_value=test_user1)
    user_dao.get_one = MagicMock(return_value=test_user2)
    user_dao.update_password = MagicMock()
    user_dao.create = MagicMock(return_value=User(id=3))
    user_dao.update = MagicMock()
    user_dao.update_password = MagicMock()

    return user_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_by_email(self):
        user = self.user_service.get_by_email(1)
        assert user is not None
        assert user.id == 1

    def test_get_one(self):
        user = self.user_service.get_one(1)
        assert user is not None
        assert user.id == 2

    def test_create(self):
        new_user = {
            "email": "new_email",
            "password": "password"
        }
        user = self.user_service.create(new_user)
        assert user.id != None
        assert user.id == 3

    def test_update(self):
        update_user = {
            "email": "new_email",
            "password": "password"
        }
        self.user_service.update(update_user)

    def test_get_hash(self):
        password = 'test_password'
        hash = self.user_service.get_hash(password)
        assert hash != None
        assert hash != password

    def test_compare_passwords(self):
        password = 'test_password'
        hash = self.user_service.get_hash(password)
        right_password = self.user_service.compare_passwords(hash, password)
        bad_password = self.user_service.compare_passwords(hash, 'bad_password')
        assert right_password == True
        assert bad_password == False
