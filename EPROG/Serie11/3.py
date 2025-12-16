import time
import random
import sys
import matplotlib.pyplot as plt

# Rekursionslimit erhöhen, da Worst-Case QuickSort eine Tiefe von O(n) erreicht
sys.setrecursionlimit(20000)


def quicksort(arr):
    """
    Standard Pseudo-Code Implementierung von QuickSort (Pivot = erstes Element).
    Dies führt zu O(n^2), wenn die Liste bereits sortiert oder umgekehrt sortiert ist.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    # Aufteilung in Elemente kleiner, gleich und größer als Pivot
    # Achtung: Wir müssen 'gleich' separat behandeln oder sicherstellen, dass Pivot nicht im rekursiven Aufruf landet,
    # um Endlosschleifen zu vermeiden. Hier: elements < pivot, elements > pivot.
    # Das Pivot-Element selbst ist bereits "sortiert" an seiner Position.

    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


def measure_complexity():
    # Wir benutzen kleinere n für den Worst-Case Vergleich, da O(n^2) schnell wächst
    # n bis ca. 500-1000, um nicht zu lange zu warten
    sizes = range(10, 800, 50)

    times_random = []
    times_sorted = []
    times_reverse = []

    print("Starte Messung...")
    for n in sizes:
        # 1. Zufällige Liste (Average Case: O(n log n))
        list_random = [random.randint(0, 10000) for _ in range(n)]

        # 2. Sortierte Liste (Worst Case: O(n^2))
        list_sorted = list(range(n))

        # 3. Umgekehrt sortierte Liste (Worst Case: O(n^2))
        list_reverse = list(range(n, 0, -1))

        # Messung Random
        start = time.time()
        quicksort(list_random)
        times_random.append(time.time() - start)

        # Messung Sorted (Worst Case)
        start = time.time()
        quicksort(list_sorted)
        times_sorted.append(time.time() - start)

        # Messung Reverse (Worst Case)
        start = time.time()
        quicksort(list_reverse)
        times_reverse.append(time.time() - start)

        print(f"n={n} gemessen.")

    # Plotting
    plt.figure(figsize=(10, 6))

    # Gemessene Kurven
    plt.plot(sizes, times_random, label="Average Case (Random Input)", marker="o")
    plt.plot(sizes, times_sorted, label="Worst Case (Sorted Input)", marker="x")
    plt.plot(
        sizes, times_reverse, label="Worst Case (Reverse Sorted Input)", marker="s"
    )

    # Quadratische Referenzkurve zum Vergleich (skaliert auf den letzten Wert der Worst-Case Kurve)
    # y = c * x^2
    ref_y = [x**2 for x in sizes]
    scale = times_sorted[-1] / ref_y[-1]
    ref_y_scaled = [y * scale for y in ref_y]
    plt.plot(sizes, ref_y_scaled, "--", color="gray", alpha=0.5, label="Referenz O(n²)")

    plt.title("QuickSort Laufzeitanalyse: Worst Case vs Average Case")
    plt.xlabel("Listenlänge n")
    plt.ylabel("Zeit (Sekunden)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    measure_complexity()
