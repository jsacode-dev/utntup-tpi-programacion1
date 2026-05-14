# - - - - Importaciones necesarias - - - -
from functions import *

# - - - - Programa principal - - - -

limpiar_consola()
persistencia_error = False
dataset, error_generado = cargar_paises() # Cargar datos desde el archivo CSV al iniciar el programa

while True:
    if error_generado and not persistencia_error:
        persistencia_error = True
    else:
        limpiar_consola()
    mostrar_menu()
    opcion = validacion_entero("Seleccione una opción: ", None, False) # Acá va validación de string
    match opcion:
        case 1: # Agregar un nuevo país (con todos los datos necesarios)
            dataset = agregar_pais(dataset)
        case 2: # Actualizar los datos de población y superficie de un país existente
            dataset = actualizar_pais(dataset)
        case 3: # Buscar un país por nombre (coincidencia parcial o exacta)
            buscar_paises(dataset)
        case 4: # Filtrar por contiente, rango de poblacióno o rango de superficie
            filtrar_pais(dataset)
        case 5: # Ordenar países por nombre, población o superficie (ascendente o descendente)
            pass
        case 6: # Mostrar estadísticas como país con mayor y menor población, promedio de población, promedio de superficie o cantidad de países por continente
            mostrar_estadisticas(dataset)
        case 7: # Salir del programa
            guardar_paises(dataset)
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        case _: # Opción no válida
            print("Opción no válida. Por favor, seleccione una opción del menú.")