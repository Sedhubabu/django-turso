# app/db.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

# Get Turso config
url = os.getenv("DATABASE_URL")
token = os.getenv("AUTH_TOKEN")

if not url or not token:
    raise ValueError("Missing TURSO_DATABASE_URL or TURSO_AUTH_TOKEN in .env")

# Extract hostname from the URL
hostname = url.split("://")[1]

# Create engine with libsql driver
engine = create_engine(
    f"sqlite+libsql:///{hostname}",
    connect_args={"auth_token": token},
    echo=True,
    future=True,
)

# ✅ Export these for use in views, models, etc.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
