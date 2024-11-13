import numpy as np
import pandas as pd

# Definimos las matrices A y B con los valores corregidos para los ejercicios 2 y 3
A1 = np.array([[0.33, 1], [1, 3]])
B1 = np.array([[4, 4], [3, 5]])

A2 = np.array([[1, 4], [0.22, 1]])
B2 = np.array([[3, 5], [-2, 2]])

# Función para calcular la norma de Frobenius
def frobenius_norm(matrix):
    return np.linalg.norm(matrix, 'fro')

# Función para calcular la norma infinita (de filas)
def infinity_norm(matrix):
    return np.linalg.norm(matrix, np.inf)

# Función para calcular el número de condición
def condition_number(matrix, norm_func):
    norm = norm_func(matrix)
    try:
        inverse_norm = norm_func(np.linalg.inv(matrix))
        return norm * inverse_norm
    except np.linalg.LinAlgError:
        # Si la matriz no es invertible, retornamos infinito
        return float('inf')

# Cálculos para las matrices del ejercicio 2 y 3
data = []
for i, (A, B) in enumerate([(A1, B1), (A2, B2)], start=2):
    kappa_A_fro = condition_number(A, frobenius_norm)
    kappa_B_fro = condition_number(B, frobenius_norm)
    kappa_A_inf = condition_number(A, infinity_norm)
    kappa_B_inf = condition_number(B, infinity_norm)
    
    data.append([i, 'A', kappa_A_fro, kappa_A_inf, "Bien condicionada" if kappa_A_fro < 10 else "Mal condicionada"])
    data.append([i, 'B', kappa_B_fro, kappa_B_inf, "Bien condicionada" if kappa_B_fro < 10 else "Mal condicionada"])

# Crear un DataFrame para organizar los resultados en forma de tabla
df = pd.DataFrame(data, columns=["Ejercicio", "Matriz", "κ (Norma Frobenius)", "κ (Norma Filas)", "Condicionamiento"])

# Mostrar la tabla
print(df)
