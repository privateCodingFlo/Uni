import numpy as np
import matplotlib.pyplot as plt


def mc_integral(f, a, b, n):
    # Erzeuge n zufällige Punkte im Intervall [a, b]
    x = np.random.uniform(a, b, n)
    # Mittelwert der Funktionswerte * Intervalllänge
    return (b - a) * np.mean(f(x))


# Testfunktion: f(x) = x^2, Integral von 0 bis 1 ist 1/3
def f(x): return x**2


true_val = 1/3
a, b = 0, 1

n_values = [10**i for i in range(1, 6)]
errors = []

for n in n_values:
    # Mehrere Berechnungen pro n zur Mittelung des Fehlers
    temp_errors = [abs(mc_integral(f, a, b, n) - true_val) for _ in range(20)]
    errors.append(np.mean(temp_errors))

# Log-Log Plot des Fehlers
plt.loglog(n_values, errors, 'o-', label='Simulation')
plt.loglog(n_values, 1/np.sqrt(n_values), '--',
           label='1/sqrt(n)')
plt.xlabel('Anzahl Punkte n')
plt.ylabel('Mittlerer Fehler')
plt.legend()
plt.title('Aufgabe 6: Monte-Carlo Fehlerkonvergenz')
plt.show()
