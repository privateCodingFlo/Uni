# Aufgabe 2: Newton-Verfahren
# Sucht iterativ eine Nullstelle einer Funktion f, gegeben ihre Ableitung fprime.

def newton(f, fprime, x0, tol):
    """
    Sucht iterativ eine Nullstelle der Funktion f(x) mit dem Newton-Verfahren.

    :param f: Die Funktion f(x) (als Python-Funktion).
    :param fprime: Die Ableitung f'(x) (als Python-Funktion).
    :param x0: Der Startwert.
    :param tol: Die Abbruchtoleranz (tau).
    :return: Die gefundene Nullstelle.
    """
    x_old = x0

    max_iter = 100  # Sicherheitslimit
    for n in range(max_iter):
        f_xn = f(x_old)
        fprime_xn = fprime(x_old)

        # 1. Prüfe auf Division durch Null (oder sehr kleine Ableitung)
        # |f'(x_n)| <= tau * |f(x_n)|
        if abs(fprime_xn) <= tol * abs(f_xn):
            # Statt eines Errors geben wir hier einen Hinweis auf das Problem zurück
            print(
                f"WARNUNG: Newton-Verfahren abgebrochen: Ableitung f'(x) ist zu klein bei x={x_old:.4f}. Wert: {fprime_xn:.4e}")
            return x_old  # Gebe den letzten Wert zurück

        # Newton-Iterationsformel: x_{n+1} = x_n - f(x_n) / f'(x_n)
        correction = f_xn / fprime_xn
        x_new = x_old - correction

        # 2. Abbruchkriterium für die Lösung: |f(x_n)| < tau (Nullstelle gefunden)
        if abs(f(x_new)) < tol:
            return x_new

        # 3. Abbruchkriterium für den Fortschritt: |x_n - x_{n-1}| < tau (kein Fortschritt mehr)
        if abs(x_new - x_old) < tol:
            return x_new

        # Nächster Schritt
        x_old = x_new

    # Wenn die maximale Anzahl an Iterationen erreicht ist
    print(
        f"WARNUNG: Newton-Verfahren hat nach {max_iter} Iterationen nicht konvergiert.")
    return x_old  # Gebe den besten gefundenen Wert zurück

# --- Beispiele ---

# f(x) = x^2 - 4. Nullstelle ist x=2.


def f1(x):
    return x**2 - 4


def f1prime(x):
    return 2 * x


print("\n--- Beispiel 1: Konvergiert schnell ---")
nullstelle1 = newton(f1, f1prime, x0=10, tol=1e-6)
print(f"Nullstelle von x^2 - 4 (Startwert 10.0): {nullstelle1:.6f}")
