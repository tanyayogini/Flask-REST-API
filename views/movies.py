from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service
from parsers import page_parser

from helpers.decorators import auth_required, admin_required
movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        filters = page_parser.parse_args()
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200

    @admin_required
    def post(self):
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        b = movie_service.get_one(mid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    @admin_required
    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, bid):
        movie_service.delete(bid)
        return "", 204
