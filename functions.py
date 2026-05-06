# - - - - Importaciones necesarias - - - -
import csv

# - - - - Funciones de validación - - - -

# FUNCION PARA VALIDAD ENTEROS
def validacion_entero(mensaje1, mensaje2 = None, negativo = True):
    while True:
        try: 
            numero = int(input(mensaje1))
            if negativo:
              if numero <= 0:
                  print("ERROR! No se permiten numero negativos o cero")
                  continue
            if mensaje2 != None:
              print(mensaje2) 
            return int(numero)
        except ValueError: 
            print("ERROR! Debe ingresar un numero entero")
        except Exception as e: 
            print(f"Ha ocurrido un error inesperado: {e}")

# FUNCION PARA VALIDAR FLOTANTES
def validacion_float(mensaje1, mensaje2 = None):
    while True:
        try:
            numero = float(input(mensaje1))
            if numero <= 0:
                print("ERROR! No se permiten numero negativos o cero")
                continue
            if mensaje2 != None:
                print(mensaje2)
            return numero
        except ValueError:
            print("ERROR! Debe ingresar un numero positivo")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

# FUNCION PARA VALIDAR TEXTO
def validacion_texto(mensaje1, mensaje2 = None):
    while True:
        try:
            texto = input(mensaje1).strip()
            if not texto.isalpha():
                print("ERROR! Solo se puede ingresar texto")
            else:
                if mensaje2 != None:
                    print(mensaje2)
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

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