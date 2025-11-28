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

        self.diffDigit0 = 0
        self.coefficients = coefficients
        self.order = len(self.coefficients) - 1 if self.coefficients else -1

    def __str__(self):
        """
        Gibt eine lesbare String-Repräsentation des Polynoms zurück.
        """
        if self.order == 0:
            return "0"

        terms = []
        # index startet mit 0 => len()-1
        polynomAmount = len(self.coefficients)-1

        # mit absteigender Potzenz ausgeben
        for i, a in enumerate(reversed(self.coefficients)):
            if a != 0:
                # Formatierung für x^0, x^1 und x^i
                if i < polynomAmount - 1:
                    # Rückwärts zählend die Potenzen ausgeben
                    terms.append(f"{a}x^{polynomAmount-i}")
                elif i == polynomAmount - 1:
                    terms.append(f"{a}x")
                else:
                    terms.append(f"{a}")

        # Verbinde die Terme mit " + " und ersetze "+ -" durch "- "
        # return "Beweis, dass der String hier bestimmt wird."
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
        sqrt_D = discriminant**(1/2)

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


# ----------------------------------------------------------------------
# TESTBEREICH 1: Standardpolynom f1(x) = 3x^2 + 2x + 1 (Grad 2)
# ----------------------------------------------------------------------
f1 = Polynomial([1.0, 2.0, 3.0])
print("\n--- TESTBEREICH 1: f1(x) = 3x^2 + 2x + 1 ---")
print(f"f1(x): {f1}")
print(f"Ordnung (Grad): {f1.order}")

# f1(2) = 1 + 2*2 + 3*2^2 = 1 + 4 + 12 = 17
print(f"f1(2.0): {f1.eval(2.0)}")

# f1'(x) = 6x + 2
f1_prime = f1.diff()
print(f"Ableitung f1'(x): {f1_prime}")
# f1'(2) = 6*2 + 2 = 14
print(f"f1'(2.0): {f1_prime.eval(2.0)}")

# Integral von 0 bis 2 von (3x^2 + 2x + 1) dx = [x^3 + x^2 + x]_0^2 = 14
integral_value = f1.integrate(0.0, 2.0)
print(f"Integral von f1(x) von 0 bis 2: {integral_value}")

# ----------------------------------------------------------------------
# TESTBEREICH 2: Konstantes Polynom f_const(x) = 5.0 (Grad 0)
# ----------------------------------------------------------------------
f_const = Polynomial([5.0])
print("\n--- TESTBEREICH 2: Konstantes Polynom f_const(x) = 5.0 ---")
print(f"f_const(x): {f_const}")
print(f"Ordnung (Grad): {f_const.order}")

# Konstantenwert sollte immer 5.0 sein
print(f"f_const eval(100.0): {f_const.eval(100.0)}")

# Ableitung f_const'(x) = 0
f_const_prime = f_const.diff()
print(f"Ableitung f_const'(x): {f_const_prime}")

# Integral von 0 bis 3 von 5 dx = [5x]_0^3 = 15
integral_const = f_const.integrate(0.0, 3.0)
print(
    f"Integral von f_const(x) von 0 bis 3: {integral_const}")

# ----------------------------------------------------------------------
# TESTBEREICH 3: Nullpolynom f_null(x) = 0 (Grad -1)
# ----------------------------------------------------------------------
# Eingabe: [0.0, 0.0, 0.0] -> __init__ entfernt Nullen -> Ergebnis: []
f_null = Polynomial([0.0, 0.0, 0.0])
print("\n--- TESTBEREICH 3: Nullpolynom f_null(x) = 0 ---")
print(f"f_null(x): {f_null}")
print(f"Ordnung (Grad): {f_null.order}")
print(f"f_null eval(10.0): {f_null.eval(10.0)}")

# ----------------------------------------------------------------------
# TESTBEREICH 4: Polynom mit negativen Koeffizienten (Grad 3)
# f_neg(x) = -0.5x^3 - 2x + 10
# ----------------------------------------------------------------------
f_neg = Polynomial([10.0, -2.0, 0.0, -0.5])
print("\n--- TESTBEREICH 4: f_neg(x) = -0.5x^3 - 2x + 10 ---")
print(f"f_neg(x): {f_neg}")

# f_neg(4) = 10 - 2*4 - 0.5*4^3 = 10 - 8 - 32 = -30
print(f"f_neg eval(4.0): {f_neg.eval(4.0)}")

# f_neg'(x) = -1.5x^2 - 2.0
f_neg_prime = f_neg.diff()
print(f"Ableitung f_neg'(x): {f_neg_prime}")

# ----------------------------------------------------------------------
# TESTBEREICH 5: Nullstellenberechnung (zeros)
# ----------------------------------------------------------------------
# 5.1 Doppelte Nullstelle: f_double(x) = x^2 - 6x + 9 = (x - 3)^2. Nullstelle x=3
f_double = Polynomial([9.0, -6.0, 1.0])
print("\n--- TESTBEREICH 5.1: Doppelte Nullstelle (f(x) = (x-3)^2) ---")
print(f"f_double(x): {f_double}")
print(f"Nullstellen: {f_double.zeros()}")

# 5.2 Fehlerbehandlung (Grad 3)
print("\n--- TESTBEREICH 5.2: Fehlerbehandlung bei falschem Grad ---")
try:
    f_neg.zeros()  # f_neg ist Grad 3, sollte ValueError auslösen
except ValueError as e:
    print(f"Erfolg: Fehler ausgelöst! Meldung: {e}")

# ----------------------------------------------------------------------
# TESTBEREICH 6: Addition (add)
# ----------------------------------------------------------------------
# f_add1(x) = 3x^4 - 5x + 1
f_add1 = Polynomial([1.0, -5.0, 0.0, 0.0, 3.0])
# f_add2(x) = 2x^2 + x - 5
f_add2 = Polynomial([-5.0, 1.0, 2.0])
# Summe f_sum2(x) = 3x^4 + 2x^2 - 4x - 4
f_sum2 = Polynomial.add(f_add1, f_add2)

print("\n--- TESTBEREICH 6: Addition (f_add1 + f_add2) ---")
print(f"f_add1(x): {f_add1}")
print(f"f_add2(x): {f_add2}")
print(f"Summe f_sum2(x): {f_sum2}")

# f_sum2(1) = 3*1^4 + 2*1^2 - 4*1 - 4 = -3
print(f"f_sum2(1.0): {f_sum2.eval(1.0)}")
