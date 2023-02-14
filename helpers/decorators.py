import jwt
from flask import request, abort
from helpers.constants import ALGO, SECRET


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        try:
           user = jwt.decode(token, SECRET, algorithms=[ALGO])
        except Exception as e:
            print(f"JWT Decode Exception: {e}")
            abort(401)

        email = user.get('email')
        return func(email=email, *args, **kwargs)

    return wrapper
