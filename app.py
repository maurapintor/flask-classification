import redis
from flask import Flask
from rq import Queue

app = Flask(__name__)

# noinspection PyUnresolvedReferences
from app import routes

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    r = redis.Redis()
    q = Queue(connection=r)
