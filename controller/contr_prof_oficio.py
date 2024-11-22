from sqlalchemy import desc
from modelo.model_profec_ofic import Profec_Ofici

from model import session
from datetime import datetime


class Controller_ProfOficio:
    def __init__(self):
        self.session = session    
        #self.dire=datetime.now()
    
    def listar_profeoficio(self):
        return self.session.query(Profec_Ofici).order_by(Profec_Ofici.nombre).all()
  #  def get_id_registro(self,id_persona):
  #      return self.session.query(Registro).filter_by(persona_id=id_persona).first()