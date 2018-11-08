from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

def setup_db(Base):
    engine = create_engine(
        'sqlite:////tmp/db.sqlite3'
    )

    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(engine)
    
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)

    return Session