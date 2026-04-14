import sqlalchemy
import sqlalchemy.orm

DATABASE_URL = "mysql+pymysql://root:admin@localhost/cashback"

engine = sqlalchemy.create_engine(DATABASE_URL)
SessionLocal = sqlalchemy.orm.sessionmaker(bind=engine)

Base = sqlalchemy.orm.declarative_base()

