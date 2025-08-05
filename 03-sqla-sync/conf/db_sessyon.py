import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.future.engine import Engine
from pathlib import Path
from typing import Optional
from models.model_base import ModelBase

__engine: Optional[Engine] = None

def create_engine(sqlite: bool = False) -> Engine:
    global __engine
    if __engine is None:
        
        if sqlite:
            arquivo_db = 'db/picoles.sqlite'
            folder = Path(arquivo_db).parent
            folder.mkdir(parents=True, exist_ok=True)

            conn_str = f'sqlite:///{arquivo_db}'
            __engine = sa.create_engine(conn_str, echo=False, connect_args={"check_same_thread": False})
        else:
            conn_str = "postgresql://admin:admin@localhost/sqla"
            __engine = sa.create_engine(conn_str, echo=True)
    return __engine

def create_session() -> Session:
    global __engine
    if __engine is None:
        create_engine()
    
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()
    return session

def create_tables() -> None:
    global __engine
    if __engine is None:
        create_engine()
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)