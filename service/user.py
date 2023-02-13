import base64
import hashlib
import hmac

from dao.user import UserDAO
from helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.update(data)

    def delete(self, uid):
        return self.dao.delete(uid)

    def get_hash(self, password):
        """Принимает пароль, отдает хэш"""
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, password):
        """Принимает хешированный пароль и введенный пароль, создает хеш введенного пароля,
        сравнивает их, возвращает True/False"""
        new_hash = base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))
        return hmac.compare_digest(password_hash, new_hash)
