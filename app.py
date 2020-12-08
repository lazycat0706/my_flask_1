from flask import Flask
from flask import request
from flask import redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = 'dev'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    year = db.Column(db.String(4))


# @app.cli.command()
# def forge():
#     db.create_all()
#     name = 'grey li'
#     movies = [
#         {'title': 'My Neighbor Totoro', 'year': '1988'},
#         {'title': 'Dead Poets Society', 'year': '1989'},
#         {'title': 'A Perfect World', 'year': '1993'},
#         {'title': 'Leon', 'year': '1994'},
#         {'title': 'Mahjong', 'year': '1996'},
#         {'title': 'Swallowtail Butterfly', 'year': '1996'},
#         {'title': 'King of Comedy', 'year': '1999'},
#         {'title': 'Devils on the Doorstep', 'year': '1999'},
#         {'title': 'WALL-E', 'year': '2008'},
#         {'title': 'The Pork of Music', 'year': '2012'},
#     ]
#     user = User(name=name)
#     db.session.add(user)
#     for i in movies:
#         movie = Movie(title=i['title'], year=i['year'])
#         db.session.add(movie)
#     db.session.commit()
#     click.echo('Done')


@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template('404.html'), 404


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        if not title or not year or len(year) > 4 or len(title) > 60:
            flash("Invalid input")
            print('Invalid input-----title: %s--year: %s' % (title, year))
            return redirect(url_for('index'))
        movie = Movie(title=title, year=year)
        db.session.add(movie)
        db.session.commit()
        flash("Item created")
        print('Item created-----title: %s--year: %s' % (title, year))
        return redirect(url_for('index'))
    page = request.args.get('/',1,type=int)
    per_page = request.args.get('per_page', 20, type=int)
    pagination = db.query
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)


@app.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == "POST":
        title = request.form['title']
        year = request.form['year']
        if not title or not year or len(year) > 4 or len(title) > 60:
            flash("Invalid input")
            return redirect(url_for('edit', movie_id=movie_id))
        movie.title = title
        movie.year = year
        db.session.commit()
        flash('Item Update')
        return redirect(url_for('index'))
    return render_template('edit.html', movie=movie)


@app.route('/movie/delete/<int:movie_id>', methods=['GET', 'POST'])
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Item delete')
    print('Movie delete: %s' % movie)
    return redirect(url_for('index'))


@app.route('/debug/')
def debug_info():
    return "Debug Test!"


@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)


if __name__ == '__main__':
    app.run(debug=True)
