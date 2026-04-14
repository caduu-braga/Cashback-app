import os
import sqlalchemy
import sqlalchemy.orm

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

engine = sqlalchemy.create_engine(DATABASE_URL)
SessionLocal = sqlalchemy.orm.sessionmaker(bind=engine)

Base = sqlalchemy.orm.declarative_base()

