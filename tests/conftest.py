import pytest
import app


@pytest.fixture()
def test_client():
    application = app.app
    return application.test_client()
