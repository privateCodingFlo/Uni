import math
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------------------------------
# 1. MAZE-DEFINITION UND INITIALISIERUNG
# --------------------------------------------------------------------------------------------------

# WICHTIG: Die Variable n wird für die Visualisierungsfunktion benötigt
n = 10
# Erstelle ein leeres Gitter (0 = freier Weg)
maze = [[0] * n for _ in range(n)]

# Definiere die Wände (1 = Wand)
walls = [(2, 8), (0, 9), (1, 7), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 2),
         (4, 2), (7, 2), (6, 2), (8, 2), (4, 7), (5, 1), (5, 2), (5, 3), (5, 4),
         (5, 5), (5, 6), (5, 7), (6, 2), (6, 6), (7, 6), (3, 5), (7, 4), (8, 4),
         (9, 4), (8, 6), (8, 7), (8, 8), (5, 0)]

# Setze die Wände im Gitter
for (x, y) in walls:
    if 0 <= x < n and 0 <= y < n:
        maze[x][y] = 1

# Start- und Zielkoordinaten
start = (8, 1)
goal = (3, 4)

# --------------------------------------------------------------------------------------------------
# 2. VISUALISIERUNGSFUNKTION (Matplotlib-Version aus der Aufgabenstellung)
# --------------------------------------------------------------------------------------------------

# Achtung: Die Funktion verwendet die global definierten Variablen 'n' und 'walls'.


def print_maze(maze, path=None, start=None, goal=None, dist=None):
    """Visualisiert das Gitter, Wände, Start/Ziel, Pfad und Distanzen."""

    # Hintergrund: Wände und Gitterrand
    plt.scatter([x for (x, y) in walls], [y for (x, y) in walls],
                color='lightblue', marker='s', s=600)
    plt.plot([-0.5, n-0.5, n-0.5, -0.5, -0.5], [-0.5, -0.5, n -
             0.5, n-0.5, -0.5], color='lightblue', linewidth=3)

    # Pfad
    if path:
        plt.plot([x for (x, y) in path], [y for (x, y) in path],
                 color='orange', linewidth=3)

    # Ziel
    if goal:
        plt.scatter(goal[0], goal[1], color='red', marker='*', s=200)

    # Start
    if start:
        plt.scatter(start[0], start[1], color='orange', marker='o', s=200)

    # Distanzen
    if dist:
        for i in range(n):
            for j in range(n):
                # Zeige Distanzen nur auf freiem Weg, wo die Distanz nicht unendlich ist
                if maze[i][j] == 0 and dist[i][j] < float('inf'):
                    # Formatiere die Distanz auf eine Dezimalstelle für bessere Lesbarkeit
                    plt.text(i, j, str(
                        round(dist[i][j], 1)), color='black', fontsize=12, ha='center', va='center')

    plt.xlim(-1, n)
    plt.ylim(-1, n)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


# --------------------------------------------------------------------------------------------------
# 3. ERWEITERTE LOGIK FÜR DIAGONALE SCHRITTE
# --------------------------------------------------------------------------------------------------

# Konstante für die Kosten eines diagonalen Schritts
COST_DIAGONAL = math.sqrt(2)

# Definiert alle 8 möglichen Nachbarn und die zugehörigen Kosten
NEIGHBORS = [
    # Horizontal/Vertikal (Kosten 1.0)
    (0,  1, 1.0), (0, -1, 1.0),
    (1,  0, 1.0), (-1,  0, 1.0),
    # Diagonal (Kosten Wurzel(2))
    (1,  1, COST_DIAGONAL), (-1,  1, COST_DIAGONAL),
    (1, -1, COST_DIAGONAL), (-1, -1, COST_DIAGONAL)
]


def update(dist, pred, x, y, nx, ny, cost):
    """
    Erweiterte Funktion update() zur Aktualisierung von Distanz und Vorgänger.
    """
    # Neue Distanz = Distanz zum aktuellen Knoten + Kosten des Schritts
    new_dist = dist[x][y] + cost

    # Wenn der neue Weg kürzer ist, aktualisiere die Daten
    if new_dist < dist[nx][ny]:
        dist[nx][ny] = new_dist
        pred[nx][ny] = (x, y)


def find_shortest_path(maze, start, goal):
    """
    Findet den kürzesten Pfad mit einem Dijkstra-ähnlichen Ansatz 
    (durch Scannen aller unbesuchten Knoten, da keine Queue verwendet wird).
    """
    N = len(maze)
    dist = [[float('inf')] * N for _ in range(N)]
    pred = [[None] * N for _ in range(N)]

    # Set aller Koordinaten, die noch nicht optimal besucht wurden
    unvisited_nodes = set([(x, y) for x in range(N) for y in range(N)])

    # Initialisiere Startpunkt
    start_x, start_y = start
    dist[start_x][start_y] = 0.0

    while unvisited_nodes:
        # 1. Finde den unbesuchten Knoten mit der kleinsten Distanz (ersetzt die Priority Queue)
        min_dist = float('inf')
        current_node = None

        for x, y in unvisited_nodes:
            if dist[x][y] < min_dist:
                min_dist = dist[x][y]
                current_node = (x, y)

        # Abbruch, wenn kein erreichbarer Knoten mehr übrig ist
        if current_node is None:
            break

        x, y = current_node

        # Ziel erreicht?
        if (x, y) == goal:
            break

        # Markiere als besucht
        unvisited_nodes.remove(current_node)

        # 2. Durchlaufe alle 8 Nachbarn (Entspannungs-Schritt)
        for dx, dy, cost in NEIGHBORS:
            nx, ny = x + dx, y + dy

            # Prüfe Gültigkeit: Im Gitter und kein Hindernis
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] == 0:
                update(dist, pred, x, y, nx, ny, cost)

    # 3. Pfadrekonstruktion
    path = []
    current = goal

    while current and current != start:
        path.append(current)
        if pred[current[0]][current[1]] is None:  # Prüfe, ob das Ziel erreichbar war
            return None, dist

        px, py = pred[current[0]][current[1]]
        current = (px, py)

    if current == start:
        path.append(start)
        path.reverse()
        return path, dist

    return None, dist


# --------------------------------------------------------------------------------------------------
# 4. AUSFÜHRUNG UND VISUALISIERUNG
# --------------------------------------------------------------------------------------------------

# Finde den kürzesten Pfad
shortest_path, dist_matrix = find_shortest_path(maze, start, goal)

print("## Lösung Aufgabe 6: Kürzester Weg mit diagonalen Schritten (Visualisierung mit Matplotlib)")
print("-----------------------------------------------------------------------------------------")
print(f"Start: {start}, Ziel: {goal}")

if shortest_path:
    print(
        f"Kürzester Pfad gefunden. Gesamtkosten: {dist_matrix[goal[0]][goal[1]]:.4f}")

    # 1. Visualisierung mit Matplotlib
    print("\nVisualisierung wird jetzt in einem separaten Fenster angezeigt...")
    print_maze(maze, shortest_path, start, goal, dist_matrix)

    # 2. Ausgabe des Pfades als Text
    print("\nAblauf des kürzesten Pfades (Koordinaten und Kosten):")
    for i in range(len(shortest_path) - 1):
        x1, y1 = shortest_path[i]
        x2, y2 = shortest_path[i+1]

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        kosten = 1.0 if dx == 0 or dy == 0 else COST_DIAGONAL
        typ = "horizontal/vertikal" if dx == 0 or dy == 0 else "diagonal"

        print(
            f"  {i+1}. Zug: ({x1}, {y1}) -> ({x2}, {y2}) | Kosten: {kosten:.4f} ({typ})")

else:
    print("Es konnte kein Pfad zwischen Start und Ziel gefunden werden.")
