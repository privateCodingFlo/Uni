import math

# Kopie der Klasse aus Beispiel 5 von Serie08


class Polynom:
    """
    Repräsentiert ein Polynom der Form f(x) = a_0 + a_1*x + ... + a_n*x^n.
    """

    def __init__(self, coefficients):
        """
        Initialisiert das Polynom mit einer Liste von Koeffizienten [a_0, a_1, ..., a_n].
        """
        # Führende Nullen entfernen
        # while len(coefficients) > 1 and coefficients[-1] == 0:
        #     coefficients.pop() # Deaktiviert, da es in __mul__ zu Problemen führen könnte, wenn die Koeffizienten noch nicht final sind.

        # Dieses Attribut scheint nicht verwendet zu werden.
        self.diffDigit0 = 0
        # Sicherstellen, dass es eine bearbeitbare Liste ist
        self.coefficients = list(coefficients)

        # Führende Nullen nachträglich entfernen und Grad aktualisieren
        self._normalize()

    def _normalize(self):
        """Entfernt führende Nullen und aktualisiert den Grad."""
        while len(self.coefficients) > 1 and self.coefficients[-1] == 0:
            self.coefficients.pop()

        self.order = len(self.coefficients) - 1 if self.coefficients else -1

    def __str__(self):
        """
        Gibt eine lesbare String-Repräsentation des Polynoms zurück.
        (Die Implementierung ist sehr komplex, ich verwende die bestehende Logik.)
        """
        if not self.coefficients or all(c == 0 for c in self.coefficients):
            return "0"

        terms = []
        for i, a in enumerate(self.coefficients):
            if a != 0:
                if i == 0:
                    term = f"{a}"
                elif i == 1:
                    term = f"{a}x"
                else:
                    term = f"{a}x^{i}"
                terms.append(term)

        # Formatierung (fügt "+" zwischen Termen ein)
        return " + ".join(terms).replace("+ -", " - ")

    def __repr__(self):
        """Offizielle String-Repräsentation (für Debugging)."""
        return f"Polynom({self.coefficients})"

    # --- NEUE MAGIC METHOD FÜR AUFGABE 6 ---

    def __mul__(self, other):
        """
        Implementiert die Polynom-Multiplikation (self * other).
        Berechnet das Produkt zweier Polynome f(x) * g(x).
        """
        if not isinstance(other, Polynom):
            return NotImplemented

        coeffs1 = self.coefficients
        coeffs2 = other.coefficients

        n = len(coeffs1)
        m = len(coeffs2)

        # Das resultierende Polynom hat maximal den Grad (n-1) + (m-1)
        new_degree = n + m - 2
        # Die Liste der neuen Koeffizienten hat die Länge n + m - 1
        result_coeffs = [0.0] * (n + m - 1)

        # Faltungsformel: c_k = Sum_{i=0}^{k} a_i * b_{k-i}
        # k läuft von 0 bis zum maximalen Grad (n + m - 2)
        for k in range(n + m - 1):

            # Die Summe wird über i=0 bis k berechnet
            sum_val = 0.0

            # i = Index des Koeffizienten in der ersten Liste (coeffs1)
            # j = Index des Koeffizienten in der zweiten Liste (coeffs2)
            # Wobei gelten muss: i + j = k => j = k - i

            # i läuft von 0 bis k, darf aber n nicht überschreiten
            start_i = max(0, k - m + 1)
            end_i = min(k, n - 1)

            for i in range(start_i, end_i + 1):
                j = k - i
                sum_val += coeffs1[i] * coeffs2[j]

            result_coeffs[k] = sum_val

        return Polynom(result_coeffs)

    # --- (Weitere Methoden aus der Originalklasse) ---

    def eval(self, x):
        """1. Auswertung des Polynoms an der Stelle x, f(x). (Horner-Schema)"""
        result = 0.0
        for coeff in reversed(self.coefficients):
            result = result * x + coeff
        return result

    def diff(self):
        """2. Berechnet die Ableitung f'(x)."""
        if self.order < 1:
            return Polynom([0.0])

        new_coefficients = [i * self.coefficients[i]
                            for i in range(1, len(self.coefficients))]

        return Polynom(new_coefficients)

    def integrate(self, x_1, x_2):
        """3. Berechnet das bestimmte Integral von x_1 bis x_2."""
        F_coeffs = [0.0] + [self.coefficients[i] /
                            (i + 1) for i in range(len(self.coefficients))]
        F = Polynom(F_coeffs)
        return F.eval(x_2) - F.eval(x_1)

    def zeros(self):
        """4. Berechnet die Nullstellen eines Polynoms ZWEITEN Grades (ax^2 + bx + c)."""
        if self.order != 2:
            raise ValueError(
                f"Nullstellenberechnung nur für Polynome zweiten Grades möglich. Aktueller Grad: {self.order}")

        c, b, a = self.coefficients[0], self.coefficients[1], self.coefficients[2]

        if a == 0:
            raise ValueError("Koeffizient von x^2 ist Null.")

        p = b / a
        q = c / a

        discriminant = (p / 2)**2 - q

        if discriminant < 0:
            return None

        sqrt_D = math.sqrt(discriminant)

        if discriminant == 0:
            x_1 = -p / 2
            return (x_1, x_1)

        x_1 = -p / 2 + sqrt_D
        x_2 = -p / 2 - sqrt_D

        return (x_1, x_2)

    @staticmethod
    def add(f1, f2):
        """5. Statische Methode zur Addition von zwei Polynom-Objekten."""
        max_len = max(len(f1.coefficients), len(f2.coefficients))
        new_coeffs = []

        for i in range(max_len):
            coeff1 = f1.coefficients[i] if i < len(f1.coefficients) else 0.0
            coeff2 = f2.coefficients[i] if i < len(f2.coefficients) else 0.0

            new_coeffs.append(coeff1 + coeff2)

        return Polynom(new_coeffs)

    # Für die bessere Nutzung des '+' Operators (optional)
    def __add__(self, other):
        """Ermöglicht Polynom-Addition mit dem '+' Operator."""
        if not isinstance(other, Polynom):
            return NotImplemented
        return Polynom.add(self, other)


# ----------------------------------------------------------------------
# Testsuite für __mul__
# ----------------------------------------------------------------------


print("\n--- Testsuite für Polynom-Multiplikation ---")

P1 = Polynom([3])
Q1 = Polynom([1, 2])
R1 = P1 * Q1

print("\nTest 1: Konstante * Polynom")
print(f"P(x) = {P1}, Q(x) = {Q1}")
print(f"R(x) = P(x) * Q(x) = {R1}")
assert R1.coefficients == [3.0, 6.0]
assert R1.eval(2) == 3 + 6*2  # Test mit Wert 2: 15
print(f"✅ Koeffizienten korrekt: {R1.coefficients}")
print(f"✅ Evaluierung korrekt: {R1.eval(2)}")

P2 = Polynom([1, 2, 3])
Q2 = Polynom([4, 5])
R2 = P2 * Q2
erwartet_coeffs2 = [4.0, 13.0, 22.0, 15.0]

print("\nTest 2: Quadrat * Linear")
print(f"P(x) = {P2}, Q(x) = {Q2}")
print(f"R(x) = P(x) * Q(x) = {R2}")
assert all(abs(a - b) < 1e-9 for a,
           b in zip(R2.coefficients, erwartet_coeffs2))
print(f"✅ Koeffizienten korrekt: {R2.coefficients}")
print(f"✅ Grad korrekt: {R2.order} (erwartet 3)")

P3 = Polynom([1, 0, -1])
Q3 = Polynom([1, 1])
R3 = P3 * Q3
erwartet_coeffs3 = [1.0, 1.0, -1.0, -1.0]

print("\nTest 3: Produkt mit Nullkoeffizienten")
print(f"P(x) = {P3}, Q(x) = {Q3}")
print(f"R(x) = P(x) * Q(x) = {R3}")
assert all(abs(a - b) < 1e-9 for a,
           b in zip(R3.coefficients, erwartet_coeffs3))
print(f"✅ Koeffizienten korrekt: {R3.coefficients}")
