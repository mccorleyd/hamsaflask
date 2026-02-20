from flask import Flask
from models import db, Game
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'
db.init_app(app)

with app.app_context():
    games = [
        Game(game="CyberPunk 2077", console="PS5", started=True),
        Game(game="Pikmin", console="Nintendo Switch", started=True),
        Game(game="Unicorn Overlord", console="Nintendo Switch", started=True),
        Game(game="2XKO", console="PS5", started=True),
        Game(game="No Sleep For Kaname Date", console="Switch", started=True),
    ] 
    db.session.add_all(games)
    db.session.commit()
    print("Added games successfully!")
