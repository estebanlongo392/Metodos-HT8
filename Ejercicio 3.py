import numpy as np

# Definir las matrices A y B
A = np.array([[1, 4], [0.22, 1]])
B = np.array([[3, 5], [-2, 2]])

# 3.1 Calcular las normas de Frobenius para A, B, A⁻¹ y B⁻¹
print("3.1 Normas de las matrices:")
print("Fórmula de la norma de Frobenius: ||A||_2 = sqrt(Σ|a_ij|^2)")

norm_A = np.linalg.norm(A, ord='fro')
norm_B = np.linalg.norm(B, ord='fro')
print("Resultado:")
print(f"Norma de A (Frobenius): ||A||_2 = {norm_A:.2f}")
print(f"Norma de B (Frobenius): ||B||_2 = {norm_B:.2f}")

A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)

print("\nFórmula de la norma de la inversa: ||A⁻¹||_2 = sqrt(Σ|a_ij⁻¹|^2)")
norm_A_inv = np.linalg.norm(A_inv, ord='fro')
norm_B_inv = np.linalg.norm(B_inv, ord='fro')
print("Resultado:")
print(f"Norma de A inversa (Frobenius): ||A⁻¹||_2 = {norm_A_inv:.2f}")
print(f"Norma de B inversa (Frobenius): ||B⁻¹||_2 = {norm_B_inv:.2f}")
print()

# 3.2 Calcular el número de condicionamiento para A y B
print("3.2 Número de condicionamiento:")
print("Fórmula del número de condicionamiento: κ(A) = ||A||_2 * ||A⁻¹||_2")

# Cálculo del número de condicionamiento
kappa_A = norm_A * norm_A_inv
kappa_B = norm_B * norm_B_inv

print("Cálculo:")
print(f"κ(A) = ||A||_2 * ||A⁻¹||_2 = {norm_A:.2f} * {norm_A_inv:.2f} = {kappa_A:.2f}")
print(f"κ(B) = ||B||_2 * ||B⁻¹||_2 = {norm_B:.2f} * {norm_B_inv:.2f} = {kappa_B:.2f}")
print()

# 3.3 Calcular el determinante para A y B
print("3.3 Determinantes de las matrices:")
print("Fórmula del determinante para una matriz 2x2: det(A) = a11 * a22 - a12 * a21")

det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
print("Resultado:")
print(f"Determinante de A: det(A) = {det_A:.2f}")
print(f"Determinante de B: det(B) = {det_B:.2f}")
print()

# 3.4 Verificar el condicionamiento de las matrices
print("3.4 Condicionamiento de las matrices:")
print("Criterio: Una matriz está bien condicionada si κ < 10 y mal condicionada si κ >= 10")

# Mostrar los valores de kappa y la conclusión sobre el condicionamiento
print("Valores de κ:")
print(f"κ(A) = {kappa_A:.2f}")
print(f"κ(B) = {kappa_B:.2f}")
print("Resultado:")

if kappa_A >= 10:
    print("La matriz A está mal condicionada.")
else:
    print("La matriz A está bien condicionada.")

if kappa_B >= 10:
    print("La matriz B está mal condicionada.")
else:
    print("La matriz B está bien condicionada.")
-