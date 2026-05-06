# - - - - Importaciones necesarias - - - -
import csv

# - - - - Funciones de validación - - - -



# - - - - Funciones principales - - - -

# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
  print()
  print("=== Gestor de datos de países ===")
  print("> 1. Agregar un nuevo país")
  print("> 2. Actualizar los datos de población y superficie de un país existente")
  print("> 3. Buscar un país por nombre")
  print("> 4. Filtrar por continente, rango de población o rango de superficie")
  print("> 5. Ordenar países por nombre, población o superficie")
  print("> 6. Mostrar estadísticas")
  print("> 7. Salir del programa")
  # Opciones de depuración
  print("> -1. Mostrar todos los países y sus datos (DEBUG)")

# Función para obtener todos los países y sus datos, y guardarlos en una lista de diccionarios
def obtener_paises(dataset):
  with open(dataset, mode="r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    return list(lector)