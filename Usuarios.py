import json

Archivo = "Estudiantes.json"

def cargar_datos ():
    try:
        with open (Archivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        guardar_datos([])
        return []
    except json.JSONDecodeError:
        print ("Se creará un nuevo archivo")
        guardar_datos
        return []

def guardar_datos (data):
    with open (Archivo, "w") as f:
     json.dump (data, f, indent= (4))

def crear_estudiante (lista):
   nombre = input("Nombre del estudiante: ") 
   edad = input("Edad: ")
   
   estudiante = {"id": len(lista) + 1, "nombre" : nombre, "edad" : edad}

   lista.append(estudiante)
   guardar_datos(lista)
   print("Estudiante agregado correctamente.")

def mostrar_estudiantes (lista):
    if not lista:
        print ("No hay estudiantes registrados")
        return
    print ("--- Lista de estudiantes ---")
    for est in lista:
        print (f"ID: {est["ID"]} | Nombre: {est["nombre"]} | Edad {est["edad"]}")

def actualizar_estudiantes (lista):
    mostrar_estudiantes(lista)
    id_buscar = int(input("ID del estudiante a actualizar: "))

    for est in lista:
        if est["id"] == id_buscar:
            est["nombre"] = input("Nuevo nombre: ")
            est["edad"] = input("Nueva edad: ")
            guardar_datos(lista)
            print("Estudiante actualizado.")
            return
    print("No se encontró el estudiante.")

def eliminar_estudiante(lista):
    mostrar_estudiantes(lista)
    id_buscar = int(input("ID del estudiante a eliminar: "))

    for est in lista:
        if est["id"] == id_buscar:
            lista.remove(est)
            guardar_datos(lista)
            print("Estudiante eliminado.")
            return

    print("No se encontró el estudiante.")

def menu():
    lista = cargar_datos()

    while True:
        print("\n------ MENÚ CRUD ------")
        print("1. Crear estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_estudiante(lista)
        elif opcion == "2":
            mostrar_estudiantes(lista)
        elif opcion == "3":
            actualizar_estudiantes(lista)
        elif opcion == "4":
            eliminar_estudiante(lista)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

    menu()