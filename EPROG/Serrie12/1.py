import numpy as np

# 1. Koeffizientenmatrix A und Vektor b definieren
A = np.array([[1, 1, 2],
              [2, 3, 1],
              [7, 9, -3]])

b = np.array([3, 5, 0])

# --- Methode A: Direkte Lösung ---
try:
    x_direct = np.linalg.solve(A, b)
    print("Direkte Lösung (np.linalg.solve):", x_direct)
except np.linalg.LinAlgError as e:
    print("Direkte Lösung fehlgeschlagen:", e)

# --- Methode B: Über die Inverse ---
try:
    A_inv = np.linalg.inv(A)
    x_inverse = A_inv @ b
    print("Lösung über Inverse (A^-1 * b):", x_inverse)
except np.linalg.LinAlgError as e:
    print("Invertierung fehlgeschlagen:", e)

# --- Die Probe ---
# Berechnung A * x und schauen, ob b herauskommt
if 'x_direct' in locals():
    probe = A @ x_direct
    print("Probe (A * x):", probe)
    print("Differenz zu b:", probe - b)

# --- Determinante prüfen ---
det = np.linalg.det(A)
print(f"Determinante von A: {det}")
