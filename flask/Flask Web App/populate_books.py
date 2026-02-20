# populate_games.py
import pandas as pd
from flask import Flask
from models import db, Book
from datetime import datetime
from sqlalchemy import create_engine

# --- Flask app setup ---
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# --- CSV file ---
CSV_FILE = "books.csv"

# --- Function to insert games ---
def populate_books():
    # Read CSV
    df = pd.read_csv(CSV_FILE)

    # Ensure 'started' is a boolean
    df['started'] = df['started'].apply(lambda x: x in [True, 'True', 'true', '1'])

    with app.app_context():
        # Convert each row into a Book instance
        for _, row in df.iterrows():
            book = Book(
                book=row['book'],
                author=row['author'],
                started=row['started'],
                created=datetime.now()
            )
            db.session.add(book)
        
        db.session.commit()
        print(f"Inserted {len(df)} books into the database successfully!")
if __name__ == "__main__":
    populate_books()