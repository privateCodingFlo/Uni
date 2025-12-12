import math
import matplotlib.pyplot as plt


class Polynom:
    """
    Repräsentiert ein Polynom der Form f(x) = a_0 + a_1*x + ... + a_n*x^n.
    Mit Plot-Funktionalität (Aufgabe 1, Serie 10).
    """

    def __init__(self, coefficients):
        """
        Initialisiert das Polynom mit einer Liste von Koeffizienten [a_0, a_1, ..., a_n].
        """
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
        # Die Liste der neuen Koeffizienten hat die Länge n + m - 1
        result_coeffs = [0.0] * (n + m - 1)

        for k in range(n + m - 1):
            sum_val = 0.0
            # i läuft von 0 bis k, darf aber n nicht überschreiten
            start_i = max(0, k - m + 1)
            end_i = min(k, n - 1)

            for i in range(start_i, end_i + 1):
                j = k - i
                sum_val += coeffs1[i] * coeffs2[j]

            result_coeffs[k] = sum_val

        return Polynom(result_coeffs)

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

        new_coefficients = [
            i * self.coefficients[i] for i in range(1, len(self.coefficients))
        ]

        return Polynom(new_coefficients)

    def integrate(self, x_1, x_2):
        """3. Berechnet das bestimmte Integral von x_1 bis x_2."""
        F_coeffs = [0.0] + [
            self.coefficients[i] / (i + 1) for i in range(len(self.coefficients))
        ]
        F = Polynom(F_coeffs)
        return F.eval(x_2) - F.eval(x_1)

    def zeros(self):
        """4. Berechnet die Nullstellen eines Polynoms ZWEITEN Grades (ax^2 + bx + c)."""
        if self.order != 2:
            raise ValueError(
                f"Nullstellenberechnung nur für Polynome zweiten Grades möglich. Aktueller Grad: {self.order}"
            )

        c, b, a = self.coefficients[0], self.coefficients[1], self.coefficients[2]

        if a == 0:
            raise ValueError("Koeffizient von x^2 ist Null.")

        p = b / a
        q = c / a

        discriminant = (p / 2) ** 2 - q

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

    def __add__(self, other):
        """Ermöglicht Polynom-Addition mit dem '+' Operator."""
        if not isinstance(other, Polynom):
            return NotImplemented
        return Polynom.add(self, other)

    # --- AUFGABE 1: PLOT-METHODE ---
    def plot(self, x_1, x_2):
        """
        Plottet die Funktion in einem beliebigen Intervall [x1, x2].
        """
        # Erzeugen von 500 Punkten im Intervall [x_1, x_2] ohne Numpy
        num_points = 500
        step = (x_2 - x_1) / (num_points - 1)
        x_values = [x_1 + i * step for i in range(num_points)]
        # Berechnen der y-Werte
        y_values = [self.eval(x) for x in x_values]

        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, label=f"f(x) = {self}")

        # Achsenbeschriftung
        plt.xlabel("x")
        plt.ylabel("f(x)")

        # Titel
        plt.title(f"Plot des Polynoms: {self}")

        # Gitter und Legende
        plt.grid(True)
        plt.legend()

        # Anzeigen
        plt.show()


if __name__ == "__main__":
    # Testen der Plot-Funktion
    # Beispielpolynom: f(x) = 1 - x + x^2 - x^3 (zum Beispiel)
    # Koeffizienten: [1, -1, 1, -1]
    p = Polynom([1, -1, 1, -1])
    print(f"Erstelltes Polynom: {p}")
    print("Plot wird erstellt für Intervall [-2, 2]...")
    p.plot(-2, 2)
    print("Fertig.")
