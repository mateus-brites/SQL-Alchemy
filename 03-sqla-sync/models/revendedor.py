from models.model_base import ModelBase
import sqlalchemy as sa
from datetime import datetime


class Revendedor(ModelBase):
    __tablename__ = 'revendedores'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome: str = sa.Column(sa.String(100), nullable=False, unique=True)
    razao_social: str = sa.Column(sa.String(100), nullable=False, unique=False)
    contato: str = sa.Column(sa.String(100), nullable=False, unique=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, nullable=False, index=True)

    def __repr__(self):
        return f"<Revendedor: {self.nome}>"