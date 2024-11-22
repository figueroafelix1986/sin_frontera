from modelo.model_pais import Pais
from model import session
import pandas as pd

class Controller_Pais:
    def __init__(self):
        self.session = session
          
        
        if self.session.query(Pais).count()==0:
            df = pd.read_csv('paises.csv') 
            for index,row in df.iterrows():
                nuevo_genero = Pais(nombre=row['nombre'])
                self.session.add(nuevo_genero)
            self.session.commit() 
             

    def agregar_pais(self, nombre):
        nuevo_pais = Pais(nombre=nombre.title())
        self.session.add(nuevo_pais)
        self.session.commit()

    def get_pais(self, nombre):
        return self.session.query(Pais).filter_by(nombre=nombre).first()
    
    def listar_paises(self):
        return self.session.query(Pais).order_by(Pais.nombre).all()
    
    def get_id_pais(self,id_pais):
        return self.session.query(Pais).filter_by(id=id_pais).first()