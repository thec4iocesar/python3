import flask

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods= ['GET', 'POST'])
def docker():    
    context = {
        'title': 'Python | Sysadmin'
    }
    return flask.render_template('gitlab.html', context=context)