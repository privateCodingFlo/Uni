import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import os

# 1. Pfad zur Datei dynamisch bestimmen
# 'os.path.dirname(__file__)' gibt den Ordner an, in dem dieses Skript gespeichert ist
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'vertices.npy')

# 2. Datei laden [cite: 34, 35]
try:
    vertices = np.load(file_path)
    print(f"Datei erfolgreich geladen von: {file_path}")
except FileNotFoundError:
    print(f"FEHLER: Die Datei wurde nicht gefunden unter: {file_path}")
    # Fallback für Testzwecke
    vertices = np.array([[0, 0], [2, 0], [2, 2], [1, 3], [0, 2]])

# 3. Bounding Box für Zufallspunkte bestimmen
x_min, y_min = vertices.min(axis=0)
x_max, y_max = vertices.max(axis=0)

# 4. Monte-Carlo Methode anwenden [cite: 35, 36]
n_points = 50000
points = np.random.uniform([x_min, y_min], [x_max, y_max], size=(n_points, 2))

# Prüfen, welche Punkte im Polygon liegen
poly_path = Path(vertices)
inside = poly_path.contains_points(points)

# Flächenberechnung: (Fläche der Box) * (Anteil der Treffer) [cite: 35, 36]
box_area = (x_max - x_min) * (y_max - y_min)
poly_area = box_area * np.sum(inside) / n_points

# 5. Visualisierung mit matplotlib [cite: 37]
plt.figure(figsize=(8, 8))
plt.scatter(points[inside, 0], points[inside, 1], s=1,
            color='blue', alpha=0.4, label='Inside')
plt.scatter(points[~inside, 0], points[~inside, 1], s=1,
            color='lightgray', alpha=0.2, label='Outside')

# Polygon-Umriss zeichnen
polygon_closed = np.vstack([vertices, vertices[0]])  # Schließt das Polygon
plt.plot(polygon_closed[:, 0], polygon_closed[:, 1],
         'r-', linewidth=2, label='Polygon Border')

plt.title(f"Monte-Carlo Flächenberechnung\nGeschätzte Fläche: {poly_area:.4f}")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
