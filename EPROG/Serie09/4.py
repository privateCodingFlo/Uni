import math


class MyFunction:
    """
    Klasse zur Speicherung einer mathematischen Funktion f: [a, b] -> R
    und zur Überprüfung des Definitionsbereichs beim Aufruf.
    """

    def __init__(self, func, a, b):
        """
        Konstruktor: Speichert die Funktion und den Definitionsbereich [a, b].

        :param func: Die eigentliche Funktion (z.B. ein Lambda-Ausdruck oder eine def-Funktion).
        :param a: Die untere Grenze des Definitionsbereichs (einschließlich).
        :param b: Die obere Grenze des Definitionsbereichs (einschließlich).
        """
        if a > b:
            raise ValueError(
                "Der Definitionsbereich [a, b] ist ungültig: a muss <= b sein.")

        self.func = func
        self.a = a
        self.b = b

        # Speichere den Definitionsbereich als String für Fehlermeldungen
        self.domain = f"[{a}, {b}]"

    def __call__(self, x):
        """
        Magic Method: Ermöglicht den Aufruf des Objekts wie eine normale Funktion (objekt(x)).

        :param x: Der Eingabewert für die Funktion.
        :return: Das Ergebnis der Funktion f(x).
        """

        # 1. Überprüfung des Definitionsbereichs
        if not (self.a <= x <= self.b):
            raise ValueError(
                f"Eingabewert x={x} liegt außerhalb des gültigen Definitionsbereichs {self.domain}."
            )

        # 2. Ausführung der Funktion
        return self.func(x)

    # Optional: Repräsentation für besseres Debugging
    def __repr__(self):
        return f"MyFunction(domain={self.domain})"

# ----------------------------------------------------------------------
# Testsuite
# ----------------------------------------------------------------------

# Beispiel-Funktionen für die Tests


def linear_func(x):
    """f(x) = 2x + 1"""
    return 2 * x + 1


def abs_func(x):
    """f(x) = |x|"""
    return abs(x)


print("--- Start der Testsuite für MyFunction ---")

# 1. Test: Initialisierung (Konstruktor)

print("\n## 1. Test: Initialisierung")

# Test 1.1: Gültiger Bereich
try:
    f1 = MyFunction(linear_func, 0, 10)
    print(f"✅ Test 1.1 (Gültige Initialisierung [0, 10]): {f1}")
except Exception as e:
    print(f"❌ Test 1.1 (Gültige Initialisierung) FEHLGESCHLAGEN: {e}")

# Test 1.2: Bereich mit gleichen Grenzen (einzelner Punkt)
try:
    f2 = MyFunction(linear_func, 5, 5)
    print(f"✅ Test 1.2 (Gleiche Grenzen [5, 5]): {f2}")
except Exception as e:
    print(f"❌ Test 1.2 (Gleiche Grenzen) FEHLGESCHLAGEN: {e}")

# Test 1.3: Ungültiger Bereich (Fehlerbehandlung)
try:
    f_error = MyFunction(linear_func, 10, 0)
    print("❌ Test 1.3 (Ungültiger Bereich) FEHLGESCHLAGEN: Kein ValueError geworfen.")
except ValueError as e:
    print(f"✅ Test 1.3 (Ungültiger Bereich) ERFOLGREICH: {e}")
except Exception as e:
    print(
        f"❌ Test 1.3 (Ungültiger Bereich) FEHLGESCHLAGEN: Falscher Fehler geworfen: {e}")

print("-" * 35)

# 2. Test: Gültiger Funktionsaufruf (__call__)

print("\n## 2. Test: Gültiger Aufruf")

f_linear = MyFunction(linear_func, -5, 5)  # f(x) = 2x + 1, Bereich [-5, 5]

# Test 2.1: Wert in der Mitte
x_mid = 0
erw_mid = 2 * 0 + 1  # 1
erg_mid = f_linear(x_mid)
assert erg_mid == erw_mid
print(f"✅ Test 2.1 (Wert in der Mitte, x={x_mid}): Ergebnis {erg_mid} stimmt.")

# Test 2.2: Untere Grenze (einschließlich)
x_low = -5
erw_low = 2 * (-5) + 1  # -9
erg_low = f_linear(x_low)
assert erg_low == erw_low
print(f"✅ Test 2.2 (Untere Grenze, x={x_low}): Ergebnis {erg_low} stimmt.")

# Test 2.3: Obere Grenze (einschließlich)
x_high = 5
erw_high = 2 * 5 + 1  # 11
erg_high = f_linear(x_high)
assert erg_high == erw_high
print(f"✅ Test 2.3 (Obere Grenze, x={x_high}): Ergebnis {erg_high} stimmt.")

print("-" * 35)

# 3. Test: Fehlerfälle (__call__ außerhalb des Bereichs)

print("\n## 3. Test: Fehlerfälle")

# Test 3.1: Wert unterhalb des Bereichs
x_out_low = -5.1
try:
    f_linear(x_out_low)
    print("❌ Test 3.1 (x < a) FEHLGESCHLAGEN: Kein ValueError geworfen.")
except ValueError as e:
    print(f"✅ Test 3.1 (x < a) ERFOLGREICH: {e}")

# Test 3.2: Wert oberhalb des Bereichs
x_out_high = 5.001
try:
    f_linear(x_out_high)
    print("❌ Test 3.2 (x > b) FEHLGESCHLAGEN: Kein ValueError geworfen.")
except ValueError as e:
    print(f"✅ Test 3.2 (x > b) ERFOLGREICH: {e}")

# Test 3.3: Komplexere Funktion (z.B. math.sqrt)
f_sqrt = MyFunction(math.sqrt, 1, 100)  # Bereich [1, 100]

try:
    # Gültig
    erg_sqrt = f_sqrt(25)
    assert erg_sqrt == 5.0
    print(f"✅ Test 3.3a (Gültig): sqrt(25) = {erg_sqrt}")

    # Ungültig
    f_sqrt(0.5)
    print("❌ Test 3.3b (Ungültig) FEHLGESCHLAGEN: Kein ValueError geworfen.")
except ValueError as e:
    # Hier fangen wir den erwarteten Fehler für x=0.5 ab
    print(f"✅ Test 3.3b (Ungültig) ERFOLGREICH: {e}")
except Exception as e:
    print(f"❌ Test 3.3b (Ungültig) FEHLGESCHLAGEN: Unerwarteter Fehler: {e}")

print("-" * 35)
print("--- Ende der Testsuite ---")
