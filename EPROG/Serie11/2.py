import time
import random
import math
import matplotlib.pyplot as plt


def merge(left, right):
    """
    Merge Schritt: Fügt zwei sortierte Listen zu einer sortierten Liste zusammen.
    Aufwand: O(len(left) + len(right)), also linear bzgl. der Gesamtanzahl n = len(left) + len(right).
    Dies entspricht dem Term 'bn' in der Aufgabenstellung.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Reste anhängen (falls eine Liste noch Elemente hat)
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergesort(arr):
    """
    Rekursiver MergeSort.
    Rekursionsgleichung: A(n) <= 2*A(n/2) + bn + c
    - 2*A(n/2): Zwei rekursive Aufrufe für die Hälften.
    - bn: Aufwand für das Mergen (linear).
    - c: Konstanter Aufwand für Base-Case Check, Slicing etc.
    """
    # Basisfall: Konstante Zeit c
    # A(1) = const
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Rekursiver Aufstieg: 2 * A(n/2)
    left_sorted = mergesort(arr[:mid])
    right_sorted = mergesort(arr[mid:])

    # Merge Schritt: bn
    return merge(left_sorted, right_sorted)


# Theoretische Beweisführung als Kommentar (gemäß Aufgabe):
"""
Beweis zu Aufgabe 2:

1. Rekursionsungleichung A(n) <= 2A(n/2) + bn + c:
   - Der Algorithmus teilt die Liste der Länge n in zwei Hälften der Länge n/2.
   - Diese werden rekursiv sortiert: Kosten 2 * A(n/2).
   - Danach werden sie mit 'merge' zusammengefügt. Der Merge-Vorgang durchläuft beide Teillisten einmal linear.
     Der Aufwand ist also proportional zu n. Sei b die Proportionalitätskonstante, so ist der Aufwand <= bn.
   - Dazu kommen konstante Kosten c für Vergleiche, Zuweisungen etc. im Funktionsrumpf.
   => A(n) <= 2A(n/2) + bn + c

2. Zeigen der Lösung A(n) = Dn log(n):
   Wir setzen den Ansatz A(n) = Dn log2(n) in die Ungleichung ein (log zur Basis 2):
   
   Zu zeigen: Dn log2(n) >= 2(D(n/2) log2(n/2)) + bn + c  (für die obere Schranke betrachten wir es asymptotisch)
   
   Rechte Seite:
   2 * (D * n/2 * log2(n/2)) + bn + c
   = D * n * (log2(n) - log2(2)) + bn + c
   = D * n * (log2(n) - 1) + bn + c
   = D * n * log2(n) - D * n + bn + c
   
   Damit A(n) <= Rechte Seite gilt, muss gelten:
   A(n) <= A(n) - Dn + bn + c
   0 <= -Dn + bn + c
   Dn >= bn + c
   D >= b + c/n
   
   Da b und c Konstanten sind, existiert ein D (z.B. D >= b + c), sodass die Ungleichung für alle n >= 1 erfüllt ist.
   Somit ist A(n) = O(n log n).
"""


def measure_complexity():
    # Wir testen mit n = 2^k, wie in der Aufgabe angenommen
    k_values = range(5, 15)  # k von 5 bis 14 (n = 32 bis 16384)
    list_sizes = [2**k for k in k_values]
    times = []

    theoretical_curve = []

    print("Messung gestartet...")
    for size in list_sizes:
        test_list = [random.randint(0, 100000) for _ in range(size)]

        start_time = time.time()
        mergesort(test_list)
        end_time = time.time()

        duration = end_time - start_time
        times.append(duration)

        # Für Vergleichskurve (dn log n)
        theoretical_curve.append(size * math.log2(size))

        print(f"n: {size}, Zeit: {duration:.6f} Sekunden")

    # Skalierung der theoretischen Kurve an den letzten Messwert, damit sie im Plot vergleichbar liegt
    scale_factor = (
        times[-1] / theoretical_curve[-1] if theoretical_curve[-1] != 0 else 1
    )
    theoretical_curve_scaled = [t * scale_factor for t in theoretical_curve]

    # Plot erstellen
    plt.figure(figsize=(10, 6))
    plt.plot(list_sizes, times, marker="o", linestyle="-", label="Gemessene Zeit")
    plt.plot(
        list_sizes,
        theoretical_curve_scaled,
        linestyle="--",
        color="red",
        label="Theorie: O(n log n)",
    )

    plt.title("Merge Sort Zeitkomplexität")
    plt.xlabel("Listenlänge n (logarithmisch skaliert)")
    plt.ylabel("Zeit (Sekunden)")
    plt.xscale("log", base=2)  # X-Achse log2 skalieren, da wir Potenzen von 2 nutzen
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    measure_complexity()
