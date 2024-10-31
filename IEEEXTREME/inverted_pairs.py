test_cases = int(input())

A = [0] * test_cases
data = [0] * test_cases

for i in range(test_cases):
    A[i] = input()
    data[i] = [int(x) for x in input().split()]

def max_subset_sum(nums):
    n = len(nums)
    max_sum = float('-inf')  # Inicializar con el valor más bajo posible

    # Generar todos los subconjuntos utilizando una técnica de bit masking
    for i in range(1 << n):  # 2^n combinaciones
        current_sum = 0
        for j in range(n):
            if i & (1 << j):  # Verifica si el j-ésimo elemento está incluido
                current_sum += nums[j]
        max_sum = max(max_sum, current_sum)

    return max_sum

def alternative_combination_generator(input_array):
    array_length = len(input_array)
    
    # Verificar si el arreglo tiene longitud par
    if array_length % 2 != 0:
        raise ValueError("El arreglo debe tener longitud par.")

    result_combinations = []

    # Crear combinaciones iterativamente
    def generate_combinations(index, current_combination):
        if index >= array_length:
            result_combinations.append(current_combination[:])
            return
        
        # Mantener los números originales
        current_combination[index] = input_array[index]
        generate_combinations(index + 1, current_combination)
        
        # Cambiar a negativo solo en pares consecutivos
        if index % 2 == 0 and index + 1 < array_length:
            current_combination[index] = -input_array[index]
            current_combination[index + 1] = -input_array[index + 1]
            generate_combinations(index + 2, current_combination)

    # Comenzar con un arreglo temporal
    current_combination = [0] * array_length
    generate_combinations(0, current_combination)

    return result_combinations



for array in data:

    max_sum = float('-inf')

    combos = alternative_combination_generator(array)

    for list in combos:
        max_subset_sumum = max_subset_sum(list)

        if (max_sum< max_subset_sumum):
            max_sum = max_subset_sumum
    
    A[data.index(array)] = max_sum

for value in A:
    print(value)

    