from sqlalchemy import Column, Integer, String

import db


class Persona(db.Base):

    # Aqui es donde se configuran cosas especificas de la base de datps
    __tablename__ = "persona"  # nombre de la tabla
    __table_args__ = {'sqlite_autoincrement': True}  # Variable numerica usada com id Se auto incrementa
    id_persona = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)  # esto hace que el campo nombre no pueda estar vacio
    edad = Column(Integer)

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print('Persona creada con exito')

    def __str__(self):
        return "Se ha creado una Persona({},{})".format(self.nombre, self.edad)

class Equipo(db.Base):
    # Aqui es donde se configuran cosas especificas de la base de datps
    __tablename__ = "equipo"  # nombre de la tabla
    __table_args__ = {'sqlite_autoincrement': True}  # Variable numerica usada com id Se auto incrementa
    id_equipo = Column(Integer, primary_key = True)
    nombre = Column(String, nullable=False)  # esto hace que el campo nombre no pueda estar vacio
    folio = Column(Integer)
    tipo = Column(Integer)

    def __init__(self, nombre, folio, tipo):
        self.nombre = nombre
        self.folio = folio
        self.tipo = tipo
        print('Se ha creado un equipo con exito!')

    def __str__(self):
        return 'Equipo: ({},{},{})'.format(self.nombre, self.folio, self.tipo)