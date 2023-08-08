import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

# URL = os.getenv('SQLALCHEMY_DATABASE_URL')
# NAME = os.getenv('POSTGRES_DB')
# USER = os.getenv('POSTGRES_USER')
# PASSWORD = os.getenv('POSTGRES_PASSWORD')
# HOST = 'localhost'
# PORT = os.getenv('POSTGRES_PORT')
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379
# REDIS_DB = 0



class Settings(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: int
    postgres_port: int
    sqlalchemy_database_url: str
    secret_key: str
    algorithm: str
    mail_username: str
    mail_password: str
    mail_from: str
    mail_from_name: str
    mail_port: int
    mail_server: str
    redis_host: str
    redis_port: int
    redis_db: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

class Config:
    DB_URL = settings.sqlalchemy_database_url#f'postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'


class RedisConfig:
    host = settings.redis_host
    port = settings.redis_port
    db = settings.redis_db


config = Config
redis_config = RedisConfig
