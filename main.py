# Desde aqui se crea la base de datos
import db
from models import Persona, Equipo

if __name__ == "__main__":

    #Reseteamos la base de datos si existe
    #db.Base.metadata.drop_all(bind=db.engine, checkfirst=True)

    # En esta linea indicamos a SQLAlchemy que cree, si no existen, las tablas
    # de todos los modelos que encuentre en models.py
    db.Base.metadata.create_all(db.engine)

    p1 = Persona(nombre='Sergio', edad=21)
    print(p1)

    e1 = Equipo(nombre='Monitor Sondan', folio=323123, tipo='Imagen')
    print(e1)