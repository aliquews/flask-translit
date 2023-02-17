from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from config import DB_URL


engine = create_engine(DB_URL)
session_maker = sessionmaker(engine, class_=Session, expire_on_commit=False)
Base = declarative_base()

def get_session():
    with session_maker() as session:
        yield session