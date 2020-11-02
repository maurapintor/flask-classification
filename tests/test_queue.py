import unittest

import redis
from rq import Connection, Queue

from config import Configuration


class TestRedis(unittest.TestCase):

    def setUp(self):
        config = Configuration()
        redis_url = config.REDIS_URL
        self.conn = redis.from_url(redis_url)

    def test_enqueue(self):
        with Connection(self.conn):
            q = Queue(name='test')
        job = q.enqueue(lambda x: x, 1)
        self.assertTrue(job)
        fetched = q.fetch_job(job.get_id())
        self.assertTrue(fetched)
        self.assertEqual(job.get_id(), fetched.get_id())

    def tearDown(self):
        with Connection(self.conn):
            q = Queue(name='test')
            for job in q.get_jobs():
                q.remove(job)
        self.conn.close()
