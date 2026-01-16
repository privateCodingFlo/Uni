import numpy as np
import matplotlib.pyplot as plt
import time

# Parameter definieren
n_values = [10, 50, 100, 250, 500, 1000, 2000]
times = []

for n in n_values:
    # Erzeuge zwei zufällige n x n Matrizen
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    # Zeitmessung starten
    start_time = time.perf_counter()
    C = A @ B  # Matrix-Matrix-Multiplikation
    end_time = time.perf_counter()

    times.append(end_time - start_time)
    print(f"n={n} benötigt {end_time - start_time:.5f} Sekunden")

# Log-Log-Plot erstellen
plt.figure(figsize=(8, 5))
plt.loglog(n_values, times, marker='o', linestyle='-', label='Messwerte')

# Theoretische O(n^3) Linie zum Vergleich (skaliert auf den ersten Messwert)
theoretical_n3 = [times[0] * (n / n_values[0])**3 for n in n_values]
plt.loglog(n_values, theoretical_n3, linestyle='--',
           color='red', label='Theoretisch O(n³)')

plt.xlabel('Matrixgröße n (log-Skala)')
plt.ylabel('Zeit in Sekunden (log-Skala)')
plt.title('Aufwand Matrix-Matrix-Multiplikation')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.show()
