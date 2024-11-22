from modelo.model_raza import Raza
from model import session

class Controller_Raza:
    def __init__(self):
        self.session = session    
        
        if self.session.query(Raza).count()==0:
            colores = [
    "Branco",
    "Preto",
    "Pardo",
    "Amarelo",
    "Indígena",
    "Não sabe/Prefere não responder (Não ler esta opção)"
    
]
            for nombre in colores:
                nuevo_raza = Raza(nombre=nombre)
                self.session.add(nuevo_raza)
            self.session.commit() 

    def agregar_raza(self, nombre):
        nuevo_raza = Raza(nombre=nombre.title())
        self.session.add(nuevo_raza)
        self.session.commit()

    def get_raza(self, nombre):
        return self.session.query(Raza).filter_by(nombre=nombre).first()
    
    def listar_raza(self):
        return self.session.query(Raza).order_by(Raza.nombre).all()
    
    def get_id_raza(self,id_raza):
        return self.session.query(Raza).filter_by(id=id_raza).first()