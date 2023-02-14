from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self, filters):
        page = filters.get('page')
        status = filters.get('status')
        movies = self.session.query(Movie)
        if status == 'new':
            movies = movies.order_by(Movie.year.desc())
        return movies.paginate(page=page, per_page=12).items
