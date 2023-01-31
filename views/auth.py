from flask import request, abort
from flask_restx import Namespace, Resource
from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get("username", None)
        password = req_json.get("password", None)
        try:

            tokens = auth_service.generate_tokens(username, password)
            return tokens, 201
        except Exception as e:
            abort(401)

    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        try:
            tokens = auth_service.get_new_tokens(refresh_token)
            return tokens, 201

        except Exception as e:
            abort(401)
