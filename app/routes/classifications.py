from app import app

@app.route('/classifications')
def index():
    return"Hello, World!"