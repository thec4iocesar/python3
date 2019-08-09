import flask

blueprint = flask.Blueprint('jenkins', __name__)

@blueprint.route('/jenkins', methods= ['GET', 'POST'])
def jenkins():    
    context = {
        'title': 'Python | Sysadmin'
    }
    return flask.render_template('jenkins.html', context=context)