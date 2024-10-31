import re

s = input()

x = len(s)  

my_dict = {i: [0] for i in range(1, x + 1)}

myset = set()

def contar_bloques(lista):
    if not lista:  # Si la lista está vacía, retornar 0
        return 0
    
    bloques = 1  # Inicializa el contador de bloques
    for i in range(1, len(lista)):
        if lista[i] != lista[i - 1]:  # Si el número actual es diferente al anterior
            bloques += 1  # Incrementa el contador de bloques

    return bloques

def encontrar_posiciones(string, substring):
    posiciones = []
    start = 0
    
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        posiciones.append(start)
        start += 1  # Avanzar para buscar en la siguiente posición

    return posiciones

def hacer_bloques(posiciones, length, s):
    aux_array = list(range(len(s)))
    for position in posiciones:
        if aux_array[position] == aux_array[position-1]:
            aux_array[position: position + length] = [aux_array[position]] * length
        else:
            aux_array[position: position + length] = [-position-1] * length
    
    return aux_array

for length in range(1, len(s)+1):
    for i in range(len(s)):
        if i+length <= len(s):
            myset.add(s[i: i+length])

for element in myset:
    if element in s:
        aux_array = list(range(len(s)))
        posiciones = encontrar_posiciones(s, element)
        
        aux_array = hacer_bloques(posiciones, len(element), s)
        
        
        bloques = contar_bloques(aux_array)
        value = len(element)
        my_dict[bloques].append(value)

response = list(range(len(s)))
for i in range(len(response)):
    if len(my_dict[i+1]) != 1:
        response[i] = sorted(my_dict[i+1])[1]
    else:
        response[i] = 0
print(' '.join(map(str, response)))

