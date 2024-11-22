from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,DateTime,Date
from sqlalchemy.orm import relationship, sessionmaker
from model import Base


class Hijo(Base):
    __tablename__ = 'hijos'
    id = Column(Integer, primary_key=True)
    genero = Column(String, nullable=False)
    
    fecha_nacimiento = Column(Date, nullable=False)
    
    # Clave foránea para relacionar con Persona
    persona_id = Column(Integer, ForeignKey('personas.id'))  # Nueva columna
    persona = relationship('Persona', back_populates='hijos')  # Cambiado a singular
    