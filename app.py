from flask import Flask
from flask import request
from flask import redirect, url_for, render_template
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route('/')
def index():
    exam = {'A': -5}
    return render_template('index.html', info=exam)


@app.route('/debug/')
def debug_info():
    return "Debug Test!"


if __name__ == '__main__':
    app.run(debug=True)
