from flask import Flask
from flask import request
from flask import redirect, url_for, render_template
from werkzeug.routing import BaseConverter
from flask_sqlalchemy import SQLAlchemy
import os,sys

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    year = db.Column(db.String(4))





@app.route('/')
def index():
    # name = 'Grey Li'
    # movies = [
    #     {'title': 'My Neighbor Totoro', 'year': '1988'},
    #     {'title': 'Dead Poets Society', 'year': '1989'},
    #     {'title': 'A Perfect World', 'year': '1993'},
    #     {'title': 'Leon', 'year': '1994'},
    #     {'title': 'Mahjong', 'year': '1996'},
    #     {'title': 'Swallowtail Butterfly', 'year': '1996'},
    #     {'title': 'King of Comedy', 'year': '1999'},
    #     {'title': 'Devils on the Doorstep', 'year': '1999'},
    #     {'title': 'WALL-E', 'year': '2008'},
    #     {'title': 'The Pork of Music', 'year': '2012'},
    # ]
    # exam = {'A': -5}
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', user=user, movies=movies)


@app.route('/debug/')
def debug_info():
    return "Debug Test!"


if __name__ == '__main__':
    app.run(debug=True)
