import numpy as np
import time
import matplotlib.pyplot as plt


def strassen(A, B):
    n = A.shape[0]
    # Basisfall: Wenn Matrix <= 2x2, nutze Standard-Multiplikation
    if n <= 2:
        return A @ B

    # 2. Zerlegung in Untermatrizen
    mid = n // 2
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]

    # 3. Berechne die sieben Hilfsmatrizen M1 bis M7
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    # 4. Ergebnis-Matrix C zusammensetzen
    C = np.zeros((n, n))
    C[:mid, :mid] = M1 + M4 - M5 + M7
    C[:mid, mid:] = M3 + M5
    C[mid:, :mid] = M2 + M4
    C[mid:, mid:] = M1 - M2 + M3 + M6

    return C


# Performance-Test
n_values = [2**i for i in range(2, 8)]  # n = 4, 8, 16, 32, 64, 128
times = []

for n in n_values:
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    start = time.perf_counter()
    strassen(A, B)
    times.append(time.perf_counter() - start)

# Plot
plt.loglog(n_values, times, 'o-', label='Strassen-Laufzeit')
theoretical = [times[0] * (n/n_values[0])**2.81 for n in n_values]
plt.loglog(n_values, theoretical, '--', label='Theorie O(n^2.81)')
plt.xlabel('n')
plt.ylabel('Zeit (s)')
plt.legend()
plt.title('Aufgabe 3: Strassen-Algorithmus')
plt.show()
