# CRUD de Estudiantes con Archivos JSON
Este proyecto implementa un sistema CRUD (Crear, Leer, Actualizar y Eliminar) para la gestión de estudiantes usando archivos JSON como base de datos.
El programa funciona por consola e incluye validaciones básicas, manejo de errores y persistencia de datos.

## Características principales
- Crear estudiantes
- Mostrar lista completa
- Actualizar un estudiante
- Eliminar un registro
- Guardar automáticamente en archivo JSON
- Cargar datos al iniciar
- Menú interactivo por consola

## ¿Cómo funciona?
El sistema utiliza un archivo llamado: Estudiantes.json
Todas las operaciones CRUD se realizan sobre la estructura guardada allí.
Si el archivo no existe, el programa lo crea automáticamente.

## Estructura del proyecto
1. cargar_datos()
Carga los datos desde Estudiantes.json.
Si no existe, crea un archivo vacío.
2. guardar_datos(lista)
Guarda la lista completa de estudiantes en formato JSON.
3. crear_estudiante(lista)
Solicita al usuario: Nombre, Edad, ID único, Luego añade el estudiante a la lista.
4. mostrar_estudiantes(lista)
Imprime todos los estudiantes en pantalla.
5. actualizar_estudiantes(lista)
Permite modificar los datos de un estudiante existente según su ID.
6. eliminar_estudiante(lista)
Elimina un registro por ID.
7. menu()
Muestra las opciones:
