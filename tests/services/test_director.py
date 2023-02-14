import pytest
from unittest.mock import MagicMock

from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService

from setup_db import db


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)
    test_director1 = Director(id=1, name='test_director1')
    test_director2 = Director(id=2, name='test_director2')
    test_director3 = Director(id=3, name='test_director3')

    director_dao.get_one = MagicMock(return_value=test_director1)
    director_dao.get_all = MagicMock(return_value=[test_director1, test_director2, test_director3])

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id == 1

    def test_get_all(self):
        directors = self.director_service.get_all(None)
        assert len(directors) > 0
