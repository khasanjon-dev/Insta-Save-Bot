from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data.config import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Session = sessionmaker(engine, autoflush=True)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
