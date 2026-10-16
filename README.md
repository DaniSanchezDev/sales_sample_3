# Sales Sample 3

## Descripción

Proyecto de procesamiento y análisis de datos de ventas utilizando Python. El objetivo es procesar los archivos de ventas correspondientes a los tres cuatrimestres de 2025 y calcular estadísticas como el número de ventas y el importe total.

## Tecnologías utilizadas

- **Python 3:** procesamiento de los datos.
- **CSV:** lectura de los archivos de ventas mediante el módulo `csv` de la biblioteca estándar de Python.

## Estructura del proyecto

```text
sales_sample_3/
├── README.md
├── datos/
│   ├── clean/
│   └── raw/
│       ├── vendas_2025_cuadrimestre1.csv
│       ├── vendas_2025_cuadrimestre2.csv
│       └── vendas_2025_cuadrimestre3.csv
├── notebooks/
├── output/
├── requirements.txt
├── sql/
└── src/
    └── tarefa3.py
```

## Requisitos

- Python 3 instalado.
- Git instalado para clonar el repositorio.

El script actual utiliza únicamente módulos de la biblioteca estándar de Python, por lo que no requiere instalar dependencias externas.

## Instalación y ejecución

### 1. Clonar el repositorio

Desde una terminal, ejecutar:

```bash
git clone URL_DEL_REPOSITORIO
```

Sustituir `URL_DEL_REPOSITORIO` por la dirección real del repositorio.

### 2. Acceder al directorio del proyecto

```bash
cd sales_sample_3
```

### 3. Comprobar la versión de Python

```bash
python --version
```

### 4. Ejecutar el script

Desde la raíz del proyecto:

```bash
python src/tarefa3.py
```

El programa procesa los archivos CSV definidos en el script y muestra por pantalla el número de ventas registradas y el importe total calculado.

## Directorios de datos

- **`datos/raw/`**: contiene los archivos originales de ventas.
- **`datos/clean/`**: destinado a almacenar datos limpios y transformados.
- **`notebooks/`**: destinado a notebooks de análisis y pruebas.
- **`output/`**: destinado a los resultados generados.
- **`sql/`**: destinado a consultas y scripts SQL.
- **`src/`**: contiene los scripts de Python.

## Autores

Trabajo realizado por:

- Alejandro López Pedreira
- Mateo López García
- Daniel Sánchez Vázquez
