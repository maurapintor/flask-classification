from app import app


@app.route('/info', methods=['GET'])
def info():
    """Returns a dictionary with the list of models and
    the list of available image files."""
    pass
