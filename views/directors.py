from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
from parsers import page_parser

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        """Возвращает всех режиссеров, если указано page= возвращает по страницам (12 шт)"""
        filters = page_parser.parse_args()
        rs = director_service.get_all(filters)
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        """Возвращает фильм по id"""
        r = director_service.get_one(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
