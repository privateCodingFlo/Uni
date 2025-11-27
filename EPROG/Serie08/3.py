# Aufgabe 3: Wahrscheinlichkeit der Würfelsumme
# Sie haben n faire Würfel mit jeweils m_k Seiten (m_k = k+1).
# Berechnen Sie die Wahrscheinlichkeit, dass die Summe der Augenzahlen genau k beträgt.

# Ein Dictionary zum Speichern bereits berechneter Ergebnisse:
# Schlüssel: (num_dice, target_sum), Wert: Anzahl der Wege
memo = {}


def num_ways_to_get_sum(num_dice, target_sum):
    """
    Gibt die Anzahl der Möglichkeiten zurück, mit 'num_dice' Würfeln (m_i=i+1 Seiten) 
    die 'target_sum' zu erreichen, unter Verwendung von Memoization.
    """
    if target_sum < 0:
        return 0
    if num_dice == 0:
        return 1 if target_sum == 0 else 0

    # Prüfe, ob das Ergebnis bereits gespeichert wurde
    state = (num_dice, target_sum)
    if state in memo:
        return memo[state]

    # Der aktuelle Würfel hat m_n = num_dice + 1 Seiten (Augenzahlen 1 bis m_n)
    m_current = num_dice + 1

    count = 0
    # Der aktuelle Würfel wirft eine Augenzahl von 1 bis m_current.
    for roll in range(1, m_current + 1):
        # Addiere die Möglichkeiten des Restproblems (num_dice - 1 Würfel, Restsumme target_sum - roll)
        count += num_ways_to_get_sum(num_dice - 1, target_sum - roll)

    # Speichere das Ergebnis, bevor es zurückgegeben wird
    memo[state] = count
    return count


def probability(n, k):
    """
    Berechnet die Wahrscheinlichkeit P(Summe = k) für n Würfel (m_i = i+1 Seiten).
    """
    # 1. Berechnung der Gesamtanzahl möglicher Ergebnisse (N).
    if n <= 0:
        return 0.0

    total_outcomes = 1
    for i in range(1, n + 1):
        total_outcomes *= (i + 1)  # m_i = i + 1

    # Vor jeder neuen Wahrscheinlichkeitsberechnung muss der Speicher (memo) geleert werden,
    # falls die Funktion mehrmals aufgerufen wird.
    memo.clear()

    # 2. Berechnung der günstigen Ereignisse (G) mit Memoization.
    favorable_outcomes = num_ways_to_get_sum(n, k)

    # 3. Berechnung der Wahrscheinlichkeit P = G / N.
    if total_outcomes == 0:
        return 0.0

    return float(favorable_outcomes) / total_outcomes


# --- Testfälle ---
# Fall 2: 2 Würfel (m_1=2, m_2=3 Seiten), Gesamt-Ergebnisse: 6
# Summe 3: (1, 2) und (2, 1). -> 2 Möglichkeiten. P(Summe=3) = 2/6 = 1/3 ~ 0.3333
print("\n--- Test: 2 Würfel (m_1=2, m_2=3) ---")
print(f"P(Summe=3) für n=2, k=3: {probability(2, 3):.6f}%")
