import math
import matplotlib.pyplot as plt
import heapq  # Modul für die Priority Queue (Min-Heap)

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


def print_maze(maze, path=None, start=None, goal=None, dist=None, title=""):
    """Visualisiert das Gitter, Wände, Start/Ziel, Pfad und Distanzen."""

    plt.figure(figsize=(8, 8))
    plt.title(title)

    # Hintergrund: Wände und Gitterrand
    plt.scatter([x for (x, y) in walls], [y for (x, y) in walls],
                color='lightblue', marker='s', s=600)
    plt.plot([-0.5, n-0.5, n-0.5, -0.5, -0.5], [-0.5, -0.5, n -
             0.5, n-0.5, -0.5], color='lightblue', linewidth=3)

    # Pfad
    if path:
        plt.plot([x for (x, y) in path], [y for (x, y) in path],
                 color='orange', linewidth=3, zorder=10)

    # Ziel
    if goal:
        plt.scatter(goal[0], goal[1], color='red',
                    marker='*', s=300, zorder=11)

    # Start
    if start:
        plt.scatter(start[0], start[1], color='green',
                    marker='o', s=300, zorder=11)

    # Distanzen
    if dist:
        for i in range(n):
            for j in range(n):
                if maze[i][j] == 0 and dist[i][j] < float('inf'):
                    # Formatiere die Distanz auf eine Dezimalstelle
                    plt.text(i, j, str(
                        round(dist[i][j], 1)), color='black', fontsize=10, ha='center', va='center')

    plt.xlim(-1, n)
    plt.ylim(-1, n)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True, which='both', color='gray', linestyle='-', linewidth=0.5)
    plt.xticks(range(n))
    plt.yticks(range(n))
    plt.show()

# --------------------------------------------------------------------------------------------------
# 3. HELFER FUNKTIONEN UND KONSTANTEN
# --------------------------------------------------------------------------------------------------


COST_DIAGONAL = math.sqrt(2)

# Definiert alle 8 möglichen Nachbarn und die zugehörigen Kosten
NEIGHBORS = [
    # Horizontal/Vertikal (Kosten 1.0)
    (0, 1, 1.0), (0, -1, 1.0),
    (1, 0, 1.0), (-1, 0, 1.0),
    # Diagonal (Kosten Wurzel(2))
    (1, 1, COST_DIAGONAL), (-1, 1, COST_DIAGONAL),
    (1, -1, COST_DIAGONAL), (-1, -1, COST_DIAGONAL)
]


def heuristic(node, goal):
    """
    Heuristik h(n): Euklidische Distanz vom Knoten n zum Ziel.
    """
    x, y = node
    gx, gy = goal

    # Euklidische Distanz
    return math.sqrt((gx - x)**2 + (gy - y)**2)


def reconstruct_path(start, goal, pred):
    """Rekonstruiert den Pfad vom Ziel zurück zum Start."""
    path = []
    current = goal

    while current and current != start:
        path.append(current)
        if pred[current[0]][current[1]] is None:
            return None

        px, py = pred[current[0]][current[1]]
        current = (px, py)

    if current == start:
        path.append(start)
        path.reverse()
        return path

    return None

# --------------------------------------------------------------------------------------------------
# 4. DIJKSTRA-ALGORITHMUS MIT PRIORITY QUEUE
# --------------------------------------------------------------------------------------------------


def find_shortest_path_dijkstra(maze, start, goal):
    """
    Dijkstra-Algorithmus unter Verwendung einer Priority Queue. 
    Priorität ist die tatsächliche Distanz g(n).
    """
    N = len(maze)
    # g_score: Tatsächliche Kosten vom Start zum Knoten n
    g_score = [[float('inf')] * N for _ in range(N)]
    pred = [[None] * N for _ in range(N)]

    # Priority Queue: Speichert (Distanz, x, y)
    open_list = [(0.0, start[0], start[1])]
    g_score[start[0]][start[1]] = 0.0

    while open_list:
        # Extrahiere den Knoten mit der kleinsten g-Distanz
        g_current, x, y = heapq.heappop(open_list)

        # Ignoriere, falls wir einen längeren Weg zu diesem Knoten gefunden haben
        if g_current > g_score[x][y]:
            continue

        if (x, y) == goal:
            break

        for dx, dy, cost in NEIGHBORS:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] == 0:

                temp_g_score = g_score[x][y] + cost

                if temp_g_score < g_score[nx][ny]:
                    # Update g_score und Vorgänger
                    g_score[nx][ny] = temp_g_score
                    pred[nx][ny] = (x, y)

                    # Füge zur Priority Queue hinzu
                    heapq.heappush(open_list, (temp_g_score, nx, ny))

    return reconstruct_path(start, goal, pred), g_score

# --------------------------------------------------------------------------------------------------
# 5. A*-ALGORITHMUS MIT PRIORITY QUEUE
# --------------------------------------------------------------------------------------------------


def find_shortest_path_a_star(maze, start, goal):
    """
    A*-Algorithmus unter Verwendung einer Priority Queue. 
    Priorität ist die geschätzte Gesamtkosten f(n) = g(n) + h(n).
    """
    N = len(maze)
    g_score = [[float('inf')] * N for _ in range(N)]
    pred = [[None] * N for _ in range(N)]

    # Priority Queue: Speichert (f_score, x, y)
    start_h = heuristic(start, goal)
    # f(start) = g(start)+h(start) = 0 + h(start)
    open_list = [(start_h, start[0], start[1])]
    g_score[start[0]][start[1]] = 0.0

    while open_list:
        # Extrahiere den Knoten mit der kleinsten f-Distanz
        f_current, x, y = heapq.heappop(open_list)

        # Ignoriere, falls wir einen längeren Weg zu diesem Knoten gefunden haben
        # Da wir nur g(n) speichern, benötigen wir diesen Check.
        if f_current > g_score[x][y] + heuristic((x, y), goal):
            continue

        if (x, y) == goal:
            break

        for dx, dy, cost in NEIGHBORS:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] == 0:

                temp_g_score = g_score[x][y] + cost

                if temp_g_score < g_score[nx][ny]:
                    # Update g_score und Vorgänger
                    g_score[nx][ny] = temp_g_score
                    pred[nx][ny] = (x, y)

                    # Berechne f(n) = g(n) + h(n) für den Nachbarn
                    f_score_neighbor = temp_g_score + heuristic((nx, ny), goal)

                    # Füge zur Priority Queue hinzu
                    heapq.heappush(open_list, (f_score_neighbor, nx, ny))

    return reconstruct_path(start, goal, pred), g_score


# --------------------------------------------------------------------------------------------------
# 6. AUSFÜHRUNG BEIDER ALGORITHMEN UND VERGLEICH
# --------------------------------------------------------------------------------------------------

print("## 🧪 Vergleich: Dijkstra vs. A* (A-Stern) mit Priority Queue")
print("-----------------------------------------------------------------------------------------")
print(f"Start: {start}, Ziel: {goal}")

# --- DIJKSTRA ---
print("\n--- A) DIJKSTRA-ALGORITHMUS ---")
path_d, dist_d = find_shortest_path_dijkstra(maze, start, goal)

if path_d:
    cost_d = dist_d[goal[0]][goal[1]]
    print(f"Kürzester Pfad (Dijkstra) gefunden. Gesamtkosten: {cost_d:.4f}")
    print_maze(maze, path_d, start, goal, dist_d,
               title=f"Dijkstra Pfad (Kosten: {cost_d:.2f})")
else:
    print("Dijkstra: Es konnte kein Pfad gefunden werden.")


# --- A* ---
print("\n--- B) A*-ALGORITHMUS ---")
path_a, dist_a = find_shortest_path_a_star(maze, start, goal)

if path_a:
    cost_a = dist_a[goal[0]][goal[1]]
    print(f"Kürzester Pfad (A*) gefunden. Gesamtkosten: {cost_a:.4f}")
    # g(n) (dist_a) wird visualisiert, um die tatsächliche Distanz zu zeigen.
    print_maze(maze, path_a, start, goal, dist_a,
               title=f"A* Pfad (Kosten: {cost_a:.2f})")
else:
    print("A*: Es konnte kein Pfad gefunden werden.")
