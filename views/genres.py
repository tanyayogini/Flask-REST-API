from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from parsers import page_parser

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        """Возвращает все жанры, если указано page= возвращает по страницам (12 шт)"""
        filters = page_parser.parse_args()
        rs = genre_service.get_all(filters)
        res = GenreSchema(many=True).dump(rs)
        return res, 200

@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        """Возвращает жанр по id"""
        r = genre_service.get_one(gid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200
