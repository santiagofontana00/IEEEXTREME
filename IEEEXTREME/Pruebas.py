def generate_combinations(A):
    n = len(A)
    
    # Verificar si el arreglo tiene longitud par
    if n % 2 != 0:
        raise ValueError("El arreglo debe tener longitud par.")
    
    combinations = []
    
    # Generar combinaciones usando recursión
    def backtrack(index):
        # Si hemos procesado todos los elementos, guardamos la combinación
        if index == n:
            combinations.append(list(current_combination))
            return
        
        # Mantener el número positivo
        current_combination[index] = A[index]
        backtrack(index + 1)
        
        # Cambiar el número a negativo solo para pares consecutivos
        if index % 2 == 0 and index + 1 < n:  # Solo cambiar en la posición 2k-1
            current_combination[index] = -A[index]
            current_combination[index + 1] = -A[index + 1]  # Cambiar también el par
            backtrack(index + 2)  # Saltar al siguiente par

    # Iniciar la combinación actual
    current_combination = [0] * n
    backtrack(0)
    
    return combinations

result = generate_combinations([7, -8])
print(result)