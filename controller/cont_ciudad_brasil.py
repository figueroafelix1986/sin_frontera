from modelo.model_ciudad_brasil import Ciudad_Brasil
from model import session
import pandas as pd

class Controller_Ciudad_Brasil:
    def __init__(self):
        self.session = session    
        
        if self.session.query(Ciudad_Brasil).count()==0:
            df = pd.read_csv('ciudad_bras.csv') 
            for index,row in df.iterrows():
                nuevo_ciudad = Ciudad_Brasil(nombre=row['nombre'])
                self.session.add(nuevo_ciudad)
            self.session.commit() 

    def get_pais(self, nombre):
        return self.session.query(Ciudad_Brasil).filter_by(nombre=nombre).first()
    
    def listar_ciudadbrasil(self):
        return self.session.query(Ciudad_Brasil).order_by(Ciudad_Brasil.nombre).all()
    #
    
