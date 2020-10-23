from app import app

@app.route('/classifications/<string:job_id>', methods=['GET'])
def classifications_id(job_id):
    pass