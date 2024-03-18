# Desde aqui se crea la base de datos

import db
from models import Biomedico, Equipo
import sys


def agregarEquiposIniciales():
    eq1 = Equipo(nombre='Monitor',
                 marca='Mindray',
                 modelo='Sv300',
                 serie=12312,
                 num_inventraio=2,
                 clasificacion_riezgo=2,
                 localizacion='Terapia intensiva')

    eq2 = Equipo(nombre='Monitor',
                 marca='Mindray',
                 modelo='Sv300',
                 serie=12123,
                 num_inventraio=1,
                 clasificacion_riezgo=2,
                 localizacion='Terapia intensiva')

    eq3 = Equipo(nombre='Monitor',
                 marca='Mindray',
                 modelo='Sv800',
                 serie=3223,
                 num_inventraio=1,
                 clasificacion_riezgo=2,
                 localizacion='Terapia intensiva')

    eq4 = Equipo(nombre='Ultrasonido',
                 marca='GE',
                 modelo='logiq E9',
                 serie=234231,
                 num_inventraio=1,
                 clasificacion_riezgo=3,
                 localizacion='Atencion ambulatoria')

    eq5 = Equipo(nombre='Maquina de anestesia',
                 marca='BIOSMEQ',
                 modelo='Datex-Ohmeda Aespire S5',
                 serie=3423,
                 num_inventraio=1223,
                 clasificacion_riezgo=6,
                 localizacion='Qx 1')

    eq6 = Equipo(nombre='Maquina de anestesia',
                 marca='BIOSMEQ',
                 modelo='Datex-Ohmeda Aespire S5',
                 serie=43231,
                 num_inventraio=465423,
                 clasificacion_riezgo=6,
                 localizacion='Qx 2')

    eq7 = Equipo(nombre='Bomba de infucion',
                 marca='PISA',
                 modelo='compactplus',
                 serie=3423,
                 num_inventraio=1223,
                 clasificacion_riezgo=6,
                 localizacion='habitacion 116')

    # conectamos con la base de datos con db.session
    lista_de_equipos = [eq1, eq2, eq3, eq4, eq5, eq6, eq7]
    db.session.add_all(lista_de_equipos)
    db.session.commit()
    db.session.close()  # cerramos la base de datos


def consultasDePrueba():
    pass


def agregarEquipo():
    print('\n Agregar Equipo')

    nombre = input('Nombre: ')
    marca = input('Marca: ')
    modelo = input('Modelo: ')
    serie = int(input('Numero de serie: '))
    num_inventraio = int(input('Numero de invetario: '))
    clasificacion_riezgo = int(input('Clasificacion de riezgo: '))
    localizacion = input('Localizacion: ')

    eq = Equipo(nombre=nombre,
                marca=marca,
                modelo=modelo,
                serie=serie,
                num_inventraio=num_inventraio,
                clasificacion_riezgo=clasificacion_riezgo,
                localizacion=localizacion)
    db.session.add(eq)
    db.session.commit()
    db.session.close()
    print('Equipo creado!!')

def editarEquipo():
    print('\nEditar Equipo')
    equipo_id = int(input('Ingrese el Id del equipo a editar: '))
    equipo = db.session.query(Equipo).filter(Equipo.id_equipo == equipo_id).first() #.first() devuelve la primera coincidencia

    if equipo is None:
        print('El equipo no existe')
    else:
        print(equipo)
        nueva_localizacion = input('\nIngrese la nueva localizacion: ')
        equipo.localizacion = nueva_localizacion
        db.session.commit()
        db.session.close()
        print('Se ha actualizado el equipo!')







def eliminarEquipo():
    pass


def verEquipos():
    print('\nVer listado de Equipos')
    equipos = db.session.query(Equipo).all()

    if len(equipos) <= 0:
        print('No hay datos para mostrar')
    else:
        for e in equipos:
            print('''\t->id: {} 
                    -> Nombre: {} 
                    -> Marca: {} 
                    -> Modelo: {} 
                    -> Serie: {} 
                    -> Numero de inventario: {}
                    -> Clasificacion de riesgo: {}
                    -> Localizacion: {}'''.format(e.id_equipo,
                                                  e.nombre,
                                                  e.marca,
                                                  e.modelo,
                                                  e.serie,
                                                  e.num_inventario,
                                                  e.clasificacion_riezgo,
                                                  e.localizacion))


def agregarBiomedico():
    print('Agregar Biomedico\n')
    id_personal = int(input("Ingrese el id personal: "))
    nombre = input("Nombre: ")
    apellido = input('Apellido:')

    b = Biomedico(id_personal, nombre, apellido)
    db.session.add(b)
    db.session.commit()
    db.session.close()
    print('Biomedico creado con exito!!')

def editarBiomedico():
    print("\nEditar Biomedico")
    biomedico_id = input('Ingrese el id de la persona que quiere editar: ')
    biomedico = db.session.query(Biomedico).filter(Biomedico.id_biomedico == biomedico_id).first()

    if biomedico == None:
        print('No se han encontrado coincidencias')
    else:
        print(biomedico)
        new_personal_id = int(input('Ingrese el nuevo id personal: '))
        biomedico.id_personal = new_personal_id
        db.session.commit()
        db.session.close()
        print('Biomedico acualizado!')
def eliminarBiomedico():
    pass
def verBiomedicos():

    biomedicos = db.session.query(Biomedico).all()

    for i in biomedicos:
        print('''
        => ID: {}
        => ID personal: {} 
        => Nombre: {}
        => Apellido: {}'''.format(i.id_biomedico, i.id_personal, i.nombre, i.apellido))

if __name__ == "__main__":

    # Reseteamos la base de datos si existe
    #db.Base.metadata.drop_all(bind=db.engine, checkfirst=True)

    # En esta linea indicamos a SQLAlchemy que cree, si no existen, las tablas
    # de todos los modelos que encuentre en models.py
    db.Base.metadata.create_all(db.engine)

    b1 = Biomedico(id_personal=12234, nombre='Sergio', apellido='Antunez')

    while (True):
        print("\n1. Agregar Equipos Iniciales\n"
              "2. Consultas de prueba\n"
              "3. Agregar equipo \n"
              "4. Editar equipo \n"
              "5. Eliminar equipo \n"
              "6. Ver Equipos \n" 
              ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
              "7. Agregar Biomedico\n"
              "8. Editar Biomedico\n"
              "9. Eliminar Biomedico\n"
              "10. Ver Biomedicos\n"
              "PRESS 0. Salir")  # CRUD: CREAR MODIFICAR ELIMINAR  CONSULTAR
        option = int(input("\nIntroduzca una opcion (1-10) 0 para salir: "))
        if option == 1:
            agregarEquiposIniciales()
        elif option == 2:
            consultasDePrueba()
        elif option == 3:
            agregarEquipo()
        elif option == 4:
            editarEquipo()
        elif option == 5:
            eliminarEquipo()
        elif option == 6:
            verEquipos()
        elif option == 7:
            agregarBiomedico()
        elif option == 8:
            editarBiomedico()
        elif option == 9:
            eliminarBiomedico()
        elif option == 10:
            verBiomedicos()
        elif option == 0:
            sys.exit(1)
        else:
            print('Opcion no valida')
