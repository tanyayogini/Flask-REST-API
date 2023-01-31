import calendar
import datetime

import jwt
from flask_restx import abort

from helpers.constants import SECRET, ALGO
from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password):
        """Принимает имя пользователя и пароль, проверяет их и
        создает токен доступа на 30 минут и refresh токен на 130 дней"""

        user = self.user_service.get_by_username(username)

        if user is None:
            raise abort(404)

        if not self.user_service.compare_passwords(user.password, password):
            abort(400)

        data = {"username": user.username,
                "role": user.role}

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def get_new_tokens(self, refresh_token):
        """Принимает refresh токен, отдает новую пару access И refresh токен"""

        if refresh_token is None:
            abort(400)

        try:
            data = jwt.decode(jwt=refresh_token, key=SECRET, algorithms=[ALGO])
        except Exception as e:
            abort(400)

        username = data.get("username")

        user = self.user_service.get_by_username(username)

        data = {
            "username": user.username,
            "role": user.role
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)
        return {"access_token": access_token, "refresh_token": refresh_token}
