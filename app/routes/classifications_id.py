import redis
from rq import Connection, Queue

from app import app
from config import Configuration

config = Configuration()


@app.route('/classifications/<string:job_id>', methods=['GET'])
def classifications_id(job_id):
    """Returns the status and the result of the job identified
    by the id specified in the path."""
    task = None  # TODO connect to the database and get the task by the id

    response = {
        'task_status': task.get_status(),
        'data': task.result,
    }
    return response
