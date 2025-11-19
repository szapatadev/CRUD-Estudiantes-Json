import json # Importamos el módulo JSON para leer y escribir datos en formato JSON.

# Nombre del archivo donde se almacenarán los datos de los estudiantes
Archivo = "Estudiantes.json"

def cargar_datos ():
    """
    Carga los datos desde el archivo JSON.
    Si el archivo no existe o está corrupto, crea uno nuevo y devuelve una lista vacía.
    """
    try:
        with open (Archivo, "r") as f: # Abrir el archivo en modo lectura
            return json.load(f)  # Contenido del JSON como lista/diccionario
    except FileNotFoundError:
        # Si el archivo no existe, lo crea vacío
        guardar_datos([])
        return []
    except json.JSONDecodeError:
        # Si el archivo existe pero está dañado o vacío
        print ("Se creará un nuevo archivo")
        guardar_datos # Reemplaza con un archivo vacío
        return []

def guardar_datos (data):
    """
    Guarda la lista de estudiantes en el archivo JSON con formato legible.
    """
    with open (Archivo, "w") as f: # Abrir archivo en modo escritura
     json.dump (data, f, indent= (4)) # Guardar con indentación para buena lectura

def crear_estudiante (lista):
   """
    Crea un nuevo estudiante y lo agrega a la lista.
    """
   nombre = input("Nombre del estudiante: ") 
   edad = input("Edad: ")
   
   # Crear el diccionario del estudiante con un ID autoincrementado
   estudiante = {"id": len(lista) + 1, "nombre" : nombre, "edad" : edad}

   lista.append(estudiante) # Añadir a la lista
   guardar_datos(lista) # Guardar los cambios en el archivo JSON
   print("Estudiante agregado correctamente.")

def mostrar_estudiantes (lista):
    """
    Muestra todos los estudiantes registrados.
    """
    if not lista: # Si la lista está vacía
        print ("No hay estudiantes registrados")
        return
    print ("--- Lista de estudiantes ---")
    for est in lista:
        # Mostrar los datos de cada estudiante
        print (f"id: {est["id"]} | Nombre: {est["nombre"]} | Edad {est["edad"]}")

def actualizar_estudiantes (lista):
    """
    Permite actualizar el nombre o edad de un estudiante según su ID.
    """
    mostrar_estudiantes(lista) # Mostrar la lista para elegir
    id_buscar = int(input("ID del estudiante a actualizar: "))

    for est in lista:
        if est["id"] == id_buscar: # Si el ID coincide
            est["nombre"] = input("Nuevo nombre: ")
            est["edad"] = input("Nueva edad: ")
            guardar_datos(lista) # Guardar cambios
            print("Estudiante actualizado.")
            return
    print("No se encontró el estudiante.")

def eliminar_estudiante(lista):
    """
    Elimina un estudiante usando su ID.
    """
    mostrar_estudiantes(lista)
    id_buscar = int(input("ID del estudiante a eliminar: "))

    for est in lista:
        if est["id"] == id_buscar:
            lista.remove(est) # Elimina el objeto de la lista
            guardar_datos(lista) # Guarda los cambios
            print("Estudiante eliminado.")
            return

    print("No se encontró el estudiante.")

def menu():
    """
    Menú principal que permite al usuario seleccionar una acción CRUD.
    """
    lista = cargar_datos() # Cargar estudiantes al iniciar el programa

    while True:
        print("\n------ MENÚ CRUD ------")
        print("1. Crear estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        # Evaluar opción elegida
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

# Ejecuta el menú al iniciar el programa
menu()