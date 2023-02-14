from dao.favorites import FavoritesDAO
from service.user import UserService


class FavoritesService:
    def __init__(self, dao: FavoritesDAO, user_service: UserService):
        self.dao = dao
        self.user_service = user_service

    def create(self, mid, email):
        user = self.user_service.get_by_email(email)
        data = {"user_id": user.id,
                "movie_id": mid}
        self.dao.create(data)

    def delete(self, mid, email):
        user = self.user_service.get_by_email(email)
        data = {"user_id": user.id,
                "movie_id": mid}
        self.dao.delete(data)
