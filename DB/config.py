from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    #data base info
    database_hostname: str
    database_port: str
    database_name: str
    database_server:str
    database_user:str
    database_password:str



    class Config:
        env_file = ".env"

settings = Settings()