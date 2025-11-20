# AUFGABE 4: DIE TÜRME VON HANOI (Tower of Hanoi)

# --------------------------------------------------------------------------------------------------
# 1. INITIALISIERUNG
# --------------------------------------------------------------------------------------------------

# Die Anzahl der Scheiben für die Demonstration.
# WICHTIG: Für die Legende müsste N=64 sein (2^64 - 1 Züge), wir nutzen N=3 für eine schnelle Demo.
ANZAHL_SCHEIBEN = 3

# Die 3 Stäbe, dargestellt als verschachtelte Liste: [[Stab 1], [Stab 2], [Stab 3]].
# Die Scheibengröße ist die Zahl (z.B. 1=kleinste, 3=größte).
# Stab 1 startet mit allen Scheiben in absteigender Reihenfolge (größte unten, kleinste oben).
staebchen = [
    list(range(ANZAHL_SCHEIBEN, 0, -1)),  # Stab 1: [3, 2, 1] (wenn N=3)
    [],                                   # Stab 2: []
    []                                    # Stab 3: []
]

# Globaler Zähler für die ausgeführten Züge
zug_zaehler = 0

# --------------------------------------------------------------------------------------------------
# 2. HILFSFUNKTION: BEWEGE EINE SCHEIBE
# --------------------------------------------------------------------------------------------------


def bewege_scheibe(quelle, ziel):
    """
    Führt den Zug einer Scheibe zwischen zwei Stäben durch und protokolliert ihn.
    Prüft dabei Regel 3 (keine größere Scheibe auf eine kleinere).

    :param quelle: Index des Quellstabs (1, 2 oder 3)
    :param ziel: Index des Zielstabs (1, 2 oder 3)
    """
    global zug_zaehler

    # Umrechnung von Stab-Nummer (1, 2, 3) in Python-Index (0, 1, 2)
    quelle_idx = quelle - 1
    ziel_idx = ziel - 1

    # Hole die oberste Scheibe vom Quellstab (Regel 2: nur oberste Scheibe)
    scheibe = staebchen[quelle_idx].pop()

    # Prüfe Regel 3: Die oberste Scheibe auf dem Zielstab (falls vorhanden) muss größer sein.
    # stab[ziel_idx][-1] ist die oberste Scheibe des Zielstapels.
    if staebchen[ziel_idx] and staebchen[ziel_idx][-1] < scheibe:
        # Dies sollte im korrekten rekursiven Algorithmus nie passieren.
        print(
            f"\n!!! LOGIKFEHLER: Scheibe {scheibe} kann nicht auf Scheibe {staebchen[ziel_idx][-1]} auf Stab {ziel} gelegt werden.")
        # Scheibe zurück zur Quelle, da der Zug ungültig ist.
        staebchen[quelle_idx].append(scheibe)
        return

    # Führe den Zug durch (setze die Scheibe auf den Zielstapel)
    staebchen[ziel_idx].append(scheibe)

    # Protokolliere den Zug, wie in der Aufgabenstellung verlangt
    zug_zaehler += 1
    print(f"{zug_zaehler}. Zug: Bewege Scheibe {scheibe} von Stab {quelle} zu Stab {ziel}")


# --------------------------------------------------------------------------------------------------
# 3. REKURSIVE HAUPTFUNKTION: TÜRMEN VON HANOI
# --------------------------------------------------------------------------------------------------

def tuerme_von_hanoi(m, quelle, ziel, hilfsstab):
    """
    Löst das Problem rekursiv (Divide and Conquer), um m Scheiben von Quelle nach Ziel zu bewegen.

    :param m: Die Anzahl der zu bewegenden Scheiben
    :param quelle: Der Startstab (z.B. 1)
    :param ziel: Der Zielstab (z.B. 3)
    :param hilfsstab: Der temporäre Hilfsstab (z.B. 2)
    """

    # ABBRUCHBEDINGUNG: Wenn 0 Scheiben zu bewegen sind, sind wir fertig.
    if m <= 0:
        return

    # 1. Verschiebe die obersten m - 1 Scheiben von Quelle auf den Hilfsstab (nutze Ziel als Hilfsstab)
    #    -> Ziel: Die größte Scheibe (m) auf der Quelle ist nun frei.
    tuerme_von_hanoi(m - 1, quelle, hilfsstab, ziel)

    # 2. Bewege die größte Scheibe (m) von Quelle auf den Zielstab
    bewege_scheibe(quelle, ziel)

    # 3. Verschiebe die m - 1 Scheiben vom Hilfsstab auf den Zielstab (nutze Quelle als Hilfsstab)
    #    -> Ziel: Die m-1 Scheiben liegen nun sortiert auf der größten Scheibe (m) auf dem Zielstab.
    tuerme_von_hanoi(m - 1, hilfsstab, ziel, quelle)

# --------------------------------------------------------------------------------------------------
# 4. AUSFÜHRUNG DES ALGORITHMUS
# --------------------------------------------------------------------------------------------------


print(f"--- Lösung: Türme von Hanoi (N={ANZAHL_SCHEIBEN}) ---")
print(f"Start: Stab 1 mit Scheiben {staebchen[0]}. Ziel: Stab 3.")
print("--- Protokoll der Züge ---")

# Starte die Lösung: Bewege ANZAHL_SCHEIBEN von Stab 1 nach Stab 3 (mit Stab 2 als Hilfsstab)
tuerme_von_hanoi(ANZAHL_SCHEIBEN, 1, 3, 2)

print("--- Ergebnis ---")
print(
    f"Gesamtzahl der Züge: {zug_zaehler} (Minimal nötig: {2**ANZAHL_SCHEIBEN - 1})")
print(f"Endbelegung Stab 1: {staebchen[0]}")
print(f"Endbelegung Stab 2: {staebchen[1]}")
print(f"Endbelegung Stab 3: {staebchen[2]}")
