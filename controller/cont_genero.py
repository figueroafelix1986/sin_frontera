from modelo.model_genero import Genero
from model import session

class Controller_Genero:
    def __init__(self):
        self.session = session
        
        
        if self.session.query(Genero).count()==0:
            generos_list=['Masculino','Feminino','Outros']
            for nombre in generos_list:
                nuevo_genero = Genero(nombre=nombre)
                self.session.add(nuevo_genero)
            self.session.commit() 

    def agregar_sexo(self, nombre):
        nuevo_pais = Genero(nombre=nombre.title())
        self.session.add(nuevo_pais)
        self.session.commit()

    def get_genero(self, nombre):
        return self.session.query(Genero).filter_by(nombre=nombre).first()
    
    def listar_genero(self):
        return self.session.query(Genero).order_by(Genero.nombre).all()
    
    def get_id_genero(self,id_genero):
        return self.session.query(Genero).filter_by(id=id_genero).first()