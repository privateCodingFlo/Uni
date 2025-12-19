import numpy as np
import matplotlib.pyplot as plt
import os


def process_and_plot_data():
    # 1. Datei laden
    try:
        # Die Datei befindet sich im gleichen Verzeichnis
        file_path = os.path.dirname(__file__) + "/xy1d.npy"
        data = np.load(file_path)
        print(f"Daten erfolgreich geladen. Form (Shape) der Rohdaten: {data.shape}")

        # 2. Reshape der Daten
        # Die Daten sind in der Form [x0, y0, x1, y1, ...]
        # Wir wollen Paare (x, y), also eine Matrix mit N Zeilen und 2 Spalten
        reshaped_data = data.reshape(-1, 2)
        print(f"Daten nach reshape(-1, 2): {reshaped_data.shape}")

        # Extrahieren von x und y für den Plot
        x_coords = reshaped_data[:, 0]
        y_coords = reshaped_data[:, 1]

        # 3. Plotten
        plt.figure(figsize=(8, 8))
        plt.plot(x_coords, y_coords, marker="o", linestyle="-", markersize=2)

        # 4. Axen skalieren
        plt.axis("equal")

        # Tuning
        plt.title("Plot der Daten aus xy1d.npy")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)

        plt.show()

    except FileNotFoundError:
        print(f"Fehler: Die Datei '{file_path}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


if __name__ == "__main__":
    process_and_plot_data()
