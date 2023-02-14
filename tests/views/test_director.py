class TestDirector:

    def test_all_directors_status(self, test_client):
        """ Проверяем при запросе режиссеров нужный статус-код """
        response = test_client.get('/directors/', follow_redirects=True)
        assert response.status_code == 200, "Статус-код запроса режиссеров не ок"

    def test_one_director_status(self, test_client):
        """ Проверяем при запросе одного режиссера нужный статус-код """
        response = test_client.get('/directors/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса режиссера по id не ок"
