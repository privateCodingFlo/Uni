import math


class Polynom:
    def __init__(self, coefficients):
        # Wir entfernen führende Nullen am Ende, um den wahren Grad zu bestimmen
        while len(coefficients) > 1 and coefficients[-1] == 0:
            coefficients.pop()
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))

    def __add__(self, other):
        new_coeffs = []
        for i in range(max(len(self.coefficients), len(other.coefficients))):
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coef1 + coef2)
        return self._cast_to_special(new_coeffs)

    def __sub__(self, other):
        new_coeffs = []
        for i in range(max(len(self.coefficients), len(other.coefficients))):
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coef1 - coef2)
        return self._cast_to_special(new_coeffs)

    def _cast_to_special(self, coeffs):
        """Hilfsmethode, um das Ergebnis in die korrekte Klasse zu gießen."""
        # Entferne führende Nullen für die Gradbestimmung
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()

        grad = len(coeffs) - 1
        if grad == 1:
            return LinearFunction(coeffs[0], coeffs[1])
        elif grad == 2:
            return QuadraticFunction(coeffs[0], coeffs[1], coeffs[2])
        else:
            return Polynom(coeffs)


class LinearFunction(Polynom):
    def __init__(self, c0, c1):
        # Konstruktor akzeptiert Einzelparameter statt Liste
        super().__init__([c0, c1])

    def nullstellen(self):
        """Gibt die reelle Nullstelle als Liste zurück."""
        c0 = self.coefficients[0]
        c1 = self.coefficients[1]
        if c1 == 0:
            return []  # Keine oder unendlich viele Nullstellen
        return [-c0 / c1]


class QuadraticFunction(Polynom):
    def __init__(self, c0, c1, c2):
        # Konstruktor akzeptiert Einzelparameter statt Liste
        super().__init__([c0, c1, c2])

    def nullstellen(self):
        """Berechnet reelle Nullstellen mit der Mitternachtsformel."""
        c0, c1, c2 = self.coefficients[0], self.coefficients[1], self.coefficients[2]

        # Diskriminante: D = b^2 - 4ac
        d = c1**2 - 4*c2*c0

        if d < 0:
            return []
        elif d == 0:
            return [-c1 / (2 * c2)]
        else:
            sqrt_d = math.sqrt(d)
            return [(-c1 - sqrt_d) / (2 * c2), (-c1 + sqrt_d) / (2 * c2)]


# Testbeispiel
q1 = QuadraticFunction(1, 0, 1)  # x^2 + 1 (keine reellen Nullstellen)
q2 = QuadraticFunction(0, 0, 1)  # x^2 (Nullstelle: 0)
res = q1 - q2                    # Ergibt konstantes Polynom (Polynom-Klasse)
print(f"Typ von res: {type(res).__name__}")
