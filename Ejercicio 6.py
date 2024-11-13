import numpy as np

# Definir las matrices de coeficientes y términos independientes para ambos sistemas
A1 = np.array([[-0.10, 1.00], [0.11, -1.00]])
b1 = np.array([-2.0, 2.1])

A2 = np.array([[-0.10, 1.00], [0.11, -1.00]])
b2 = np.array([-2.00, 2.14])

# Inciso 6.1: Solución exacta del primer sistema de ecuaciones
sol1 = np.linalg.solve(A1, b1)
print("6.1 Solución exacta del primer sistema:")
print(f"x = {sol1[0]}, y = {sol1[1]}\n")

# Inciso 6.2: Solución exacta del segundo sistema de ecuaciones
sol2 = np.linalg.solve(A2, b2)
print("6.2 Solución exacta del segundo sistema:")
print(f"x = {sol2[0]}, y = {sol2[1]}\n")

# Inciso 6.3: Número de condición para ambos sistemas
cond_A1 = np.linalg.cond(A1)
cond_A2 = np.linalg.cond(A2)

print("6.3 ¿Es este un sistema bien condicionado?")

# Verificar condición para el primer sistema
print(f"Número de condición del primer sistema (κ) = {cond_A1}")
if cond_A1 > 100:
    print("El primer sistema está mal condicionado.\n")
else:
    print("El primer sistema está bien condicionado.\n")

# Verificar condición para el segundo sistema
print(f"Número de condición del segundo sistema (κ) = {cond_A2}")
if cond_A2 > 100:
    print("El segundo sistema está mal condicionado.\n")
else:
    print("El segundo sistema está bien condicionado.\n")

# Inciso 6.4: Relación entre κ, el determinante y los autovalores de la matriz de coeficientes
det_A1 = np.linalg.det(A1)
eigvals_A1 = np.linalg.eigvals(A1)
print("6.4 Relación entre κ, el determinante y los autovalores de la matriz de coeficientes para el primer sistema:")
print(f"Determinante de la matriz de coeficientes = {det_A1}")
print(f"Autovalores: λ1 = {eigvals_A1[0]}, λ2 = {eigvals_A1[1]}\n")

det_A2 = np.linalg.det(A2)
eigvals_A2 = np.linalg.eigvals(A2)
print("Relación entre κ, el determinante y los autovalores de la matriz de coeficientes para el segundo sistema:")
print(f"Determinante de la matriz de coeficientes = {det_A2}")
print(f"Autovalores: λ1 = {eigvals_A2[0]}, λ2 = {eigvals_A2[1]}")
