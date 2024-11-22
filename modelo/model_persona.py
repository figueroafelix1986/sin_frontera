from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,DateTime,Date
from sqlalchemy.orm import relationship
from model import Base


class Persona(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    nombre_apellido = Column(String, nullable=False)
    pais_id = Column(Integer, ForeignKey('paises.id'))
    pais = relationship('Pais', back_populates='personas')    
    nivel_escol_id = Column(Integer, ForeignKey('nivel_scol.id'))
    nivel_escol = relationship('NivelEscol', back_populates='personas')
    fecha_nacimiento=Column(Date, nullable=False)
    fecha_llegada=Column(Date, nullable=False)
    ciudad_person=Column(String, nullable=False)
    hijos = relationship('Hijo', back_populates='persona')    
    raza_id = Column(Integer, ForeignKey('razas.id'))
    raza = relationship('Raza', back_populates='personas')    
    genero_id = Column(Integer, ForeignKey('genero.id'))
    genero = relationship('Genero', back_populates='personas')    
    fecha_creacion = Column(DateTime, nullable=False)    
    # Relación uno a muchos con Registro
    registros = relationship('Registro', back_populates='persona')
    
    