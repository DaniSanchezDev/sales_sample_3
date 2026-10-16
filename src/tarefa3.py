import csv
datos = {}
archivos = [
    "datos/raw/vendas_2025_cuadrimestre1.csv",
    "datos/raw/vendas_2025_cuadrimestre2.csv",
    "datos/raw/vendas_2025_cuadrimestre3.csv"
]

for nome_archivo in archivos:
    with open(nome_archivo, newline="", encoding="utf-8") as arquivo:
        lector = csv.DictReader(arquivo, delimiter=";")


        for fila in lector:
            id_venda = int(fila["id_venda"])
            importe = float(fila["importe"].replace(",", "."))

            datos[id_venda] = importe

print(len(datos))
print(f"{sum(datos.values()):.2f} €")
