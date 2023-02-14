from dao.model.favorites import Favorites


class FavoritesDAO:
    def __init__(self, session):
        self.session = session

    def create(self, data):
        new_favorites = Favorites(**data)
        self.session.add(new_favorites)
        self.session.commit()

    def delete(self, data):
        delete_favorite = self.session.query(Favorites).\
            filter(Favorites.user_id == data.get('user_id'), Favorites.movie_id == data.get('movie_id')).\
            first()
        self.session.delete(delete_favorite)
        self.session.commit()
