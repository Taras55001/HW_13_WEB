from pydantic_settings import BaseSettings


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
    cloudinary_name: str
    cloudinary_api_key: str
    cloudinary_api_secret: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

class Config:
    DB_URL = settings.sqlalchemy_database_url


class RedisConfig:
    host = settings.redis_host
    port = settings.redis_port
    db = settings.redis_db


config = Config
redis_config = RedisConfig
