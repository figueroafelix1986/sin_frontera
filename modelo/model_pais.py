from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,DateTime
from sqlalchemy.orm import relationship, sessionmaker
from model import Base


class Pais(Base):
    __tablename__ = 'paises'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)    
    # Relación uno a muchos con Persona
    personas = relationship('Persona', back_populates='pais')    
    # Relación uno a muchos con Pais_Ciudad
    ciudades = relationship('Pais_Ciudad', back_populates='pais')