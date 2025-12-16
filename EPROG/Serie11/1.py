import time
import random
import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)
    # Durchlaufe alle Array-Elemente
    for i in range(n):
        # Die letzten i Elemente sind bereits sortiert
        for j in range(0, n - i - 1):
            # Tausche, wenn das gefundene Element größer ist als das nächste
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def measure_complexity():
    # Listenlängen von 2 (2 elemente können unsortiert sein) bis n
    n = (10**3) + 1
    list_sizes = range(2, n, 10)
    times = []

    for size in list_sizes:
        # Zufällige Liste generieren
        test_list = [random.randint(0, 10000) for _ in range(size)]

        start_time = time.time()
        bubble_sort(test_list)
        end_time = time.time()

        duration = end_time - start_time
        times.append(duration)
        print(f"Größe: {size}, Zeit: {duration:.6f} Sekunden")

    # Plot erstellen
    plt.figure(figsize=(10, 6))
    plt.plot(list_sizes, times, marker="o", linestyle="-")
    plt.title("Bubble Sort Zeitkomplexität")
    plt.xlabel("Listenlänge (Anzahl der Elemente)")
    plt.ylabel("Zeit (Sekunden)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    measure_complexity()
