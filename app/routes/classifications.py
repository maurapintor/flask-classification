import flask

from app import app


@app.route('/classifications', methods=['GET', 'POST'])
def classifications():
    if flask.request.method == 'POST':
        pass
    else:
        pass
