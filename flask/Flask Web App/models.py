from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy(# Show all SQL - don't do this in production!
                engine_options={'echo': True}
                )

class Game(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    game: Mapped[str] = mapped_column(db.String(300),unique=True)
    console: Mapped[str]
    created: Mapped[datetime] = mapped_column(default=datetime.now)
    started: Mapped[bool] = mapped_column(default=False)

    
    def __repr__(self):
        return f"Game {self.id}: {self.game}"

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    movie: Mapped[str] = mapped_column(db.String(300),unique=True)
    director: Mapped[str]
    created: Mapped[datetime] = mapped_column(default=datetime.now)
    watched: Mapped[bool] = mapped_column(default=False)

    
    def __repr__(self):
        return f"Movie {self.id}: {self.movie}"


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    book: Mapped[str] = mapped_column(db.String(300),unique=True)
    author: Mapped[str]
    created: Mapped[datetime] = mapped_column(default=datetime.now)
    started: Mapped[bool] = mapped_column(default=False)

    
    def __repr__(self):
        return f"Book {self.id}: {self.book}"


class Category(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    def __repr__(self):
        return f"Category {self.id}: {self.name}"

        
        