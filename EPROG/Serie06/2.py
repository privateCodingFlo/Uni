def LxV(L, vector):
    """
    Berechnet das Produkt einer unteren Dreiecksmatrix L (als verschachtelte Liste)
    mit einem Vektor v (als Liste) und gibt das Ergebnis y = L * v zurück.

    L: Untere Dreiecksmatrix (Liste von Listen)
    vector: Vektor v (Liste)

    Die Berechnung erfolgt nur für die Elemente, bei denen der Spaltenindex j
    kleiner oder gleich dem Zeilenindex i ist (y_i = Summe_{j=1}^{i} L_ij * v_j).
    """

    n = len(L)
    # 1. Überprüfen der Kompatibilität (quadratische Matrix und korrekte Vektorlänge)
    if n != len(vector) or any(len(row) != n for row in L):
        raise ValueError(
            "Matrix L muss quadratisch sein und ihre Dimension muss der Länge des Vektors entsprechen.")

    # 2. Initialisieren des Ergebnisvektors y mit Nullen
    y = [0] * n

    # 3. Schleife über die Zeilen der Matrix L (entspricht dem Index i in y_i)
    for i in range(n):
        sum_val = 0

        # 4. Schleife über die Spalten der Matrix L (entspricht dem Index j in L_ij)
        # Die Summe läuft von j=0 bis j=i (n-1 in der 0-basierten Indexierung),
        # wodurch die Nulleinträge oberhalb der Diagonalen (j > i) ignoriert werden.
        # Dies erfüllt die Anforderung, nicht auf offensichtliche Null-Einträge zuzugreifen.
        for j in range(i + 1):
            # Berechnung des Terms L_ij * v_j und Aufsummieren
            sum_val += L[i][j] * vector[j]

        # 5. Speichern des berechneten Elements y_i
        y[i] = sum_val

    return y


# --- Beispiel ---
# Untere Dreiecksmatrix L (3x3)
L_test = [
    [4, 0, 0],
    [2, 5, 0],
    [1, 3, 6]
]

# Vektor v
v_test = [10, 2, 5]

# Berechnung: y = L * v
result_y = LxV(L_test, v_test)


# sprich es kommt folgendes raus:
# result_y[0] = v_test[0] * L_test[0][0]
# result_y[1] = v_test[0] * L_test[1][0] + v_test[1] * L_test[1][1]
# result_y[1] = v_test[0] * L_test[2][0] + v_test[1] * L_test[2][1] + v_test[2] * L_test[2][2]

print(f"Matrix L:\t\t{L_test}")
print(f"Vektor v:\t\t{v_test}")
print(f"Ergebnis y = L * v:\t{result_y}")
