# Nombre (string)
# Población (int)
# Superficie en km2 (float)
# Continente (string)

# - - - - Importaciones necesarias - - - -
from functions import *

# - - - - Programa principal - - - -

while True:
  mostrar_menu()
  opcion = validacion_entero("Seleccione una opción: ", None, False) # Acá va validación de string
  match opcion:
    case 1: # Agregar un nuevo país (con todos los datos necesarios)
      pass
    case 2: # Actualizar los datos de población y superficie de un país existente
      pass
    case 3: # Buscar un país por nombre (coincidencia parcial o exacta)
      pass
    case 4: # Filtrar por contiente, rango de poblacióno o rango de superficie
      pass
    case 5: # Ordenar países por nombre, población o superficie (ascendente o descendente)
      pass
    case 6: # Mostrar estadísticas como país con mayor y menor población, promedio de población, promedio de superficie o cantidad de países por continente
      pass
    case 7: # Salir del programa
      print("Gracias por usar el programa. ¡Hasta luego!")
      break
    case -1: # DEBUG - Mostrar todos los países y sus datos
      print(obtener_paises("dataset.csv"))
    case _: # Opción no válida
      print("Opción no válida. Por favor, seleccione una opción del menú.")