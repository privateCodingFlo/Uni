def back_substitution(U, b):
    """
    Löst das lineare Gleichungssystem U*x = b mittels Rückwärtseinsetzen, 
    wobei U eine obere Dreiecksmatrix ist. 

    Diese Implementierung verwendet NUR Standard-Python-Listen.

    :param U: Die obere Dreiecksmatrix (Liste von Listen).
    :param b: Der rechte Seite Vektor (Liste von Zahlen).
    :return: Der Lösungsvektor x (Liste von Zahlen).
    :raises ValueError: Wenn U keine quadratische Matrix ist, Dimensionen nicht passen oder b keine Liste ist.
    :raises ZeroDivisionError: Wenn ein Diagonalelement von U null ist.
    """

    # 1. Dimensionen und Typen prüfen

    if not isinstance(b, list) or not all(isinstance(val, (int, float)) for val in b):
        raise TypeError(
            "Vektor b muss eine Liste von Zahlen (int/float) sein.")

    n = len(b)

    if not isinstance(U, list) or len(U) != n:
        raise ValueError(f"Matrix U muss {n} Zeilen haben.")

    # Prüfen, ob U quadratisch ist (n x n)
    for row in U:
        if not isinstance(row, list) or len(row) != n:
            raise ValueError(f"Matrix U muss quadratisch ({n}x{n}) sein.")

    # Initialisierung des Lösungsvektors x
    x = [0.0] * n

    # 2. Berechnung des letzten Elements x_n (Index n-1)

    # Fehlerbehandlung: Division durch Null
    u_nn = U[n-1][n-1]
    if u_nn == 0:
        raise ZeroDivisionError(
            f"Diagonalelement u_{n}{n} ist null. Das System hat keine eindeutige Lösung.")

    x[n-1] = b[n-1] / u_nn

    # 3. Berechnung der restlichen Elemente von x_{n-1} bis x_1
    # Iteration von i = n-2 (letzte Zeile) bis 0 (erste Zeile)
    for i in range(n - 2, -1, -1):

        b_i = b[i]

        # Berechnung der Summe: Sum_{j=i+1}^{n} u_{ij} * x_j
        sum_val = 0.0
        # J geht von i+1 bis n-1
        for j in range(i + 1, n):
            # U[i][j] * x[j]
            sum_val += U[i][j] * x[j]

        # Fehlerbehandlung: Division durch Null
        u_ii = U[i][i]
        if u_ii == 0:
            # i+1 ist die 1-basierte Zeilennummer
            raise ZeroDivisionError(
                f"Diagonalelement u_{i+1}{i+1} ist null. Das System hat keine eindeutige Lösung.")

        # x_i = (1 / u_{ii}) * (b_i - Summe)
        x[i] = (b_i - sum_val) / u_ii

    return x


U_test = [
    [2.0, 1.0, 3.0],
    [0.0, 4.0, 2.0],
    [0.0, 0.0, 5.0]
]
b_test = [10.0, 8.0, 15.0]

try:
    x_solution = back_substitution(U_test, b_test)
    print("\n--- Erfolgreiche Lösung ---")
    print(f"Matrix U: {U_test}")
    print(f"Vektor b: {b_test}")
    # Erwartetes Ergebnis: x = [1, 1, 3]
    print(f"Lösungsvektor x: {x_solution}")

    # Manuelle Überprüfung des Ergebnisses (ohne numpy)
    print("\nManuelle Überprüfung (U * x):")
    for i in range(len(U_test)):
        result = 0.0
        for j in range(len(U_test)):
            result += U_test[i][j] * x_solution[j]
        # Sollte 10.0, 8.0, 15.0 ergeben
        print(f"  Zeile {i+1} Ergebnis: {result:.1f}")

except Exception as e:
    print(f"Fehler bei der Berechnung: {e}")
