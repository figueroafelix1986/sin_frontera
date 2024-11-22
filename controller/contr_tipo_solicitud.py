from sqlalchemy import desc
from modelo.model_tipo_solicitud import Tipo_Solicitud

from model import session
from datetime import datetime


class Controller_TipoSolicitud:
    def __init__(self):
        self.session = session    
        #self.dire=datetime.now()
    
    def listar_tiposolicitud(self):
        return self.session.query(Tipo_Solicitud).order_by(Tipo_Solicitud.nombre).all()
  #  def get_id_registro(self,id_persona):
  #      return self.session.query(Registro).filter_by(persona_id=id_persona).first()