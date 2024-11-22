from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


# Cambia estos valores según tu configuración de PostgreSQL
#USER = 'tu_usuario'
#PASSWORD = 'tu_contraseña'
#HOST = 'localhost'  # o la dirección de tu servidor
#PORT = '5432'       # el puerto por defecto de PostgreSQL
#DATABASE = 'mi_base_de_datos'

# Crear el engine para PostgreSQL
#engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

engine = create_engine('sqlite:///mi_base_de_datos.db')
#Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



Base = declarative_base()

