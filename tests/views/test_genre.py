class TestGenre:

    def test_all_genres_status(self, test_client):
        """ Проверяем при запросе жанров нужный статус-код """
        response = test_client.get('/genres/', follow_redirects=True)
        assert response.status_code == 200, "Статус-код запроса жанров не ок"

    def test_one_genre_status(self, test_client):
        """ Проверяем при запросе одного жанра нужный статус-код """
        response = test_client.get('/genres/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса жанра по id не ок"
