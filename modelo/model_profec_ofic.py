from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,DateTime
from sqlalchemy.orm import relationship, sessionmaker
from model import Base


class Profec_Ofici(Base):
    __tablename__ = 'profe_oficio'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    