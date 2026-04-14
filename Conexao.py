import os
import sqlalchemy
import sqlalchemy.orm

DATABASE_URL = os.getenv("mysql+pymysql://root:llVIhzbGjWIcFDhmRLtRXiACNztEJbDF@centerbeam.proxy.rlwy.net:44206/railway")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

engine = sqlalchemy.create_engine(DATABASE_URL)
SessionLocal = sqlalchemy.orm.sessionmaker(bind=engine)

Base = sqlalchemy.orm.declarative_base()

