# populate_games.py
import pandas as pd
from flask import Flask
from models import db, Game
from datetime import datetime
from sqlalchemy import create_engine

# --- Flask app setup ---
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# --- CSV file ---
CSV_FILE = "games.csv"

# --- Function to insert games ---
def populate_games():
    # Read CSV
    df = pd.read_csv(CSV_FILE)

    # Ensure 'started' is a boolean
    df['started'] = df['started'].apply(lambda x: x in [True, 'True', 'true', '1'])

    with app.app_context():
        # Convert each row into a Game instance
        for _, row in df.iterrows():
            game = Game(
                game=row['game'],
                console=row['console'],
                started=row['started'],
                created=datetime.now()
            )
            db.session.add(game)
        
        db.session.commit()
        print(f"Inserted {len(df)} games into the database successfully!")
if __name__ == "__main__":
    populate_games()