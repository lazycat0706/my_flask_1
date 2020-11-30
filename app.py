from flask import Flask
from flask import request
from flask import redirect, url_for, render_template
from werkzeug.routing import BaseConverter

app = Flask(__name__)



@app.route('/')
def index():
    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    exam = {'A': -5}
    return render_template('index.html', info=exam, name=name, movies=movies)


@app.route('/debug/')
def debug_info():
    return "Debug Test!"


if __name__ == '__main__':
    app.run(debug=True)
