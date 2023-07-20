from pymongo import MongoClient
from DB.config import settings
from pymongo.database import Database
from typing import Dict,Union

def get_db_config()->Dict[str,Union[str,int]]:
    return {"host":settings.database_hostname,"port":int(settings.database_port),"username": settings.database_user,"password": settings.database_password,
            "uuidRepresentation":"standard"}


def get_database()->Database:
    config = get_db_config()
    client = MongoClient(**config)
    #client:MongoClient = MongoClient(f"{settings.database_server}://{settings.database_hostname}:{settings.database_port}/")
    return client[settings.database_name]