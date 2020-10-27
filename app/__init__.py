import redis
from flask import Flask
from rq import Queue


from config import Configuration

config = Configuration()

app = Flask(__name__)
app.config.from_object(config)

# noinspection PyUnresolvedReferences
from app import routes

app.run(host='0.0.0.0')
r = redis.Redis()
q = Queue(connection=r)
