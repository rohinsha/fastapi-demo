
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql+psycopg://postgres:12345678@localhost:5432/my_portfolio_db"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
