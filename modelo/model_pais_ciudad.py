from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,DateTime
from sqlalchemy.orm import relationship, sessionmaker
from model import Base


class Pais_Ciudad(Base):
    __tablename__ = 'paises_ciudad'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    pais_id = Column(Integer, ForeignKey('paises.id'), nullable=False)  # Clave foránea
    
    # Relación muchos a uno con Pais
    pais = relationship('Pais', back_populates='ciudades')