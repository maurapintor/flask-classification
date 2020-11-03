from flask import Flask

from config import Configuration

config = Configuration()

app = Flask(__name__)
app.config.from_object(config)

# noinspection PyUnresolvedReferences
from app import routes

app.run(host='0.0.0.0', debug=True)
