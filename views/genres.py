from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from helpers.decorators import auth_required, admin_required
from parsers import page_parser

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        filters = page_parser.parse_args()
        rs = genre_service.get_all(filters)
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        req_json = request.json
        new_genre = genre_service.create(req_json)
        return "", 201



@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = rid
        genre_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, rid):
        genre_service.delete(rid)
        return "", 204
