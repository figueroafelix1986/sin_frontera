from sqlalchemy import desc
from modelo.model_registro import Registro
from modelo.model_persona import Persona
from sqlalchemy.orm import joinedload

from model import session
from datetime import datetime


class Controller_Registro:
    def __init__(self):
        self.session = session    
        
        
    def get_id_registro(self,id_persona):
        return self.session.query(Registro).filter_by(persona_id=id_persona).first()
    
    
    def listar_fecha(self):
        self.fecha_creacion=datetime.now()
        start_of_day = datetime(self.fecha_creacion.year, self.fecha_creacion.month, self.fecha_creacion.day)
        return self.session.query(Registro).filter(Registro.fecha_creacion>=start_of_day).order_by(desc(Registro.id)).all()
    
    
    def report_fecha(self,fecha_ini,fecha_fin):
        return (self.session.query(Registro)
            .join(Registro.persona)  # Realiza el JOIN con la relación 'persona'
            #.join(Persona.pais)      # Realiza el JOIN con la relación 'pais'           
            .filter(Registro.fecha_creacion >= fecha_ini,
                    Registro.fecha_creacion < fecha_fin)
            .options(joinedload(Registro.persona)
                    # .joinedload(Persona.pais)
                     )  # Carga las relaciones
            .order_by(desc(Registro.id))
            .all())
        