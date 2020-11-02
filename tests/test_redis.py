import unittest

from config import Configuration


class TestRedis(unittest.TestCase):
    import redis
    config = Configuration()
    redis_url = config.REDIS_URL
    r = redis.from_url(redis_url)
    r.ping()
