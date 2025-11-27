# Aufgabe 4: Adaptiertes Bisektionsverfahren
# Überprüfen, ob ein Vektor x mit der Eigenschaft |x_{i+1} - x_i| <= 1 das Element 0 enthält.

def contains_zero_adapted_bisection(x):
    """
    Überprüft, ob der Vektor x das Element 0 enthält, unter Ausnutzung der Kontinuitätsbedingung.
    Funktioniert effizient, wenn x[0] und x[n-1] unterschiedliche Vorzeichen haben.
    """
    n = len(x)
    if n == 0:
        return False

    # 1. Trivialfall: Endpunkte sind 0
    if x[0] == 0 or x[n - 1] == 0:
        return True

    left, right = 0, n - 1

    # Bestimme das Vorzeichen der Endpunkte
    sign_l = 1 if x[left] > 0 else -1
    sign_r = 1 if x[right] > 0 else -1

    # Wenn die Vorzeichen an den Enden GLEICH sind (z.B. [1, 2] oder [-1, -2]),
    # kann 0 nur enthalten sein, wenn der Vektor nicht monoton ist (z.B. [1, 0, 1]).
    # Das Bisektionsverfahren ist in diesem Fall nicht effizient/sicher,
    # da keine Nullstelle garantiert ist => müssen wir linear suchen.
    # Da die Aufgabe *explizit* ein Bisektionsverfahren verlangt, wenden wir dieses nur an,
    # wenn der Vorzeichenwechsel vorliegt. Ansonsten ist die einfachste Prüfung ein Loop.

    if sign_l == sign_r:
        # Fallback: Lineare Suche (einfacher Loop), um die 0 sicher zu finden,
        # da die Bisektion nur bei unterschiedlichen Vorzeichen funktioniert.
        for val in x:
            if val == 0:
                return True
        return False

    # 2. Bisektionsverfahren (Anwendbar, da unterschiedliche Vorzeichen vorhanden)
    while left <= right:
        # Mitte berechnen (verhindert Überlauf, ist aber hier nicht kritisch)
        mid = left + (right - left) // 2

        if x[mid] == 0:
            return True

        # Bestimme das Vorzeichen des Mittelpunkts (1: positiv, -1: negativ)
        sign_mid = 1 if x[mid] > 0 else -1

        # Wenn der Mittelpunkt dasselbe Vorzeichen wie das linke Ende hat,
        # muss der Vorzeichenwechsel (und damit die 0) im rechten Teil liegen.
        if sign_mid == sign_l:
            left = mid + 1
        # Andernfalls muss der Vorzeichenwechsel (und die 0) im linken Teil liegen.
        else:
            right = mid - 1

    return False


# --- Testfälle ---
x_works_1 = [5, 4, 3, 2, 1, 0, -1, -2]
x_fails_1 = [1, 0, 1]

print("\n--- Testfälle für Bisektions-Check ---")
print(
    f"Vektor 1: {x_works_1}. Enthält 0? {contains_zero_adapted_bisection(x_works_1)} (Erwartet True)")
print(f"Vektor 3: {x_fails_1}. Enthält 0? {contains_zero_adapted_bisection(x_fails_1)} (Erwartet True - via Fallback)")
