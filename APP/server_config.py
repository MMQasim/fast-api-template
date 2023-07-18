from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    system_ip_fast:str
    system_port_fast:int
    class Config:
        env_file = ".env"
        
settings = Settings()

# "postgresql://"+settings.database_name+":"+settings.database_password+"@"+settings.database_hostname+":"+settings.database_port+"/"+settings.database_name