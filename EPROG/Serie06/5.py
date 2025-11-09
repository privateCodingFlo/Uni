import copy  # Wird benötigt, um Matrizen sicher zu kopieren


def get_submatrix(matrix, j):
    """
    Erzeugt die Untermatrix M_1j durch Entfernen der ersten Zeile und der j-ten Spalte
    der gegebenen Matrix.

    matrix: Die quadratische Matrix (Liste von Listen).
    j: Der Spaltenindex (0-basiert), der entfernt werden soll.
    """
    # Erstelle eine Kopie der Matrix (ohne die erste Zeile)
    # Die erste Zeile [0] wird entfernt, da wir die Laplace-Entwicklung nach dieser durchführen.
    sub_matrix = copy.deepcopy(matrix[1:])

    # Iteriere über die verbleibenden Zeilen der Untermatrix
    for row in sub_matrix:
        # Entferne das Element an der j-ten Spalte (Index j) aus jeder Zeile
        row.pop(j)

    return sub_matrix


def determinante(matrix):
    """
    Berechnet die Determinante einer quadratischen Matrix rekursiv
    mittels Laplace-Entwicklung nach der ersten Zeile.

    matrix: Die quadratische Matrix (Liste von Listen).
    """
    n = len(matrix)

    # 1. BASENFALL (Abbruchbedingung der Rekursion)
    # Für eine 1x1 Matrix A = [a_11] ist det(A) = a_11.
    if n == 1:
        return matrix[0][0]

    det = 0

    # 2. REKURSIVER SCHRITT
    # Iteriere über die Spalten der ersten Zeile (Index j von 0 bis n-1)
    for j in range(n):
        # a_1j ist das Element in der ersten Zeile (Index 0) und der aktuellen Spalte (Index j)
        a_1j = matrix[0][j]

        # Berechne den Kofaktor(-Vorzeichen): (-1)^(1+j)
        # Da unsere Indizierung bei 0 beginnt (0, 1, 2, ...), ist das Vorzeichen (-1)^(0+j) = (-1)^j.
        # Im Python-Code: Wenn j gerade ist, ist (-1)^j = +1. Wenn j ungerade ist, ist (-1)^j = -1.
        # Alternativ: (-1)**(1 + (j+1)) = (-1)**(j+2)
        sign = (-1)**(j)

        # Ermittle die Untermatrix M_1j (entsteht durch Streichen der ersten Zeile und j-ten Spalte)
        M_1j = get_submatrix(matrix, j)

        # Addiere den Term zum Gesamtergebnis: sign * a_1j * det(M_1j)
        # Hier erfolgt der REKURSIVE AUFRUF der Funktion determinante()
        det += sign * a_1j * determinante(M_1j)

    return det

# --- Test-Beispiele ---


# 1. 2x2 Matrix (Det = ad - bc)
A_2x2 = [
    [4, 6],
    [3, 8]
]
# Erwartet: 4*8 - 6*3 = 32 - 18 = 14
det_2x2 = determinante(A_2x2)

# 2. 3x3 Matrix
A_3x3 = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]
# Erwartet (Laplace nach 1. Zeile):
# +1 * 1 * det([1, 4; 6, 0])  -> 1 * (1*0 - 4*6) = -24
# -1 * 2 * det([0, 4; 5, 0])  -> -2 * (0*0 - 4*5) = -2 * (-20) = +40
# +1 * 3 * det([0, 1; 5, 6])  -> +3 * (0*6 - 1*5) = +3 * (-5) = -15
# Gesamt: -24 + 40 - 15 = 1
det_3x3 = determinante(A_3x3)


# --- Ausgabe ---
print("--- Aufgabe 5: Rekursive Determinante ---")
print(f"Matrix 2x2:\n{A_2x2}")
print(f"Determinante: {det_2x2}")
print("-" * 30)
print(f"Matrix 3x3:\n{A_3x3}")
print(f"Determinante: {det_3x3}")
print("-" * 30)
