from models.model_base import ModelBase
import sqlalchemy as sa
from datetime import datetime


class Sabor(ModelBase):
    __tablename__ = 'sabores'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome: str = sa.Column(sa.String(100), nullable=False, unique=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, nullable=False, index=True)

    def __repr__(self):
        return f"<Sabor: {self.nome}>"