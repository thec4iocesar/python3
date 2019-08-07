import sys 
import os

import flask

app = flask.Flask(__name__)

if __name__ == "__main__":

    root_module = os.path.abspath(os.path.curdir)
    sys.path.append(root_module)

    app.run(host='0.0.0.0')