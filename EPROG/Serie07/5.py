#  ----- Nicht mit kopieren danke -----
#  ----- Nicht mit kopieren danke -----
# (Gemini Gelöst, weil ich keinen Bock mehr nach Beispiel 4 hatte)
# ----- Nicht mit kopieren danke -----
# ----- Nicht mit kopieren danke -----
import math


def diff(f, x, h0, eps):
    """
    Approximiert die Ableitung f'(x) mithilfe des einseitigen Differenzenquotienten
    und der Folge h_n = 2^(-n) * h0.

    Die Berechnung stoppt, wenn die relative Änderung zwischen zwei aufeinanderfolgenden
    Approximationen kleiner oder gleich eps ist.

    :param f: Die differenzierbare Funktion (z.B. lambda x: x**2).
    :param x: Der feste Punkt, an dem die Ableitung approximiert werden soll.
    :param h0: Die anfängliche Schrittweite h0 (n=0).
    :param eps: Die Fehlerschranke (Epsilon) für die Abbruchbedingung.
    :return: Die finale Approximation der Ableitung f'(x) (Phi(h_n)).
    """

    # ----------------------------------------------------------------------
    # 1. Startwerte für n=0
    # ----------------------------------------------------------------------

    # h_n ist die aktuelle Schrittweite (h_0 in der ersten Iteration)
    h_n = h0

    # Berechne den ersten Differenzenquotienten Phi(h_0)
    # Phi(h) = (f(x + h) - f(x)) / h
    phi_n = (f(x + h_n) - f(x)) / h_n

    # ----------------------------------------------------------------------
    # 2. Iteration (für n = 1, 2, 3, ...)
    # ----------------------------------------------------------------------

    n = 0  # Zähler für die Iterationen (entspricht dem Exponenten in 2^-n)

    while True:
        # Erhöhe den Zähler für den nächsten Schritt
        n += 1

        # 2a. Berechne Phi(h_{n+1})

        # Die neue Schrittweite h_{n+1} ist h_n / 2 (da 2^(-n) * h0 = 2^(-(n-1)) * h0 / 2)
        h_n_plus_1 = h_n / 2.0

        # Berechne den neuen Differenzenquotienten Phi(h_{n+1})
        phi_n_plus_1 = (f(x + h_n_plus_1) - f(x)) / h_n_plus_1

        # 2b. Prüfe die Abbruchbedingung

        # Absolute Differenz der Approximationen: |Phi(h_n) - Phi(h_{n+1})|
        differenz_abs = abs(phi_n - phi_n_plus_1)

        # Schranke: epsilon * |Phi(h_n)|. Wir verwenden Phi(h_n) als Referenzwert.
        schranke = eps * abs(phi_n)

        # Wenn die absolute Differenz die Schranke unterschreitet, breche ab.
        # Bedingung: |Phi(h_n) - Phi(h_{n+1})| <= epsilon * |Phi(h_n)|
        if differenz_abs <= schranke:
            # Die Näherung phi_n_plus_1 ist das Ergebnis der letzten akzeptierten Iteration.
            return phi_n_plus_1

        # 2c. Werte für die nächste Iteration vorbereiten

        # Die aktuelle Näherung wird zur alten Näherung für den nächsten Schritt
        phi_n = phi_n_plus_1

        # Die neue Schrittweite wird zur aktuellen Schrittweite für den nächsten Schritt
        h_n = h_n_plus_1

        # Sicherheit: Breche ab, wenn h zu klein wird (Gefahr von Gleitkommafehlern)
        if h_n < 1e-15:
            # Gib die beste bisherige Näherung zurück
            return phi_n_plus_1


# ----------------------------------------------------------------------
# Beispielanwendung
# ----------------------------------------------------------------------

# Funktion f(x) = x^2. Ableitung f'(x) = 2x.
# An der Stelle x=3 ist die exakte Ableitung f'(3) = 2 * 3 = 6.0
def funktion_quadrat(x):
    return x**2


X_punkt = 3.0       # Punkt x
H_initial = 0.1     # Startwert h0
EPS_toleranz = 1e-4  # Fehlerschranke epsilon (1 * 10^-4)

ableitung_approx = diff(funktion_quadrat, X_punkt, H_initial, EPS_toleranz)

print("## 🧪 Numerische Ableitung - Beispiel")
print(f"Funktion: f(x) = x^2, Punkt: x = {X_punkt}")
print(f"Exakte Ableitung f'({X_punkt}): 6.0")
print(f"Anfängliche Schrittweite h0: {H_initial}")
print(f"Toleranz (eps): {EPS_toleranz}")
print("---")
print(f"Approximierte Ableitung (diff): {ableitung_approx:.8f}")
print(f"Abweichung zum exakten Wert: {abs(6.0 - ableitung_approx):.8e}")

# Weiteres Beispiel: f(x) = sin(x) an der Stelle x=0.5


def funktion_sinus(x):
    return math.sin(x)


X_sinus = 0.5
# Exakte Ableitung f'(x) = cos(x). f'(0.5) = cos(0.5) ≈ 0.87758256
exakt_sinus = math.cos(X_sinus)

ableitung_sinus = diff(funktion_sinus, X_sinus, H_initial, EPS_toleranz)

print("\n--- Weiteres Beispiel: f(x) = sin(x) ---")
print(f"Exakte Ableitung f'({X_sinus}): {exakt_sinus:.8f}")
print(f"Approximierte Ableitung (diff): {ableitung_sinus:.8f}")
print(f"Abweichung zum exakten Wert: {abs(exakt_sinus - ableitung_sinus):.8e}")
