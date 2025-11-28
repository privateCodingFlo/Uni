# ======================================================================
# AUFGABE 6: LUZIFER-RÄTSEL
# ======================================================================
# Zwei Zahlen x, y (2 <= x < y <= 99) werden gesucht. S = x + y < 100.

# 1. Rahmenbedingungen
MIN_VAL = 2    # Untere Grenze für x und y
MAX_VAL = 99    # Obere Grenze für x und y
MAX_SUM = 100   # Summe S MUSS kleiner als 100 sein.


def count_items(items):
    """
    Hilfsfunktion: Zählt die Häufigkeit von Elementen in einer Liste (wird für Produkte und Summen benötigt).
    """
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def solve_lucifer_puzzle():
    """
    Führt die logischen Schritte des Luzifer-Rätsels aus.
    """
    # 1. Initialisierung: Erstellen aller möglichen Paare (x, y) mit 2 <= x < y <= 99 und x+y < 100
    all_pairs = []
    for x in range(MIN_VAL, MAX_VAL + 1):
        for y in range(x + 1, MAX_VAL + 1):
            if x + y < MAX_SUM:
                all_pairs.append((x, y))

    # Gruppierung nach Produkt P und Summe S für die Logik
    pairs_by_product = {}
    pairs_by_sum = {}
    for x, y in all_pairs:
        P = x * y
        S = x + y

        # setdefault erstellt ein dictonary mit P als key und einer Liste als Value
        pairs_by_product.setdefault(P, []).append((x, y))
        pairs_by_sum.setdefault(S, []).append((x, y))

    # ---------------------------------------------
    # SCHRITT 1: Gauß: "Ich kenne die Zahlen nicht."
    # Das Produkt P muss ZWEI oder mehr mögliche Paare (Faktorisierungen) haben.
    # ---------------------------------------------
    non_unique_products = {
        P for P, pairs in pairs_by_product.items() if len(pairs) > 1}

    # G1_PAIRS: Die Menge der Paare (x, y), deren Produkt nicht eindeutig ist.
    g1_pairs = []
    for x, y in all_pairs:
        if x * y in non_unique_products:
            g1_pairs.append((x, y))

    # ---------------------------------------------
    # SCHRITT 2: Euler: "Das war mir klar."
    # JEDE mögliche Zerlegung (x', y') der Summe S MUSS die Bedingung aus Schritt 1 erfüllen (in G1_PAIRS sein).
    # ---------------------------------------------
    possible_sums_e2 = []
    for S, current_pairs in pairs_by_sum.items():
        is_e2_possible = True
        for pair in current_pairs:
            # Wenn ein Paar zu dieser Summe S nicht in G1_PAIRS ist, fällt die Summe S raus.
            if pair not in g1_pairs:
                is_e2_possible = False
                break
        if is_e2_possible:
            possible_sums_e2.append(S)

    # E2_PAIRS: Paare aus G1_PAIRS, deren Summe in der Liste der möglichen Summen liegt.
    e2_pairs = []
    for x, y in g1_pairs:
        if x + y in possible_sums_e2:
            e2_pairs.append((x, y))

    # ---------------------------------------------
    # SCHRITT 3: Gauß: "Jetzt kenne ich die Zahlen."
    # Das Produkt P MUSS in E2_PAIRS EINDEUTIG sein (nur einmal vorkommen).
    # ---------------------------------------------
    product_counts_in_e2 = count_items(x * y for x, y in e2_pairs)

    unique_products_in_e2 = {
        P for P, count in product_counts_in_e2.items() if count == 1}

    # G3_PAIRS: Die Paare aus E2_PAIRS, deren Produkt eindeutig ist.
    g3_pairs = []
    for x, y in e2_pairs:
        if x * y in unique_products_in_e2:
            g3_pairs.append((x, y))

    # ---------------------------------------------
    # SCHRITT 4: Euler: "Dann kenne ich sie jetzt auch."
    # Die Summe S MUSS in G3_PAIRS EINDEUTIG sein (nur einmal vorkommen).
    # ---------------------------------------------
    sum_counts_in_g3 = count_items(x + y for x, y in g3_pairs)

    unique_sums_in_g3 = {
        S for S, count in sum_counts_in_g3.items() if count == 1}

    # final_pairs: Das Endpaar muss eines der G3_PAIRS sein, dessen Summe eindeutig ist.
    final_pairs = []
    for x, y in g3_pairs:
        if x + y in unique_sums_in_g3:
            final_pairs.append((x, y))

    # Die Lösung muss eindeutig sein (es ist bekannt, dass nur (4, 13) übrig bleibt)
    if len(final_pairs) == 1:
        return final_pairs[0]
    else:
        print(f"WARNUNG: Mehr als ein oder kein Paar gefunden: {final_pairs}")
        return final_pairs[0] if final_pairs else (0, 0)


# --- Ausführung und Log für Rätsel ---
result_x, result_y = solve_lucifer_puzzle()
print("\n--- Ergebnis des Luzifer-Rätsels ---")
print(f"Die gesuchten Zahlen sind: ({result_x}, {result_y})")
print(f"Summe S = {result_x + result_y}. Produkt P = {result_x * result_y}")
