import configparser
import pathlib

from mongoengine import connect
# import redis
# from redis_lru import RedisLRU


# docker run --name redis-cache -d -p 6379:6379 redis
# r = redis.Redis(host="localhost", port=6379, password=None, db=0)
# cache = RedisLRU(r)

file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
database = config.get('DEV_DB', 'DB_NAME')

uri = f"mongodb+srv://{username}:{password}@{database}/?retryWrites=true&w=majority"

session_hw = connect("home_work_8",host=uri, ssl=True)

