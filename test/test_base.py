from unittest import TestCase
from fastapi.testclient import TestClient
from . import create_app,get_mock_db
from pymongo.database import Database

class BaseTest(TestCase):
    def setUp(self):
        self.client:TestClient=create_app()
        self.db:Database=get_mock_db()

    def test_dummy(self):
        res=self.client.get(url='')
        assert res.is_success
        assert res.json()=="hello"