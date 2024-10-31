import io
import csv

# Leer la entrada completa hasta EOF
entrada = []
try:
    while True:
        linea = input()
        entrada.append(linea)
except EOFError:
    pass

# Unir las líneas en una sola cadena y simular un archivo en memoria
csv_data = "\n".join(entrada)
df = io.StringIO(csv_data)

# Leer los datos en una lista de listas usando csv.reader
data = list(csv.reader(df))

# Eliminar filas sin acrónimo (columna 3)
data = [row for row in data if row[2]]  # Filtra si columna 3 está vacía

# Filtrar entradas basadas en "Parent Event" y verificar acrónimos
for i in range(len(data) - 1, -1, -1):
    entry = data[i][5]  # Columna 6
    acronym = data[i][2]  # Columna 3
    if entry == "Parent Event" and not any(d[2] == acronym and d[5] == "IEEE Event" for d in data):
        del data[i]

# Filtrar entradas basadas en "IEEE Event" y verificar acrónimos
for i in range(len(data) - 1, -1, -1):
    entry = data[i][5]  # Columna 6
    acronym = data[i][2]  # Columna 3
    if entry == "IEEE Event" and sum(1 for d in data if d[2] == acronym and d[5] == "Parent Event") != 1:
        del data[i]

# Filtrar entradas basadas en "Parent Event" y verificar acrónimos
for i in range(len(data) - 1, -1, -1):
    entry = data[i][5]  # Columna 6
    acronym = data[i][2]  # Columna 3
    if entry == "Parent Event" and not any(d[2] == acronym and d[5] == "IEEE Event" for d in data):
        del data[i]

# Filtrar entradas basadas en "IEEE Event" y verificar acrónimos
for i in range(len(data) - 1, -1, -1):
    entry = data[i][5]  # Columna 6
    acronym = data[i][2]  # Columna 3
    if entry == "IEEE Event" and sum(1 for d in data if d[2] == acronym and d[5] == "Parent Event") != 1:
        del data[i]

# Buscar valores de la columna 7 para entradas que coinciden con "IEEE Event"
for i in range(len(data)):
    entry = data[i][5]  # Columna 6
    acronym = data[i][2]  # Columna 3
    if entry == "Parent Event":
        # Crear un conjunto con los valores de la columna 7 de las entradas que coinciden
        digit_code = set([d[4] for d in data if d[2] == acronym and d[5] == "IEEE Event"])
        
        if len(digit_code) == 1:
            data[i][4] = digit_code.pop()
        else:
            data[i][4] = "???"

# Ordenar data por acrónimo (columna 3), luego por "Parent Event" (columna 6), y luego por nombre e ID
data = sorted(data, key=lambda x: (x[2], x[5] != "Parent Event", x[1], x[0]))

# Crear un diccionario para mapear los IDs de los Parent Events
parent_ids = {row[2]: row[0] for row in data if row[5] == "Parent Event"}

# Asignar el ID del Parent Event a los Child Events
for row in data:
    if row[5] != "Parent Event":
        # Verifica si existe el ID del Parent
        if parent_ids.get(row[2]) is not None:
            row.append(parent_ids[row[2]])  # Agrega el ID del Parent

# Imprimir el resultado como una oración
for row in data:
    print(",".join(f'"{item}"' if isinstance(item, str) and (i != 0 and i != 6 and i != 3 and i != 4) else str(item) if item != "" else '' for i, item in enumerate(row)))  # Combina los elementos de la fila en una cadena con comillas solo para strings, excluyendo columnas 1, 4 y 7 y representando espacios vacíos como ""
