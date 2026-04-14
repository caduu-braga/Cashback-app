import sqlalchemy
from Conexao import Base

class Historico(Base):
    __tablename__ = "Cliente"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    ip = sqlalchemy.Column(sqlalchemy.String(100))
    nome = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    valor = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    desconto = sqlalchemy.Column(sqlalchemy.Float)
    cashback = sqlalchemy.Column(sqlalchemy.Float)