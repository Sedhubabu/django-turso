# app/db.py

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Example SQLite connection (change for production)
engine = create_engine('sqlite:///embedded.db', connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
