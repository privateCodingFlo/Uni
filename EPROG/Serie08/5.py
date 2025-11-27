# Aufgabe 5: Polynom-Klasse
# Erstellen Sie eine Klasse Polynomial zur Darstellung und Bearbeitung von Polynomen.

class Polynomial:
    """
    Repräsentiert ein Polynom der Form f(x) = a_0 + a_1*x + ... + a_n*x^n.
    """

    def __init__(self, coefficients):
        """
        Initialisiert das Polynom mit einer Liste von Koeffizienten [a_0, a_1, ..., a_n].
        """
        # Führende Nullen entfernen
        while len(coefficients) > 1 and coefficients[-1] == 0:
            coefficients.pop()

        self.coefficients = coefficients
        self.order = len(self.coefficients) - 1 if self.coefficients else -1

    def __str__(self):
        """
        Gibt eine lesbare String-Repräsentation des Polynoms zurück.
        """
        if self.order == -1:
            return "0"

        terms = []
        for i, a in enumerate(self.coefficients):
            if a != 0:
                # Formatierung für x^0, x^1 und x^i
                if i == 0:
                    terms.append(str(a))
                elif i == 1:
                    terms.append(f"{a}x")
                else:
                    terms.append(f"{a}x^{i}")

        # Verbinde die Terme mit " + " und ersetze "+ -" durch "- "
        return " + ".join(terms).replace("+ -", "- ")

    def eval(self, x):
        """
        1. Auswertung des Polynoms an der Stelle x, f(x). (Horner-Schema)
        """
        result = 0.0
        # Horner-Schema: f(x) = a_0 + x * (a_1 + x * (a_2 + ...))
        # Iteriere rückwärts über die Koeffizienten
        for coeff in reversed(self.coefficients):
            result = result * x + coeff
        return result

    def diff(self):
        """
        2. Berechnet die Ableitung f'(x).
        """
        if self.order < 1:
            return Polynomial([0.0])  # Ableitung einer Konstanten ist 0

        new_coefficients = []
        # Neuer Koeffizient a_i wird zu i * a_i (und der neue Index ist i-1).
        # Starte bei i=1, da a_0 (Konstante) wegfällt.
        for i in range(1, len(self.coefficients)):
            new_coefficients.append(i * self.coefficients[i])

        return Polynomial(new_coefficients)

    def integrate(self, x_1, x_2):
        """
        3. Berechnet das bestimmte Integral von x_1 bis x_2.
        """
        # Stammfunktion F(x) = a_0*x/1 + a_1*x^2/2 + ...
        integral_coeffs = []
        # Der Koeffizient b_0 der Stammfunktion (Konstante C) ist 0
        F_coeffs = [0.0]

        for i, a in enumerate(self.coefficients):
            # Der Koeffizient von x^(i+1) in F(x) ist a / (i + 1)
            F_coeffs.append(a / (i + 1))

        F = Polynomial(F_coeffs)

        # Hauptsatz der Differential- und Integralrechnung: F(x_2) - F(x_1)
        return F.eval(x_2) - F.eval(x_1)

    def zeros(self):
        """
        4. Berechnet die Nullstellen eines Polynoms ZWEITEN Grades (ax^2 + bx + c).
        """
        if self.order != 2:
            raise ValueError(
                f"Nullstellenberechnung nur für Polynome zweiten Grades möglich. Aktueller Grad: {self.order}")

        # c = a_0, b = a_1, a = a_2
        c, b, a = self.coefficients[0], self.coefficients[1], self.coefficients[2]

        if a == 0:  # Sollte durch self.order != 2 abgefangen sein
            raise ValueError("Koeffizient von x^2 ist Null.")

        # p-q-Formel vorbereiten: x^2 + p*x + q = 0
        p = b / a
        q = c / a

        # Diskriminante D = (p/2)^2 - q
        discriminant = (p / 2)**2 - q

        if discriminant < 0:
            return None  # Keine reellen Nullstellen

        # Wurzel der Diskriminante
        sqrt_D = discriminant**0.5

        if discriminant == 0:
            x_1 = -p / 2
            return (x_1, x_1)  # Eine doppelte Nullstelle

        # Zwei reelle Nullstellen
        x_1 = -p / 2 + sqrt_D
        x_2 = -p / 2 - sqrt_D

        return (x_1, x_2)

    # @staticmethod = Funktion kann über <Klassen-Namen>.<Funktions-Namen>() aufgerufen werden und es muss nicht 
    # extra ein Objekt angelegt werden (sprich keine Variable mit der Klasse)
    @staticmethod
    def add(f1, f2):
        """
        5. Statische Methode zur Addition von zwei Polynom-Objekten.
        """
        max_len = max(len(f1.coefficients), len(f2.coefficients))
        new_coeffs = []

        for i in range(max_len):
            coeff1 = f1.coefficients[i] if i < len(f1.coefficients) else 0.0
            coeff2 = f2.coefficients[i] if i < len(f2.coefficients) else 0.0

            new_coeffs.append(coeff1 + coeff2)

        return Polynomial(new_coeffs)


# --- Test ---
f1 = Polynomial([1.0, 2.0, 3.0])
print("\n--- Test Polynom f1 ---")
print(f"f1(x): {f1}")
print(f"Integral von f1(x) von 0 bis 2: {f1.integrate(0.0, 2.0)}")
