# UTN TUP - TPI Programación 1

## Descripción del programa
Este programa es una aplicación de consola que permite gestionar un dataset de países. El programa ofrece funcionalidades para cargar datos desde un archivo CSV, mostrar información sobre los países, realizar búsquedas, agregar nuevos países, eliminar países existentes y guardar los cambios realizados en el archivo CSV. El programa está diseñado para ser fácil de usar y proporciona mensajes de error claros en caso de que ocurran problemas durante la carga o manipulación de los datos.

## Instrucciones de uso
### Requisitos previos
- Python 3.14.x o superior instalado en el sistema.
- Instalación de las bibliotecas necesarias utilizando (instalación obligatoria para el correcto funcionamiento del programa):
```bash
pip install colorama rich
```
> La librería `colorama` se utiliza para mejorar la visualización de los mensajes en la consola, mientras que `rich` se emplea para mostrar tablas y otros elementos de forma más atractiva.

> [!CAUTION]
> Recomendamos utilizar un entorno virtual para instalar las dependencias y evitar conflictos con otras bibliotecas instaladas globalmente.
- El archivo `dataset.csv` debe estar presente en el mismo directorio que el programa para cargar los datos de los países. Si el archivo no está presente, el programa cargará un dataset inicial predefinido.
### Ejecución del programa
1. Clonar el repositorio o descargar los archivos del programa.
2. Navegar al directorio del programa en la terminal o línea de comandos.
3. Ejecutar el programa con el comando:
```bash
python main.py
```
4. Seguir las instrucciones en pantalla para interactuar con el programa y gestionar el dataset de países.

## Ejemplos de entradas/salidas
### Ejemplo 1: Cargar datos desde el archivo CSV
- Entrada: El programa se inicia y encuentra el archivo `dataset.csv` con datos válidos
- Salida: "Datos cargados exitosamente desde 'dataset.csv'."
### Ejemplo 2: Cargar datos con filas inválidas en el CSV
- Entrada: El programa se inicia y encuentra el archivo `dataset.csv` con algunas filas que no cumplen con el formato esperado
- Salida: "Se omitieron 2 fila(s) invalidas del CSV: 3, 5"
### Ejemplo 3: Cargar datos sin encontrar el archivo CSV
- Entrada: El programa se inicia y no encuentra el archivo `dataset.csv`
- Salida: "Archivo 'dataset.csv' no encontrado. Se cargará el dataset inicial."
### Ejemplo 4: Cargar datos con un error inesperado
- Entrada: El programa se inicia y ocurre un error al intentar cargar el archivo `dataset.csv` (por ejemplo, debido a permisos insuficientes o un formato de archivo incorrecto)
- Salida: "Ha ocurrido un error al cargar los datos: [mensaje de error específico]"

## Participación de los integrantes
- Juan Santiago Arango ([@jsacode-dev](https://github.com/jsacode-dev))
- Alvaro David Salla ([@AlvaroSalla](https://github.com/AlvaroSalla))