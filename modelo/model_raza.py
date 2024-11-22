from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,DateTime
from sqlalchemy.orm import relationship, sessionmaker
from model import Base


class Raza(Base):
    __tablename__ = 'razas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    personas = relationship('Persona', back_populates='raza')