from flask import Flask, render_template, abort, request, redirect, url_for
from sqlalchemy import select
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Length

from models import db, Game, Movie, Book

app = Flask(__name__)
app.config["SECRET_KEY"] = "42edWmCKqQA0FK0zt78CaPDUNvOMy0Rf-O9wm3_GCqSFgM"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'
db.init_app(app)

db_1 = [
    {"movie": "Paprika", "director": "Satoshi Kon"},
    {"movie": "The Dark Knight", "director": "Port-au-Prince"},
    {"movie": "Shall We Dance", "director": "Bishkek"},
    {"movie": "Breakin All the Rules", "director": "Manila"},
    {"movie": "Capital of Uruguay", "director": "Montevideo"},
]

db_2 = [
    {"book": "The Colour of Madness", "author": "Satoshi Kon"},
    {"book": "The Dark Knight", "author": "Port-au-Prince"},
    {"book": "Shall We Dance", "author": "Bishkek"},
    {"book": "Breakin All the Rules", "author": "Manila"},
    {"book": "Capital of Uruguay", "author": "Montevideo"},
]


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        games=db.session.execute(select(Game)).scalars(),
        movies=db.session.execute(select(Movie)).scalars(),
        books=db.session.execute(select(Book)).scalars()
    )


@app.route("/game/<int:id>")
def game_view(id):
    game = db.get_or_404(Game, id)
    return render_template("game.html",
                           game=game)

@app.route("/movie/<int:id>")
def movie_view(id):
    movie = db.get_or_404(Movie, id)
    return render_template("movie.html",
                           movie=movie)

@app.route("/book/<int:id>")
def book_view(id):
    book = db.get_or_404(Book, id)
    return render_template("book.html",
                           book=book)



class AddGameForm(FlaskForm):
    game = StringField("Game", validators=[InputRequired(), Length(max=25)])
    console = StringField("Console", validators=[InputRequired()])
    started = BooleanField("Started?")  

class AddMovieForm(FlaskForm):
    movie = StringField("movie", validators=[InputRequired(), Length(max=25)])
    director = StringField("director", validators=[InputRequired()])
    watched = BooleanField("Watched?")  

class AddBookForm(FlaskForm):
    book = StringField("book", validators=[InputRequired(), Length(max=25)])
    author = StringField("author", validators=[InputRequired()])
    started = BooleanField("Started?")  



@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    form = AddGameForm(request.form)
    if form.validate_on_submit():
        new_game = Game(
            game=form.game.data,
            console=form.console.data,
            started=form.started.data  
        )
        db.session.add(new_game)
        db.session.commit()
        return redirect(url_for("game_view", id=new_game.id))
    else:
        return render_template("add_game.html", form=form)

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm(request.form)
    if form.validate_on_submit():
        new_movie = Movie(
            movie=form.movie.data,
            director=form.director.data,
            watched=form.watched.data  
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("movie_view", id=new_movie.id))
    else:
        return render_template("add_movie.html", form=form)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm(request.form)
    if form.validate_on_submit():
        new_book = Book(
            book=form.book.data,
            author=form.author.data,
            started=form.started.data  
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("book_view", id=new_book.id))
    else:
        return render_template("add_book.html", form=form)



@app.route('/remove_game/<int:id>', methods=['GET', 'POST'])
def remove_game(id):
    game = db.get_or_404(Game, id)
    if request.method == 'POST':
        db.session.delete(game)
        db.session.commit()
        return redirect(url_for('welcome'))
    else:
        return render_template("remove_game.html",
                               game=game)

@app.route('/remove_movie/<int:id>', methods=['GET', 'POST'])
def remove_movie(id):
    movie = db.get_or_404(Movie, id)
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('welcome'))
    else:
        return render_template("remove_movie.html",
                               movie=movie)


@app.route('/remove_book/<int:id>', methods=['GET', 'POST'])
def remove_book(id):
    book = db.get_or_404(Book, id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('welcome'))
    else:
        return render_template("remove_book.html",
                               book=book)


if __name__ == '__main__':
    app.run(debug=True)