
import os
import sys

import flask


app = flask.Flask(__name__)

@app.route('/users/auth', methods=[ 'POST' ])
def auth_users():
    return 'auth user'

@app.route('/users', methods=[ 'GET' ])
def get_users():
    return 'get users'

@app.route('/users', methods=[ 'POST' ])
def post_users():
    return 'post users'

@app.route('/users/<userid>', methods=[ 'GET' ])
def get_user_by_id(userid):
    return 'get {} users'.format(userid)

@app.route('/users/<userid>', methods=[ 'PUT', 'PATCH' ])
def update_user_by_id(userid):
    return 'update {} users'.format(userid)

@app.route('/users/<userid>', methods=[ 'DELETE' ])
def delete_user_by_id(userid):
    return 'delete {} users'.format(userid)

if __name__ == "__main__":
    
    root_module = os.path.abspath(os.path.curdir)
    sys.path.append(root_module)

    os.environ['FLASK_APP'] = 'ex_7.py'
    os.environ['FLASK_ENV'] = 'development'

    app.run(host='0.0.0.0', debug=True)