import redis
from flask import Flask
from rq import Queue

app = Flask(__name__)

# noinspection PyUnresolvedReferences
from app import routes

app.run(host='0.0.0.0')
r = redis.Redis()
q = Queue(connection=r)
