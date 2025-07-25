import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Get credentials from env
url = os.getenv("DATABASE_URL")
token = os.getenv("AUTH_TOKEN")

# Check both are present
if not url or not token:
    raise ValueError("Missing TURSO_DATABASE_URL or TURSO_AUTH_TOKEN in .env")

# Strip 'libsql://' prefix for SQLAlchemy URL
if url.startswith("libsql://"):
    host = url[len("libsql://"):]
else:
    raise ValueError("TURSO_DATABASE_URL must start with libsql://")

# Create engine
engine = create_engine(
    f"sqlite+libsql:///{host}",
    connect_args={"auth_token": token},
    echo=True,
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
