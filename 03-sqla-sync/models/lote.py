from models.model_base import ModelBase
import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from models.tipo_picole import TipoPicole


class Lote(ModelBase):
    __tablename__ = 'lotes'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    quantidade: int = sa.Column(sa.Integer, nullable=False)
    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey("tipos_picole.id"), nullable=False)

    tipo_picole: TipoPicole = orm.relationship("TipoPicole", lazy="joined")

    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, nullable=False, index=True)

    def __repr__(self):
        return f"<Lote: {self.id}>"