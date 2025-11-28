# Aufgabe 6: Luzifer-Rätsel
# Zwei Zahlen x, y (2 <= x < y <= 99) werden gesucht. S = x + y < 100.

# 1. Rahmenbedingungen
MIN_VAL = 2
MAX_VAL = 99
MAX_SUM = 100  # Summe MUSS kleiner als 100 sein.


def get_possible_products(P, max_x_y):
    """
    Findet alle möglichen Paare (x, y) mit P = x*y, wobei 2 <= x < y <= max_x_y gilt.
    """
    pairs = []
    # Iteriere nur bis zur Wurzel von P, da y = P/x
    limit = int(P**0.5)
    for x in range(MIN_VAL, limit + 1):
        if P % x == 0:
            y = P // x
            # Paare müssen die Rahmenbedingungen erfüllen: x < y und y <= max_x_y
            if x < y and y <= max_x_y:
                pairs.append((x, y))
    return pairs


def count_items(items):
    """
    Ersatz für collections.Counter: Zählt die Häufigkeit von Elementen in einer Liste.
    """
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def solve_lucifer_puzzle():
    """
    Führt die logischen Schritte des Luzifer-Rätsels aus.
    """
    # 1. Initialisierung: Erstellen aller möglichen Paare (x, y)
    all_pairs = []
    for x in range(MIN_VAL, MAX_VAL + 1):
        for y in range(x + 1, MAX_VAL + 1):
            if x + y < MAX_SUM:
                all_pairs.append((x, y))

    # Paare nach Produkt und Summe gruppieren
    pairs_by_product = {}
    pairs_by_sum = {}
    for x, y in all_pairs:
        P = x * y
        S = x + y
        pairs_by_product.setdefault(P, []).append((x, y))
        pairs_by_sum.setdefault(S, []).append((x, y))

    # ---------------------------------------------
    # SCHRITT 1: Gauß: "Ich kenne die Zahlen nicht."
    # ---------------------------------------------
    # Produkt P muss mindestens ZWEI mögliche Paare (x, y) haben.

    # Produkte, die NICHT eindeutig sind (Länge > 1)
    non_unique_products = {
        P for P, pairs in pairs_by_product.items() if len(pairs) > 1}

    # G1_PAIRS: Paare, deren Produkt nicht eindeutig ist.
    g1_pairs = []
    for x, y in all_pairs:
        if x * y in non_unique_products:
            g1_pairs.append((x, y))

    # ---------------------------------------------
    # SCHRITT 2: Euler: "Das war mir klar."
    # ---------------------------------------------
    # Jedes Paar (x', y') mit Eulers Summe S MUSS in G1_PAIRS enthalten sein.

    # Die Summen S, für die ALLE Zerlegungen in G1_PAIRS liegen.
    possible_sums_e2 = []
    for S, current_pairs in pairs_by_sum.items():
        # Prüfen, ob alle Zerlegungen (x,y) von S auch in G1_PAIRS sind
        is_e2_possible = True
        for pair in current_pairs:
            if pair not in g1_pairs:
                is_e2_possible = False
                break

        if is_e2_possible:
            possible_sums_e2.append(S)

    # E2_PAIRS: Paare aus G1_PAIRS, deren Summe in possible_sums_e2 liegt.
    e2_pairs = []
    for x, y in g1_pairs:
        if x + y in possible_sums_e2:
            e2_pairs.append((x, y))

    # ---------------------------------------------
    # SCHRITT 3: Gauß: "Jetzt kenne ich die Zahlen."
    # ---------------------------------------------
    # Das Produkt P darf jetzt nur EIN Paar in E2_PAIRS haben.

    # Zähle Produkte in E2_PAIRS
    product_counts_in_e2 = count_items(x * y for x, y in e2_pairs)

    # Produkte, die nur einmal in E2_PAIRS vorkommen
    unique_products_in_e2 = {
        P for P, count in product_counts_in_e2.items() if count == 1}

    # G3_PAIRS: Paare aus E2_PAIRS, deren Produkt eindeutig in E2_PAIRS ist.
    g3_pairs = []
    for x, y in e2_pairs:
        if x * y in unique_products_in_e2:
            g3_pairs.append((x, y))

    # ---------------------------------------------
    # SCHRITT 4: Euler: "Dann kenne ich sie jetzt auch."
    # ---------------------------------------------
    # Die Summe S darf jetzt nur EIN Paar in G3_PAIRS haben.

    # Zähle Summen in G3_PAIRS
    sum_counts_in_g3 = count_items(x + y for x, y in g3_pairs)

    # Summen, die nur einmal in G3_PAIRS vorkommen
    unique_sums_in_g3 = {
        S for S, count in sum_counts_in_g3.items() if count == 1}

    # Das gesuchte Endpaar
    final_pairs = []
    for x, y in g3_pairs:
        if x + y in unique_sums_in_g3:
            final_pairs.append((x, y))

    if len(final_pairs) == 1:
        return final_pairs[0]
    else:
        # Die Lösung ist (4, 13)
        print(
            f"WARNUNG: Rätsel ist nicht eindeutig lösbar oder es wurde mehr als ein Paar gefunden: {final_pairs}")
        # Gebe bestes Ergebnis zurück
        return final_pairs[0] if final_pairs else (0, 0)


# --- Ausführung und Log ---
result_x, result_y = solve_lucifer_puzzle()
print("\n--- Ergebnis des Luzifer-Rätsels ---")
print(f"Die gesuchten Zahlen sind: ({result_x}, {result_y})")
print(f"Summe S = {result_x + result_y}. Produkt P = {result_x * result_y}")
