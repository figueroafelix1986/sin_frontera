from sqlalchemy import desc
from modelo.model_hijos_menor import Hijo

from model import session
from datetime import datetime


class Controller_HijosMenor:
    def __init__(self):
        self.session = session    
        #self.dire=datetime.now()
    
    def listar_hijosmenores(self,id_persona):
        return self.session.query(Hijo).filter(Hijo.persona_id==id_persona).order_by(Hijo.genero).all()
  #  def get_id_registro(self,id_persona):
  #      return self.session.query(Registro).filter_by(persona_id=id_persona).first()