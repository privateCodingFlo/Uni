import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_tic_tac_toe(board):
    """
    Visualisiert ein Tic-Tac-Toe Spielfeld.
    board: 3x3 Matrix (Liste von Listen) mit Einträgen "", "x", "o".
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    # Achsen-Grenzen und Aspekt
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_aspect("equal")

    # Raster zeichnen
    # Vertikale Linien
    ax.plot([1, 1], [0, 3], color="black", linewidth=2)
    ax.plot([2, 2], [0, 3], color="black", linewidth=2)
    # Horizontale Linien
    ax.plot([0, 3], [1, 1], color="black", linewidth=2)
    ax.plot([0, 3], [2, 2], color="black", linewidth=2)

    # Symbole zeichnen
    # Koordinatensystem: (0,0) ist links unten.
    # Zeilenindex i: 0 ist oben, 2 ist unten -> y = 2.5, 1.5, 0.5
    # Spaltenindex j: 0 ist links, 2 ist rechts -> x = 0.5, 1.5, 2.5

    for i in range(3):
        for j in range(3):
            symbol = board[i][j]
            symbol = symbol.lower()

            # Zentrum des Feldes berechnen
            center_x = j + 0.5
            center_y = (2 - i) + 0.5

            if symbol == "o":
                # Kreis zeichnen
                circle = patches.Circle(
                    (center_x, center_y),
                    radius=0.3,
                    edgecolor="blue",
                    facecolor="none",
                    linewidth=3,
                )
                ax.add_patch(circle)

            elif symbol == "x":
                # Rechteck (Quadrat) zeichnen
                # Ankerpunkt (unten links) berechnen für zentriertes Quadrat
                side_length = 0.6
                rect_x = center_x - side_length / 2
                rect_y = center_y - side_length / 2

                rect = patches.Rectangle(
                    (rect_x, rect_y),
                    side_length,
                    side_length,
                    edgecolor="red",
                    facecolor="none",
                    linewidth=3,
                )
                ax.add_patch(rect)

                # Alternativ: Ein "X" zeichnen (falls Rechteck zu langweilig ist, aber Aufgabe sagt Rechteck)
                # ax.plot([center_x - 0.3, center_x + 0.3], [center_y - 0.3, center_y + 0.3], 'r-', linewidth=3)
                # ax.plot([center_x - 0.3, center_x + 0.3], [center_y + 0.3, center_y - 0.3], 'r-', linewidth=3)

    # Achsen verstecken
    ax.axis("off")

    plt.title("Tic-Tac-Toe")
    plt.show()


if __name__ == "__main__":
    # Test-Spielfeld
    test_board = [["x", "o", "x"], ["", "x", "o"], ["o", "", ""]]

    draw_tic_tac_toe(test_board)
