def collatz(n, m):
    """
    Berechnet die ersten m Elemente der Collatz-Folge für eine gegebene Startzahl n.

    Args:
        n (int): Die Startzahl der Collatz-Folge (n = c_0).
        m (int): Die maximale Anzahl der zu berechnenden Elemente (c_0, ..., c_{m-1}).

    Returns:
        tuple: Eine Liste der Collatz-Folge-Elemente und
               die Schrittanzahl k, bis c_k = 1 ist, oder None, falls 1 nicht erreicht wird.
    """

    # 1. Initialisierung
    collatz_sequence = []
    current_c = n
    k_steps = 0  # Zählt die Schritte (k) bis c_k = 1

    # Die Schleife läuft maximal m Mal, um c_0 bis c_{m-1} zu berechnen.
    # Da wir in der Schleife direkt c_i zur Liste hinzufügen, prüfen wir auf len() < m
    while len(collatz_sequence) < m:
        # Füge das aktuelle Element c_i zur Liste hinzu
        collatz_sequence.append(current_c)

        # 2. Prüfen auf Ende der Folge (c_k = 1)
        # Die Schrittzahl k_steps wird erst NACH dem Eintreten von c_k=1 zurückgegeben
        # Wir müssen den Wert 1 zuerst hinzufügen und DANN prüfen
        if current_c == 1:
            # Das Element 1 wurde gerade hinzugefügt. Die Anzahl der Schritte k
            # ist die Anzahl der Elemente VOR der 1, also len() - 1.
            # Oder einfacher: k_steps ist die Anzahl der Iterationen, um von n zu 1 zu gelangen.
            return collatz_sequence, k_steps

        # 3. Berechne das nächste Element c_{i+1}
        if current_c % 2 == 0:
            # c_{i+1} = c_i / 2, falls c_i gerade ist
            next_c = current_c // 2
        else:
            # c_{i+1} = 3*c_i + 1, falls c_i ungerade ist
            next_c = 3 * current_c + 1

        current_c = next_c
        k_steps += 1

    # 4. Rückgabe, falls 1 nicht in den ersten m Elementen erreicht wurde
    # Wenn die Schleife beendet wird, ohne return, dann wurde 1 nicht gefunden.
    return collatz_sequence, None


# --- Testläufe ---
print("--- Testergebnisse Aufgabe 6: Collatz-Folge ---")

# Beispiel 1: n=6. Folge: 6, 3, 10, 5, 16, 8, 4, 2, 1. Schritte k=8.
# m=10 ist groß genug, um 1 zu erreichen
n1, m1 = 6, 10
folge1, schritte1 = collatz(n1, m1)
print(f"n={n1}, m={m1}: Folge: {folge1}")
print(f"Schritte bis 1 (k): {schritte1}")  # Erwartet: 8

# Beispiel 2: n=27. Die Folge ist sehr lang.
# m=10 ist zu klein, um 1 zu erreichen.
n2, m2 = 27, 10
folge2, schritte2 = collatz(n2, m2)
print(f"\nn={n2}, m={m2}: Folge: {folge2}")
print(f"Schritte bis 1 (k): {schritte2}")  # Erwartet: None


# Beispiel 2.5: n=27. Die Folge ist sehr lang.
# m=112 wäre groß genug.
n2, m2 = 27, 1112
folge2, schritte2 = collatz(n2, m2)
print(f"\nn={n2}, m={m2}: Folge: {folge2}")
print(f"Schritte bis 1 (k): {schritte2}")  # Erwartet: None

# Beispiel 3: n=1. Folge: 1. Schritte k=0.
n3, m3 = 1, 5
folge3, schritte3 = collatz(n3, m3)
print(f"\nn={n3}, m={m3}: Folge: {folge3}")
print(f"Schritte bis 1 (k): {schritte3}")  # Erwartet: 0
