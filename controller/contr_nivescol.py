from modelo.model_nivel_escol import NivelEscol
from model import session


class Controller_Nivelescolar:
    def __init__(self):
        self.session = session
        
        if self.session.query(NivelEscol).count()==0:
            niveles_educacion = [
    "Analfabeto",
    "Educação infantil",
    "Fundamental",
    "Ensino Médio",
    "Ensino Técnico",
    "Superior (Graduação)",
    "Pós-Graduação",
    "Mestrado",
    "Doutorado"
]    
            for nombre in niveles_educacion:
                nuevo_nivel = NivelEscol(nombre=nombre)
                self.session.add(nuevo_nivel)
            self.session.commit() 

    def agregar_nivel_escol(self, nombre):
        
        nuevo_nivelescol = NivelEscol(nombre=nombre.title())
        self.session.add(nuevo_nivelescol)
        self.session.commit()
        
        
    def get_nivelescolar(self, nombre):
        return self.session.query(NivelEscol).filter_by(nombre=nombre).first()
    
    def listar_nivelescolar(self):
        return self.session.query(NivelEscol).order_by(NivelEscol.nombre).all()
    
    def get_id_nivelescolar(self,id_nivelesclar):
        return self.session.query(NivelEscol).filter_by(id=id_nivelesclar).first()

