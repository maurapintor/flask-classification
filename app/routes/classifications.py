import redis
from flask import render_template
from rq import Connection, Queue
from rq.job import Job

from app import app
from app.forms.classification_form import ClassificationForm
from ml.classification_utils import classify_image
from config import Configuration

config = Configuration()


@app.route('/classifications', methods=['GET', 'POST'])
def classifications():
    """API for selecting a model and an image and running a 
    classification job. Returns the output scores from the 
    model."""
    form = ClassificationForm()
    if form.validate_on_submit():  # POST
        image_id = form.image.data
        model_id = form.model.data
        # TODO create the result_dict, with a key 'data' that stores
        #  the output of the classification function
        result_dict = dict()

        # returns the image classification output from the specified model
        return render_template('classification_output.html', image_id=image_id, results=result_dict)

    # otherwise, it is a get request and should return the
    # image and model selector
    return render_template('classification_select.html', form=form)
