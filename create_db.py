# create_db.py

from app.db import engine
from app.models import Base

# Create tables
def create_tables():
    Base.metadata.create_all(bind=engine)


