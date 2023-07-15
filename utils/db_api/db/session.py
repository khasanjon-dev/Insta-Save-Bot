from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from data.config import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
