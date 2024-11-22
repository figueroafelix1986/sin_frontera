from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,DateTime
from sqlalchemy.orm import relationship, sessionmaker
from model import Base


class Ciudad_Brasil(Base):
    __tablename__ = 'ciudad_bras'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    #personas = relationship('Persona', back_populates='pais')