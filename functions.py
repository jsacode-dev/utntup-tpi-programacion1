# - - - - Importaciones necesarias - - - -

import csv
import os
import time
from colorama import Fore, Back, Style
from rich.console import Console
from rich.table import Table

# - - - - Funciones de colores - - - -

# Función para mostrar mensajes de error en rojo
def mensaje_error(texto):
    print(Fore.RED + Style.BRIGHT + texto + Style.RESET_ALL)

# Función para mostrar mensajes de éxito en verde
def mensaje_exito(texto):
    print(Fore.GREEN + Style.BRIGHT + texto + Style.RESET_ALL)

# - - - - Funciones de validación - - - -

# Función para validar enteros
def validacion_entero(mensaje1, mensaje2 = None, negativo = True, cero_incluido = True, salto_valor = False):
    while True:
        try:
            entrada = input(mensaje1)
            if salto_valor and entrada.strip() == "":
                return None
            numero = int(entrada)
            if negativo:
                if numero < 0 or (not cero_incluido and numero == 0):
                    mensaje_error(f"ERROR! No se permiten numero negativos {'ni cero' if not cero_incluido else ''}")
                    continue
            if mensaje2 != None:
                print(mensaje2)
            return numero
        except ValueError: 
            mensaje_error("ERROR! Debe ingresar un numero entero")
        except Exception as e: 
            mensaje_error(f"Ha ocurrido un error inesperado: {e}")

# Función para validar flotantes
def validacion_float(mensaje1, mensaje2 = None, negativo = True, cero_incluido = True, salto_valor = False):
    while True:
        try:
            entrada = input(mensaje1)
            if salto_valor and entrada.strip() == "":
                return None
            numero = float(entrada)
            if negativo:
                if numero < 0 or (not cero_incluido and numero == 0):
                    mensaje_error(f"ERROR! No se permiten numero negativos {'ni cero' if not cero_incluido else ''}")
                    continue
            if mensaje2 != None:
                print(mensaje2)
            return numero
        except ValueError:
            mensaje_error("ERROR! Debe ingresar un numero positivo")
        except Exception as e:
            mensaje_error(f"Ha ocurrido un error inesperado: {e}")

# Función para validar texto
def validacion_texto(mensaje1, mensaje2 = None, salto_valor = False):
    while True:
        try:
            texto = input(mensaje1).strip()
            if salto_valor and texto == "":
                return None
            if not texto:
                mensaje_error("ERROR! No se permiten campos vacios")
                continue
            if mensaje2 != None:
                print(mensaje2)
            return texto
        except ValueError:
            mensaje_error("ERROR! Debe ingresar un texto válido")
        except Exception as e:
            mensaje_error(f"Ha ocurrido un error inesperado: {e}")

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
                mensaje_error(f"ERROR! Continente no válido. Los continentes válidos son: {', '.join(continentes_validos)}")
                continue
            if mensaje2 != None:
                print(mensaje2)
            return continente.capitalize()
        except Exception as e:
            mensaje_error(f"Ha ocurrido un error inesperado: {e}")

# - - - - Funciones principales - - - -

# Función para borrar la consola (compatible con Windows y Unix)
def limpiar_consola(tiempo_espera = None):
    if tiempo_espera is not None:
        time.sleep(tiempo_espera)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

# Función para esperar a que el usuario presione una tecla antes de continuar
def esperar_tecla():
    input("Presione Enter para continuar...")

# Funcion para armar una tabla
def armar_tabla(lista, table):
    table.add_column("País", style="bold magenta", header_style="bold bright_green", justify="center")
    table.add_column("Población", style="bold magenta", header_style="bold bright_green", justify="center")
    table.add_column("Superficie", style="bold magenta", header_style="bold bright_green", justify="center")
    table.add_column("Continente", style="bold magenta", header_style="bold bright_green", justify="center")
    for pais in lista:
        table.add_row(f"{pais["nombre"]}", f"{pais["poblacion"]}", f"{pais["superficie"]}", f"{pais["continente"]}")
    Console().print(table)
    esperar_tecla()
    limpiar_consola()

# Función para cargar los datos de países desde un archivo CSV
def cargar_paises():
    dataset = []
    error_generado = False
    try:
        with open("dataset.csv", "r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            filas_invalidas = [] # Lista para almacenar los números de línea de las filas inválidas
            for numero_linea, row in enumerate(reader, start=2): # Empezamos en 2 para contar la línea del encabezado
                try:
                    nombre = row["nombre"].strip().capitalize()
                    poblacion = int(row["poblacion"])
                    superficie = float(row["superficie"])
                    continente = row["continente"].strip().capitalize()
                    if not nombre or not continente:
                        raise ValueError("Nombre o continente vacios.")
                    if poblacion <= 0 or superficie <= 0:
                        raise ValueError("Poblacion o superficie no validas.")
                    pais = {
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente
                    }
                    dataset.append(pais)
                except (ValueError, TypeError, KeyError):
                    filas_invalidas.append(numero_linea)
            if filas_invalidas:
                mensaje_error(f"Se omitieron {len(filas_invalidas)} fila(s) invalidas del CSV: {', '.join(map(str, filas_invalidas))}")
                error_generado = True
    except FileNotFoundError:
        mensaje_error("Archivo 'dataset.csv' no encontrado. Se cargará el dataset inicial.")
        error_generado = True
    except Exception as e:
        mensaje_error(f"Ha ocurrido un error al cargar los datos: {e}")
        error_generado = True
    return (dataset, error_generado)

# Función para guardar cambios en el archvio csv
def guardar_paises(dataset):
    fieldnames = ["nombre", "poblacion", "superficie", "continente"]
    try:
        with open("dataset.csv", "w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dataset)
        mensaje_exito("Datos guardados correctamente en 'dataset.csv'.")
    except PermissionError:
        mensaje_error("No se tienen permisos para escribir en 'dataset.csv'. Verifique que el archivo no esté abierto en otro programa.")
    except OSError as e:
        mensaje_error(f"No se pudo guardar el archivo: {e}")
    except Exception as e:
        mensaje_error(f"Ha ocurrido un error inesperado al guardar los datos: {e}")

# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    menu = {
        1: "Agregar un nuevo país",
        2: "Actualizar los datos de población y superficie de un país existente",
        3: "Buscar un país por nombre",
        4: "Filtrar por continente, rango de población o rango de superficie",
        5: "Ordenar países por nombre, población o superficie",
        6: "Mostrar estadísticas",
        7: "Salir del programa",
    }

    tabla = Table(show_lines=True)
    tabla.add_column("MENU PRICIPAL", style="bold bright_yellow", justify="center")

    for k,v in menu.items():
        tabla.add_row(f"{k}) {v}")
    Console().print(tabla)

# Funcion para mostrar paises por consola
def mostrar_pais(pais):
    for k, v in pais.items():
        print(f"{k.capitalize()}: {v}")
    print("-"*50)

# Función para agregar un nuevo país al dataset
def agregar_pais(dataset):
    limpiar_consola()
    nombre = validacion_texto("Ingrese el nombre del país: ")
    if validar_pais_existente(nombre, dataset):
        mensaje_error(f"El país '{nombre.capitalize()}' ya existe en el sistema. No se puede agregar nuevamente.")
        limpiar_consola(1.5)
        return dataset
    else:
        poblacion = validacion_entero("Ingrese la población del país: ", None, True, True)
        superficie = validacion_float("Ingrese la superficie del país en km2: ", None, True, False)
        continente = validar_continente("Ingrese el continente al que pertenece el país: ")
        nuevo_pais = {
            "nombre": nombre.capitalize(),
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        dataset.append(nuevo_pais)
        mensaje_exito(f"País '{nombre.capitalize()}' cargado exitosamente al sistema.")
    limpiar_consola(1.5)
    return dataset

def actualizar_pais(dataset):
    limpiar_consola()
    nombre = validacion_texto("Ingrese el nombre del país a actualizar: ")
    if validar_pais_existente(nombre, dataset):
        for pais in dataset:
            if pais["nombre"].lower() == nombre.lower():
                modificado = False
                print("Datos actuales del país:")
                mostrar_pais(pais)
                poblacion = validacion_entero("Ingrese la nueva población del país (presione ENTER para omitir): ", None, True, True)
                superficie = validacion_float("Ingrese la nueva superficie del país en km2 (presione ENTER para omitir): ", None, True, False)
                if poblacion is not None:
                    modificado = True
                    pais["poblacion"] = poblacion
                if superficie is not None:
                    modificado = True
                    pais["superficie"] = superficie
                if modificado:
                    mensaje_exito(f"País '{nombre.capitalize()}' actualizado exitosamente.")
                else:
                    mensaje_exito("No se realizaron cambios al país.")
                break
    else:
        mensaje_error(f"El país '{nombre.capitalize()}' no existe en el sistema. No se puede actualizar.")
    limpiar_consola(1.5)
    return dataset

# Funcion para buscar un pais (coincidencia exacta o parcial)
def buscar_paises(dataset):
    limpiar_consola()
    busqueda = validacion_texto("Ingrese el nombre del pais: ", None).capitalize()
    encontrado = False
    for pais in dataset:
        if pais["nombre"].startswith(busqueda):
            if not encontrado:
                print("-"*50)
                print("RESULTADOS ENCONTRADOS")
                print("-"*50)
            encontrado = True
            mostrar_pais(pais)
    if not encontrado:
        mensaje_error("No se encontraron paises relacionados a esa busqueda!")
        limpiar_consola(1.5)
    else:
        esperar_tecla()
        limpiar_consola()

# Funcion para filtrar países (Por continente, rango de poblacion o superficie)
def filtrar_pais(dataset):
    limpiar_consola()
    opciones = {
        1: "Filtrar Por Continente",
        2: "Filtrar Por Rango de Poblacion",
        3: "Filtrar Por Rango de Superficie"
    }
    tabla = Table(show_lines=True)
    tabla.add_column("Filtrar Paises", style="bold", justify="center")
    for num, desc in opciones.items():
        tabla.add_row(f"{num}) {desc}")
    Console().print(tabla)
    opcion = validacion_entero("Ingrese una opcion: ", None, False)
    
    if opcion == 1:
        limpiar_consola()
        filtrar_por_continente(dataset)
    elif opcion == 2:
        limpiar_consola()
        filtrar_por_poblacion(dataset)
    elif opcion == 3:
        limpiar_consola()
        filtrar_por_superficie(dataset)
    else:
        mensaje_error("ERROR! Opcion fuera de rango")

# Funcion menu de continentes
def filtrar_por_continente(dataset):
    continentes = {
        1: "Africa",
        2: "America",
        3: "Asia",
        4: "Europa",
        5: "Oceania"
    }
    tabla = Table(show_lines=True)
    tabla.add_column("Filtrar Por Continentes", justify="center")
    for num, cont in continentes.items():
        tabla.add_row(f"{num}) {cont}")
    Console().print(tabla)
    opcion = validacion_entero("Ingrese una opcion: ", None, False)
    
    if opcion in continentes:
        limpiar_consola()
        paises_por_continente(opcion, dataset)
    else:
        mensaje_error("ERROR! Opcion fuera de rango")

# Funcion para filtrar países por población
def filtrar_por_poblacion(dataset):
    poblacion_min = validacion_entero("Ingrese la poblacion minima: ", None, False)
    poblacion_max = validacion_entero("Ingrese la poblacion maxima: ", None, False)

    if poblacion_min > poblacion_max:
        mensaje_error("ERROR! La poblacion minima no puede ser mayor a la maxima")
    else:
        contador = 0
        poblacion = []
        for pais in dataset:
            if poblacion_min <= pais["poblacion"] <= poblacion_max:
                poblacion.append({
                    "nombre": pais["nombre"],
                    "poblacion": pais["poblacion"],
                    "superficie": pais["superficie"],
                    "continente": pais["continente"]
                })
                contador += 1
        if contador != 0:
            limpiar_consola()
            tabla = Table(title_style="bold bright_green", title=f"Paises con poblacion entre {poblacion_min} y {poblacion_max}", show_lines= True)
            armar_tabla(poblacion, tabla)
        else:
            mensaje_error(f"No se encontrar paises con poblacion entre {poblacion_min} y {poblacion_max}")

# Funcion para filtrar países por superficie
def filtrar_por_superficie(dataset):
    superficie_min = validacion_float("Ingrese la superficie minima (en km2): ", None)
    superficie_max = validacion_float("Ingrese la superficie maxima (en km2): ", None)

    if superficie_min > superficie_max:
        mensaje_error("ERROR! La superficie minima no puede ser mayor a la maxima")
    else:
        contador = 0
        poblacion = []
        for pais in dataset:
            if superficie_min <= pais["superficie"] <= superficie_max:
                poblacion.append({
                    "nombre": pais["nombre"],
                    "poblacion": pais["poblacion"],
                    "superficie": pais["superficie"],
                    "continente": pais["continente"]
                })
                contador += 1
        if contador != 0:
            limpiar_consola()
            tabla = Table(title_style="bold bright_green", title=f"Paises con poblacion entre {superficie_min} y {superficie_max}", show_lines= True)
            armar_tabla(poblacion, tabla)
        else:
            mensaje_error(f"No se encontrar paises con poblacion entre {superficie_min} y {superficie_max}")

# Funcion para filtrar países por continente
def paises_por_continente(opcion, dataset):
    continentes = {
        1: "Africa",
        2: "America",
        3: "Asia",
        4: "Europa",
        5: "Oceania"
    }
    
    if opcion not in continentes:
        mensaje_error("ERROR! Continente no válido")
        return
    
    continente = continentes[opcion]
    paises_filtrados = []
    for pais in dataset:
        if pais["continente"] == continente:
            paises_filtrados.append({
                "nombre": pais["nombre"],
                "poblacion": pais["poblacion"],
                "superficie": pais["superficie"],
                "continente": pais["continente"]
            })
    
    if paises_filtrados:
        tabla = Table(title=f"Paises de {continente}", show_lines=True, title_style="bold bright_green")
        armar_tabla(paises_filtrados, tabla)
    else:
        mensaje_error(f"No se encuentran paises registrados de {continente}")

# Funcion para mostrar estadisticas de paises
def mostrar_estadisticas(dataset):
    limpiar_consola()
    if not dataset:
        mensaje_error("No hay datos disponibles para mostrar estadísticas.")
        limpiar_consola(1.5)
        return
    pais_mayor_poblacion = max(dataset, key=lambda x: x["poblacion"])
    pais_menor_poblacion = min(dataset, key=lambda x: x["poblacion"])
    promedio_poblacion = sum(pais["poblacion"] for pais in dataset) / len(dataset)
    promedio_superficie = sum(pais["superficie"] for pais in dataset) / len(dataset)
    paises_por_continente = {}
    for pais in dataset:
        continente = pais["continente"]
        if continente not in paises_por_continente:
            paises_por_continente[continente] = 0
        paises_por_continente[continente] += 1
    
    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']} habitantes)")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']} habitantes)")
    print(f"Promedio de población: {promedio_poblacion:.2f} habitantes")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km2")
    print("Cantidad de países por continente:")
    for continente, cantidad in paises_por_continente.items():
        print(f"  - {continente}: {cantidad} país(es)")
    esperar_tecla()
    limpiar_consola()
