class Matrix:
    """
    Klasse zur Repräsentierung von Matrizen in R^(n x m).
    Implementiert Matrix-Addition (+) und Matrix-Multiplikation (*).
    """

    def __init__(self, data):
        """
        Konstruktor: Initialisiert die Matrix aus einer verschachtelten Liste.
        data: Eine verschachtelte Liste von Zahlen.
        """
        if not data or not isinstance(data, list):
            raise ValueError(
                "Matrix-Daten müssen eine nicht-leere Liste von Listen sein.")

        self.data = data
        self.rows = len(data)

        # Sicherstellen, dass die Matrix nicht leer ist und die Spaltenanzahl konsistent ist
        if self.rows == 0:
            self.cols = 0
        else:
            self.cols = len(data[0])
            # Prüfen, ob alle Zeilen die gleiche Länge haben (konsistente Spaltenanzahl)
            for row in data:
                if len(row) != self.cols:
                    raise ValueError(
                        "Alle Zeilen der Matrix müssen die gleiche Spaltenanzahl haben.")

    # --- Magic Methods für Darstellung und String-Repräsentation ---

    def __str__(self):
        """Informelle String-Repräsentation (für print())."""
        s = '[\n'
        for row in self.data:
            # Stellt die Zeilen in einer gut lesbaren Form dar
            s += '  ' + ' '.join(f'{x:6.2f}' for x in row) + '\n'
        s += ']'
        return s

    def __repr__(self):
        """Offizielle String-Repräsentation (für Debugging)."""
        return f"Matrix({self.data})"

    # --- Magic Method für Matrix-Addition (+) ---

    def __add__(self, other):
        """
        Implementiert die Matrix-Addition: self + other.
        Voraussetzung: Die Matrizen müssen die gleichen Dimensionen (n x m) haben.
        """
        if not isinstance(other, Matrix):
            return NotImplemented

        # Fehlerbehandlung: Ungleiche Dimensionen
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Dimensionen stimmen für Addition nicht überein. "
                f"({self.rows}x{self.cols} + {other.rows}x{other.cols} erwartet {self.rows}x{self.cols})"
            )

        # Durchführung der Addition
        result_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                # Addiert die entsprechenden Elemente
                new_row.append(self.data[i][j] + other.data[i][j])
            result_data.append(new_row)

        return Matrix(result_data)

    # --- Magic Method für Matrix-Multiplikation (*) ---

    def __mul__(self, other):
        """
        Implementiert die Matrix-Multiplikation: self * other.
        Voraussetzung: self.cols muss gleich other.rows sein.
        """
        if not isinstance(other, Matrix):
            return NotImplemented

        # Fehlerbehandlung: Ungültige Dimensionen für Multiplikation
        # Matrix A (n x m) * Matrix B (m x k) -> Ergebnis (n x k)
        if self.cols != other.rows:
            raise ValueError(
                f"Dimensionen stimmen für Multiplikation nicht überein. "
                f"({self.rows}x{self.cols} * {other.rows}x{other.cols} erwartet {self.cols} == {other.rows})"
            )

        # Durchführung der Multiplikation
        C_rows = self.rows
        C_cols = other.cols

        result_data = [[0 for _ in range(C_cols)] for _ in range(C_rows)]

        # Standard-Matrix-Multiplikations-Algorithmus (Dot-Product)
        for i in range(C_rows):          # i über Zeilen von A (Ergebnis)
            for j in range(C_cols):      # j über Spalten von B (Ergebnis)
                summe = 0
                for k in range(self.cols):  # k über Spalten von A und Zeilen von B
                    summe += self.data[i][k] * other.data[k][j]
                result_data[i][j] = summe

        return Matrix(result_data)


# 1. Matrizen erstellen
A = Matrix([
    [1, 2],
    [3, 4]
])  # Dimension: 2x2

B = Matrix([
    [5, 6],
    [7, 8]
])  # Dimension: 2x2

C = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])  # Dimension: 2x3

D = Matrix([
    [10],
    [20],
    [30]
])  # Dimension: 3x1

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

# --- Matrix-Addition (+) ---
print("\n--- Addition (A + B) ---")
try:
    E = A + B  # 2x2 + 2x2 -> 2x2
    print(f"Ergebnis (A + B):\n{E}")
except ValueError as e:
    print(f"Fehler bei Addition: {e}")

# Fehlerfall Addition
print("\n--- Fehlerfall Addition (A + C) ---")
try:
    A + C  # 2x2 + 2x3 -> Fehler
except ValueError as e:
    print(f"Erwarteter Fehler (A + C): {e}")


# --- Matrix-Multiplikation (*) ---
print("\n--- Multiplikation (C * D) ---")
try:
    F = C * D  # 2x3 * 3x1 -> 2x1
    print(f"Ergebnis (C * D):\n{F}")
except ValueError as e:
    print(f"Fehler bei Multiplikation: {e}")

# Neue Matrix für den Fehlerfall (3x2)
E = Matrix([
    [10, 20],
    [30, 40],
    [50, 60]
])  # Dimension: 3x2

# Fehlerfall Multiplikation
print("\n--- Fehlerfall Multiplikation (A * E) ---")
try:
    # A (2x2) * E (3x2) -> Fehler (Spalten von A (2) != Zeilen von E (3))
    A * E
except ValueError as e:
    print(f"Erwarteter Fehler (A * E): {e}")

# Fehlerfall Konstruktor
print("\n--- Fehlerfall Konstruktor (Ungleiche Zeilenlänge) ---")
try:
    G = Matrix([
        [1, 2],
        [3, 4, 5]  # Diese Zeile ist zu lang
    ])
except ValueError as e:
    print(f"Erwarteter Fehler (Konstruktor): {e}")
