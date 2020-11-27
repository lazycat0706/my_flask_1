from flask import Flask
from flask import request
from flask import redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class TelephoneConverter(BaseConverter):
    regex = r'1[3-9][0-9]{9}'


app.url_map.converters['tel'] = TelephoneConverter


@app.route('/tel/<tel:tel_num>')
def phonenum(tel_num):
    return "welcom, {}".format(tel_num)


@app.route('/')
def index():
    # return 'Hello World!'
    # URL = url_for('login')
    return redirect('/login/')


@app.route('/user/<name>')
def user(name):
    return "hello12, {}".format(name)


@app.route('/debug/')
def debug_info():
    return "Debug Test!"


@app.route('/login/')
def login():
    info = """
    <html>
        <head>

        </head>
        <body>
            <div>
            <input type="button", value="name">
            <input type="text", value="">
            <input type="button", value="passwd">
            <input type="text", value="">
            <input type="button", value="submit">
            </div>
        </body>
    </html>
    """
    return info


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True)
