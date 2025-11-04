def pfz(n):
    """
    Berechnet die Primfaktorzerlegung der natürlichen Zahl n und gibt sie als 
    Dictionary der Form {"Primzahl": Exponent} zurück.
    Beispiel: pfz(12) -> {2: 2, 3: 1}
    """
    # Das Ergebnis-Dictionary
    factors = {}

    # Der aktuelle Teiler (startet bei der kleinsten Primzahl)
    i = 2

    # Solange i*i <= n ist, muss n entweder prim sein oder einen Primfaktor
    # <= sqrt(n) haben.
    # i * i <= n anstelle von i <= n**0.5, um keine Floating-Point-Arithmetik (Rundungsfehler durch float)
    # mit großen Zahlen zu verwenden.
    while i * i <= n:
        # Zähler für den Exponenten
        count = 0

        # Solange n durch i teilbar ist, erhöhen wir den Exponenten
        # und teilen n durch i.
        while n % i == 0:
            count += 1
            n //= i  # Ganzzahlige Division

        # Wenn count > 0, haben wir den Primfaktor i gefunden
        if count > 0:
            factors[i] = count

        # Nächster potenzieller Teiler
        # Wir können nach 2 nur ungerade Zahlen prüfen (i += 1 würde 4, 6, 8, ... prüfen)
        # Die Optimierung ist, nur 2 zu prüfen und dann mit 3 zu starten und in
        # Zweierschritten (3, 5, 7, ...) weiterzugehen.
        if i == 2:
            i += 1
        else:
            i += 2

    # Falls nach der Schleife n > 1 ist, ist der verbleibende Wert von n selbst eine Primzahl
    # (der größte Primfaktor mit dem Exponenten 1).
    if n > 1:
        factors[n] = 1

    return factors


# --- Beispiele ---
print(f"pfz(1): {pfz(1)}")       # Erwartet: {} (Da 1 keine Primfaktoren hat)
print(f"pfz(12): {pfz(12)}")     # Erwartet: {2: 2, 3: 1} (12 = 2^2 * 3^1)
print(f"pfz(13): {pfz(13)}")     # Erwartet: {13: 1} (13 ist prim)
# Erwartet: {2: 2, 3: 1, 5: 1} (60 = 2^2 * 3 * 5)
print(f"pfz(60): {pfz(60)}")
print(f"pfz(200): {pfz(200)}")   # Erwartet: {2: 3, 5: 2} (200 = 2^3 * 5^2)
print(f"pfz(200): {pfz(97)}")   # Erwartet: {97: 1} (97 = 97^1)
