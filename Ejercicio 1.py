import numpy as np

# Definimos la matriz A
A = np.array([
    [1, 0, -4, 1],
    [4, 5, 7, 0],
    [1, -2, 0, 3]
])

# 1. Cálculo de la norma de columnas (||A||_1)
norma_1 = np.max(np.sum(np.abs(A), axis=0))
print("Norma de columnas (||A||_1):", norma_1)

# 2. Cálculo de la norma de Frobenius (||A||_2)
norma_2 = np.sqrt(np.sum(A**2))
print("Norma de Frobenius (||A||_2):", norma_2)

# 3. Cálculo de la norma de filas (||A||_∞)
norma_infinito = np.max(np.sum(np.abs(A), axis=1))
print("Norma de filas (||A||_∞):", norma_infinito)

# Comparación de las normas
normas = {
    "Norma de columnas (||A||_1)": norma_1,
    "Norma de Frobenius (||A||_2)": norma_2,
    "Norma de filas (||A||_∞)": norma_infinito
}

# Encontrar la norma más grande
norma_mayor = max(normas, key=normas.get)
print(f"\nLa norma mayor es: {norma_mayor} con un valor de {normas[norma_mayor]}")
