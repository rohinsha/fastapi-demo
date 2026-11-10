
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

# This forces the app to read from Render's Environment tab first!
db_url = os.environ.get("DATABASE_URL")

if not db_url:
    # Your fallback local database string for offline development
    db_url = "postgresql+psycopg://postgres:12345678@localhost:5432/my_portfolio_db"




engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
