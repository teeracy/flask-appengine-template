import flask

from applicationName import app

from applicationName.models import *

@app.route('/')
def indexView():
    return flask.render_template('index.html',
        param="params"
    )

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    return 'Sorry, unexpected error: {}'.format(e), 500
