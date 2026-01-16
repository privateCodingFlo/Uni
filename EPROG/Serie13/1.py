def float_to_floating_point(x):
    """
    Theoretische Grundlagen für F(2, 4, -4, 4):
    ------------------------------------------
    Basis (B) = 2
    Präzision (p) = 4  => Mantisse hat die Form d.ddd (1 Vorkomma, 3 Nachkommastellen)
    Exponent (e) = [-4, 4]

    1. Darstellung von 2.75:
       2.75 = 2 + 0.5 + 0.25 = 10.11(binär)
       Normalisiert: 1.011 * 2^1
       Mantisse: 1.011 (Länge 4), Exponent: 1 (liegt im Bereich [-4, 4])
       -> Exakt darstellbar.

    2. Größte positive Zahl:
       Mantisse max: 1.111 (binär) = 1 + 1/2 + 1/4 + 1/8 = 1.875
       Exponent max: 4
       Rechnung: 1.875 * 2^4 = 1.875 * 16 = 30.0

    3. Kleinste positive Zahlen:
       - Normalisiert: 1.000 * 2^-4 = 1 * 1/16 = 0.0625
       - Nicht normalisiert (Subnormal): 0.001 * 2^-4 = 0.125 * 0.0625 = 0.0078125
    """

    if x == 0:
        return 0.0

    # Vorzeichen extrahieren
    sign = 1 if x >= 0 else -1
    abs_x = abs(x)

    # Simulation von Integer-Arithmetik durch Skalierung (z.B. Festkomma-Ersatz)
    # Wir nutzen einen hohen Faktor, um Rundungsfehler bei der Eingabe zu minimieren
    SCALE = 10**12
    val = int(abs_x * SCALE)

    p = 4
    e_min = -4
    e_max = 4

    # Hilfsfunktion für 2^e in skalierter Integer-Form
    def pow2_scaled(exp):
        if exp >= 0:
            return (2**exp) * SCALE
        else:
            return SCALE // (2**abs(exp))

    # 1. Sonderfall: Subnormale Zahlen (Bereich unterhalb der Normalisierungsgrenze)
    # Die kleinste normalisierte Zahl ist 1.000 * 2^-4
    norm_min_threshold = pow2_scaled(e_min)

    if val < norm_min_threshold:
        # Schrittweite für subnormale Zahlen: 2^e_min / 2^(p-1)
        step = norm_min_threshold // 8
        # Finde nächstes Vielfaches von step (m * 2^-4 / 8)
        m = (val + step // 2) // step
        # m kann hier 0, 1, ..., 7 sein
        return sign * (m * (2**e_min) / 8.0)

    # 2. Normalisierte Zahlen
    # Exponenten finden
    e = e_max
    while e > e_min and val < pow2_scaled(e):
        e -= 1

    # Überprüfung auf Überlauf (größer als größte darstellbare Zahl)
    max_val_scaled = (15 * pow2_scaled(e_max)) // 8
    if val >= max_val_scaled:
        return sign * 30.0

    # Mantisse bestimmen: Wir suchen m in {8, 9, ..., 15}
    # Da 2^e dem Wert m=8 entspricht (1.000 in Basis 2)
    step = pow2_scaled(e) // 8

    # Bestimme m durch kaufmännisches Runden zum nächsten Rasterpunkt
    m = (val + step // 2) // step

    # Falls m auf 16 rundet, springen wir zum nächsten Exponenten
    if m == 16:
        m = 8
        e += 1
        if e > e_max:
            return sign * 30.0

    # Finales Ergebnis (Rückkonvertierung nur für den Return-Wert)
    return sign * (m / 8.0) * (2**e)


# Beispiele laut Aufgabenstellung
print(f"Darstellung von 2.75: {float_to_floating_point(2.75)}")
print(f"Größte positive Zahl: {float_to_floating_point(100)}")  # Erzwingt Max
print(f"Kleinste positive Zahl (subnormal): {float_to_floating_point(0.001)}")
