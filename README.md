# Sales Sample 3

## Descripción

Proyecto de procesamiento y análisis de datos de ventas utilizando Python. El objetivo es procesar los archivos de ventas correspondientes a los tres cuatrimestres de 2025 y obtener estadísticas como el número de ventas y el importe total.

## Tecnologías utilizadas

- **Python 3:** procesamiento de los datos.
- **CSV:** lectura de los archivos de ventas mediante el módulo `csv` de la biblioteca estándar de Python.
- **SQL:** directorio destinado a consultas y scripts SQL.
- **Jupyter Notebook:** directorio destinado a notebooks de análisis y pruebas.

## Estructura del proyecto

```text
sales_sample_3/
├── README.md
├── datos/
│   ├── clean/                         # Datos procesados y limpios
│   └── raw/                           # Datos originales
│       ├── vendas_2025_cuadrimestre1.csv
│       ├── vendas_2025_cuadrimestre2.csv
│       └── vendas_2025_cuadrimestre3.csv
├── notebooks/                         # Notebooks de análisis
├── output/                            # Resultados generados
├── requirements.txt                   # Dependencias del proyecto
├── sql/                               # Consultas y scripts SQL
└── src/
    └── tarefa3.py                     # Script de procesamiento de ventas
```

## Requisitos

- Python 3 instalado.
- Archivos CSV disponibles en el directorio `datos/raw/`.

El script actual utiliza el módulo `csv`, incluido en la biblioteca estándar de Python, por lo que no necesita instalar dependencias externas adicionales.

## Ejecución

Desde la raíz del proyecto, ejecutar:

```bash
python src/tarefa3.py
```

El script procesa los archivos CSV indicados en el código y muestra por pantalla el número de ventas registradas y el importe total calculado.

## Directorios de datos

- **`datos/raw/`**: contiene los archivos originales de ventas.
- **`datos/clean/`**: destinado a almacenar los datos después de su limpieza y transformación.
- **`output/`**: destinado a guardar los resultados generados por el procesamiento.

## Autores

Trabajo realizado por:

- Alejandro López Pedreira
- Mateo López García
- Daniel Sánchez Vázquez
