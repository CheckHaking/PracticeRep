from sqlalchemy import Column, Integer, String

import db


class Biomedico(db.Base):

    # Aqui es donde se configuran cosas especificas de la base de datps
    __tablename__ = "biomedico"  # nombre de la tabla
    __table_args__ = {'sqlite_autoincrement': True}  # Variable numerica usada com id Se auto incrementa
    id_biomedico = Column(Integer, primary_key=True)
    id_personal = Column(Integer)
    nombre = Column(String, nullable=False)  # esto hace que el campo nombre no pueda estar vacio
    apellido = Column(String, nullable=False)


    def __init__(self, id_personal, nombre, apellido):
        self.id_personal = id_personal
        self.nombre = nombre
        self.apellido = apellido
        print('Biomedico creado con exito ')

    def __str__(self):
        return "Biomedico({},{}, {})".format(self.nombre, self.apellido, self.id_personal)

class Equipo(db.Base):
    # Aqui es donde se configuran cosas especificas de la base de datps
    __tablename__ = "equipo"  # nombre de la tabla
    __table_args__ = {'sqlite_autoincrement': True}  # Variable numerica usada com id Se auto incrementa
    id_equipo = Column(Integer, primary_key = True)
    nombre = Column(String, nullable=False)  # esto hace que el campo nombre no pueda estar vacio
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    serie = Column(Integer)
    num_inventario = Column(Integer)
    clasificacion_riezgo = Column(Integer)
    localizacion = Column(String, nullable=False)

    def __init__(self, nombre, marca, modelo, serie, num_inventraio, clasificacion_riezgo, localizacion):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.serie = serie
        self.num_inventario = num_inventraio
        self.clasificacion_riezgo = clasificacion_riezgo
        self.localizacion = localizacion
        print('Se ha creado un equipo con exito!')

    def __str__(self):
        return 'Equipo: ({},{},{},{})'.format(self.nombre, self.marca, self.modelo, self.localizacion)
