from sqlalchemy import desc
from modelo.model_pais_ciudad import Pais_Ciudad

from model import session
from datetime import datetime


class Controller_PaisCiudad:
    def __init__(self):
        self.session = session    
        #self.dire=datetime.now()
    
    def listar_paisciudad(self):
        return self.session.query(Pais_Ciudad).order_by(Pais_Ciudad.nombre).all()
    
    
    def get_id_pais(self,id_pais):
        return self.session.query(Pais_Ciudad).filter_by(pais_id=id_pais).all()
  #  def get_id_registro(self,id_persona):
  #      return self.session.query(Registro).filter_by(persona_id=id_persona).first()