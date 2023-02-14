from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self, filters):
        page = filters.get('page')
        genres = self.session.query(Genre)
        return genres.paginate(page=page, per_page=12).items
