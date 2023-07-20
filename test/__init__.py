import mongomock
from pymongo import MongoClient
from fastapi.testclient import TestClient
from APP.main import app as application
from DB.client import get_database
from functools import lru_cache

class MockMongo:
    def __init__(self) -> None:
        self.client=mongomock.MongoClient(uuidRepresentation="standard")
        self.collections={
            key:self.client["test"].get_collection(key) for key in ["Users","Records","Accounts"]
        }

    def __getitem__(self,key):
        return self.collections[key]
    
    def get_collection(self,key,*args,**kwargs):
        return self.collections[key]
    
    def my_reset(self):
        for key,col in self.collections.items():
            col.drop()



@lru_cache
def get_mock_db():
    #return mongomock.MongoClient(**{"port":27017,"uuidRepresentation":UuidRepresentation.STANDARD})["test"]
    return MockMongo()

def create_app()->TestClient:
    #mongomock_client=mongomock.MongoClient()
    #application.dependency_overrides[get_db]=lambda:mongomock_client

    application.dependency_overrides[get_database]=get_mock_db
    #reset db
    get_mock_db().my_reset()
    return TestClient(app=application)