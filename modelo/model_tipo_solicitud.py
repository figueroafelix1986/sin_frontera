from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,DateTime
from sqlalchemy.orm import relationship, sessionmaker
from model import Base


class Tipo_Solicitud(Base):
    __tablename__ = 'tipo_solicitud'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    