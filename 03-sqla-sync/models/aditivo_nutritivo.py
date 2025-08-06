import sqlalchemy as sa

from datetime import datetime
from models.model_base import ModelBase

class AditivoNutritivo(ModelBase):
    __tablename__ = 'aditivos_nutritivos'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome: str = sa.Column(sa.String(100), nullable=False, unique=True)
    formula_quimica: str = sa.Column(sa.String(255), nullable=False, unique=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, nullable=False, index=True)

    def __repr__(self):
        return f"<Aditivo Nutritivo: {self.nome}>"