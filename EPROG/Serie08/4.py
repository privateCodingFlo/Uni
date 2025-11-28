# Aufgabe 4: Adaptiertes Bisektionsverfahren
# Überprüfen, ob ein Vektor x mit der Eigenschaft |x_{i+1} - x_i| <= 1 das Element numbToSearch enthält.

def contains_numb_adapted_bisection(x, numbToSearch=0):
    """
    Überprüft, ob der Vektor x das Element numbToSearch enthält, indem das Problem 
    auf die Suche nach 0 in einem transformierten Vektor reduziert wird.

    Die Eigenschaft |x_{i+1} - x_i| <= 1 bleibt im transformierten Vektor x_t 
    (wobei x_t[i] = x[i] - numbToSearch) erhalten.

    :param x: Der Vektor von ganzen Zahlen.
    :param numbToSearch: Die gesuchte Zahl (Standard 0).
    :return: True, wenn numbToSearch enthalten ist, False sonst.
    """
    n = len(x)
    if n == 0:
        return False

    # Transformation des Vektors: Suche nach Y in X entspricht Suche nach 0 in X - Y
    # x_t ist der transformierte Vektor, der die "Nullstelle" der gesuchten Zahl Y enthält.
    x_t = [val - numbToSearch for val in x]
    n_t = len(x_t)

    # 1. Trivialfall: Endpunkte sind 0 im transformierten Vektor
    if x_t[0] == 0 or x_t[n_t - 1] == 0:
        return True

    left, right = 0, n_t - 1

    # Bestimme das Vorzeichen der Endpunkte des transformierten Vektors
    sign_l = 1 if x_t[left] > 0 else -1
    sign_r = 1 if x_t[right] > 0 else -1

    # Fallback/Edge-Case Check: Wenn die Vorzeichen an den Enden GLEICH sind,
    # liegt 0 nicht zwingend dazwischen (da Vektor nicht monoton).
    # Wir müssen linear suchen, um die 0 sicher zu finden.
    if sign_l == sign_r:
        # Fallback: Lineare Suche (einfacher Loop)
        for val in x_t:
            if val == 0:
                return True
        return False

    # 2. Bisektionsverfahren (Anwendbar, da unterschiedliche Vorzeichen vorhanden und Kontinuität gegeben)
    while left <= right:
        mid = left + (right - left) // 2
        # print("berechnete Mitte: " + mid)

        if x_t[mid] == 0:
            return True

        # Bestimme das Vorzeichen des Mittelpunkts
        sign_mid = 1 if x_t[mid] > 0 else -1

        # Wenn der Mittelpunkt dasselbe Vorzeichen wie das linke Ende hat,
        # muss der Vorzeichenwechsel (und damit die 0) im rechten Teil [mid+1, right] liegen.
        if sign_mid == sign_l:
            left = mid + 1
        # Andernfalls muss der Vorzeichenwechsel (und die 0) im linken Teil [left, mid-1] liegen.
        else:
            right = mid - 1

    return False


# --- Testfälle ---
x_works_1 = [5, 4, 3, 2, 1, 0, -1, -4]
x_fails_1 = [1, 0, 1]
x_fails_2 = [1, 3, 1]

print("\n--- Testfälle für Bisektions-Check (Suche nach 0) ---")
print(
    f"Vektor 1: {x_works_1}. Enthält 0? {contains_numb_adapted_bisection(x_works_1)}")
print(
    f"Vektor 3: {x_fails_1}. Enthält 0? {contains_numb_adapted_bisection(x_fails_1)}")
print(
    f"Vektor 3: {x_fails_2}. Enthält 0? {contains_numb_adapted_bisection(x_fails_2)}")


print("\n--- Testfälle für Bisektions-Check (Suche nach 4) ---")
print(
    f"Vektor 1: {x_works_1}. Enthält 4? {contains_numb_adapted_bisection(x_works_1, 4)}")
print(
    f"Vektor 3: {x_fails_1}. Enthält 4? {contains_numb_adapted_bisection(x_fails_1, 4)}")
print(
    f"Vektor 3: {x_fails_2}. Enthält 3? {contains_numb_adapted_bisection(x_fails_2, 3)}")
