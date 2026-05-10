# - - - - Importaciones necesarias - - - -
import csv
# - - - - Funciones de validación - - - -

# Función para validar enteros
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

# Función para validar flotantes
def validacion_float(mensaje1, mensaje2 = None):
    while True:
        try:
            numero = float(input(mensaje1))
            if numero <= 0:
                print("ERROR! No se permiten numero negativos o cero")
                continue
            if mensaje2 != None:
                print(mensaje2)
            return float(numero)
        except ValueError:
            print("ERROR! Debe ingresar un numero positivo")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

# Función para validar texto
def validacion_texto(mensaje1, mensaje2 = None):
    while True:
        try:
            texto = input(mensaje1).strip()
            if not texto.isalpha():
                print("ERROR! Solo se puede ingresar texto")
                continue
            if mensaje2 != None:
                print(mensaje2)
            return texto
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

# Función para validar si un país ya existe en el dataset
def validar_pais_existente(nombre, dataset):
    for pais in dataset:
        if pais["nombre"].lower() == nombre.lower():
            return True
    return False

# Función para validar continente
def validar_continente(mensaje1, mensaje2 = None):
    continentes_validos = ["america", "asia", "europa", "africa", "oceania"]
    while True:
        try:
            continente = validacion_texto(mensaje1).lower()
            if continente not in continentes_validos:
                print(f"ERROR! Continente no válido. Los continentes válidos son: {', '.join(continentes_validos)}")
                continue
            if mensaje2 != None:
                print(mensaje2)
            return continente.capitalize()
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

# - - - - Funciones principales - - - -

# Funcion para guardar cambios en el archvio csv
def guardar_paises(paises):
    fieldnames = ["nombre", "poblacion", "superficie", "continente"]
    with open("dataset.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(paises)

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

# Funcion para mostrar paises por consola
def mostrar_pais(pais):
    for k, v in pais.items():
        print(f"{k.capitalize()}: {v}")
    print("-"*50)

# Función para agregar un nuevo país al dataset
def agregar_pais(dataset):
    print()
    nombre = validacion_texto("Ingrese el nombre del país: ")
    if validar_pais_existente(nombre, dataset):
        print(f"El país '{nombre.capitalize()}' ya existe en el sistema. No se puede agregar nuevamente.")
        return
    else:
        poblacion = validacion_entero("Ingrese la población del país: ")
        superficie = validacion_float("Ingrese la superficie del país en km2: ")
        continente = validar_continente("Ingrese el continente al que pertenece el país: ")
        nuevo_pais = {
            "nombre": nombre.capitalize(),
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        dataset.append(nuevo_pais)
        print(f"País '{nombre.capitalize()}' cargado exitosamente al sistema.")

# Funcion para buscar un pais (coincidencia exacta o parcial)
def buscar_paises(dataset):
    print()
    busqueda = validacion_texto("Ingrese el nombre del pais: ", None).capitalize()
    encontrado = False
    for pais in dataset:
        if pais["nombre"] == busqueda or pais["nombre"].startswith(busqueda):
            if not encontrado:
                print("-"*50)
                print("RESULTADOS ENCONTRADOS")
                print("-"*50)
            encontrado = True
            mostrar_pais(pais)
    if not encontrado:
        print("No se encontraron paises relacionados a esa busqueda!")