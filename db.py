#FICHERO DE CONFIGURACION

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Seguridad, acceso, deberia ir en este file
#ENGINE permite a SQLAlchemy comunicarse con la base de datos en un dialecto concreto
# docs https://docs.sqlalchemy.org/en/13/dialects/index.html
#engine = create_engine('sqlite:///Carpeta_donde_se_va_guardar(database)/personas.db')
engine = create_engine('sqlite:///database/invetario.db')
#ADVERTENVIA: Crear el engine no conecta inmediatamente con l DB, eso lo hacemos luego

#Creamos La sesion es el objeto que nos va ayuadar en las transacciones dentro de nuestra DB
Session = sessionmaker(bind=engine)
session = Session() #este es nuestra conexion con la base de datos para modificar la base de datos

#Ahora vamos al archivo models.py en los modelos(clases) donde queremos que se transformen en tablas
#le aniadiremos esta variable y esto se encraga de mapear y vincular cada clase a cada tabla
Base = declarative_base() #es la encargada de decirle que nuestra clases se convertiran entablas

