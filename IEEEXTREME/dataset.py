import pandas as pd
import sys
import numpy as np



csv_data = sys.stdin.read()
if not csv_data.strip():
    raise ValueError("La entrada está vacía.")

# Leer el CSV usando pandas
data = pd.read_csv('data.csv', dtype=str)# Eliminar filas donde la columna 3 está vacía
arr = np.delete(arr, np.where(arr[:, 2] == '""'), axis=0)
#arr = np.delete(arr, np.where(arr[:, 2] == ""), axis=0)iParents = arr[:, 5] == '"Parent Event"'
iChilds = arr[:, 5] == '"IEEE Event"'codes = set(arr[iChilds, 2])
iParents &= np.isin(arr[:, 2], list(codes))  # Borro parent sin childrencodes = set(arr[iParents, 2])
iChilds &= np.isin(arr[:, 2], list(codes))  # Borro children sin parentfor c in sorted(codes):
#parent = arr[iParents][arr[iParents, 2] == c]
if len(parent) > 1:
    continue  # Borro + de un parent
if len(parent) == 0:
    continue  # Manejo de parent vacío
parent = parent[0]
childs = arr[iChilds][arr[iChilds][:, 2] == c]
if childs.size == 0:
    continue  # Manejo de hijos vacíos
childs = childs[np.lexsort((childs[:, 0], childs[:, 1]))]  # Ordeno hijos
digits = set(childs[:, 4])
if len(digits) == 0:
    continue
parent[4] = '???' if len(digits) > 1 else list(digits)[0]
print(','.join(parent))
key = parent[0]
for child in childs:
    print(','.join(np.append(child, key)))