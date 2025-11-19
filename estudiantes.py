import json
ruta_json = "estudiantes.json"

def leerDatos ():
    print("leer datos\n")

def guardaDatos ():
    print("guardar datos\n")

def crearEstudiante ():
    print("crear estudiantes\n")

def actualizar ():
    print("actualizar\n")

def eliminar ():
    print("eliminar\n")

programa = 0

while programa != 6:
    try:
        print("Menu:\n" \
        "1 - Leer datos\n" \
        "2 - Guardar datos\n" \
        "3 - Crear estudiante\n" \
        "4 - Actualizar\n" \
        "5 - Eliminar\n" \
        "6 - Salir")
        programa = int(input("Que quieres hacer? "))
    except:
        print("Ingresa un valor valido\n")

    if programa < 1 or programa > 6:
        print("Ingresa una opcion valida\n")
    
    if programa == 1:
        leerDatos()

    if programa == 2:
        guardaDatos()

    if programa == 3:
        crearEstudiante()

    if programa == 4:
        actualizar()

    if programa == 5:
        eliminar()