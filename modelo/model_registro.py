from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,DateTime,Date,Boolean
from sqlalchemy.orm import relationship
from model import Base



class Registro(Base):
    __tablename__ = 'registros'
    
    id = Column(Integer, primary_key=True)
    direccion = Column(String, nullable=False)
    num_ident = Column(String, nullable=False)    
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=False)
    estado_civil = Column(String, nullable=False)    
    beneficio_gobierno=Column(Boolean, default=False)
    lgbtqiapn=Column(Boolean, default=False)
    deficiencia = Column(String, nullable=False)
    situa_laboral = Column(String, nullable=False)
    nino_menor=Column(String, nullable=False)
    activ_econo=Column(String,nullable=False)
    tipo_solicitud = Column(String, nullable=False)
    status_migrat = Column(String, nullable=False)
    renta_mens = Column(String, nullable=False)
    etnia= Column(String, nullable=False)
    profec_oficio=Column(String, nullable=False)
    ciudad_resid_brasil= Column(String, nullable=False)
    uf_residen= Column(String, nullable=False)
    cadastrante= Column(String, nullable=False)    
    observacion=Column(String, nullable=True)   
    cartera_trabajo=Column(Boolean, default=False)
    # Clave foránea para la relación con Persona
    persona_id = Column(Integer, ForeignKey('personas.id'))
    fecha_creacion = Column(DateTime, nullable=False)    
    # Relación con Persona
    persona = relationship('Persona', back_populates='registros')