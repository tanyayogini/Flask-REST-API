from flask_restx import Resource, Namespace
from implemented import favorites_service
from helpers.decorators import auth_required

favorites_ns = Namespace('favorites/movies/')

@favorites_ns.route('/<int:mid>')
class FavouritesView(Resource):
    @auth_required
    def post(self, mid, email):
        """Создает новую запись в таблице любимых фильмов: id пользователя и id фильма"""
        favorites_service.create(mid, email)
        return "", 201

    @auth_required
    def delete(self, mid, email):
        """Удаляет запись в таблице любимых фильмов: id пользователя и id фильма"""
        favorites_service.delete(mid, email)
        return "", 204
