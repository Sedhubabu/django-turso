# app/db.py

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
engine = create_engine(
    os.getenv("TURSO_DATABASE_URL"),
    connect_args={"authToken": os.getenv("TURSO_AUTH_TOKEN")},
    echo=True
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
