import redis
from rq import Connection, Worker

from config import Configuration

config = Configuration()


def run_worker():
    """Picks tasks from the queue and runs them,
    storing back the results."""
    redis_url = config.REDIS_URL
    redis_connection = redis.from_url(redis_url)
    with Connection(redis_connection):
        worker = Worker([config.QUEUE])
        worker.work()


run_worker()
