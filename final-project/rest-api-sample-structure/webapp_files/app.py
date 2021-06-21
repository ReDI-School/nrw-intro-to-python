# This is going to be a book store
# We would like to Create (Add), Checkout (Remove), Update and Read titles

# This app uses the rather simple Flask framework
from flask import Flask
from flask import request
import json
app = Flask(__name__)

# Routes define your API endpoints, if you will
# @app.route() is called a Decorator - it "decorates" a function
# This route is a dynamic route that can contain the ISBN of a book
@app.route("/things", methods=['GET'])
def get_things(optionalparametername=None):
    response = app.response_class(
        response='That works',
        status=200,
        mimetype='application/json'
    )

    return response
