import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("TURSO_DATABASE_URL")  # e.g., libsql://mydb-sedhu.turso.io
token = os.getenv("TURSO_AUTH_TOKEN")

# Strip scheme and use correct libsql connection format
hostname = url.split("://")[1]

engine = create_engine(
    f"sqlite+libsql:///{hostname}",
    connect_args={"auth_token": token},  # ✅ FIXED
    echo=True
)


SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100))