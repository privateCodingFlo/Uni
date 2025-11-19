import time
import random

# --------------------------------------------------------------------------------------------------
# AUFGABE 3: MERGE-SORT (REKURSIV)
# --------------------------------------------------------------------------------------------------

# Diese Funktion ist die Basis des Merge-Sort-Algorithmus (aus Aufgabe 2).
# Sie führt zwei bereits sortierte Listen zu einer neuen sortierten Liste zusammen.


def listen_zusammenfuehren(liste1, liste2):
    """
    Vereinigt (mergt) zwei bereits aufsteigend sortierte Listen (Two Pointers-Ansatz).
    """
    ergebnis_liste = []
    i, j = 0, 0
    len1, len2 = len(liste1), len(liste2)

    # 1. Hauptschleife: Vergleiche die Elemente aus beiden Listen und füge das kleinere hinzu.
    while i < len1 and j < len2:
        if liste1[i] <= liste2[j]:
            ergebnis_liste.append(liste1[i])
            i += 1
        else:
            ergebnis_liste.append(liste2[j])
            j += 1

    # 2. Reste hinzufügen: Füge die verbleibenden (größten) Elemente hinzu.
    ergebnis_liste.extend(liste1[i:])
    ergebnis_liste.extend(liste2[j:])

    return ergebnis_liste


def merge_sort(liste):
    """
    Sortiert eine Liste rekursiv mithilfe des Merge-Sort-Algorithmus (Divide and Conquer).

    :param liste: Die unsortierte Liste.
    :return: Die sortierte Liste.
    """

    # ABBRUCHBEDINGUNG (Basis-Fall): Wenn die Liste 0 oder 1 Element hat, ist sie sortiert.
    if len(liste) <= 1:
        return liste

    # 1. DIVIDE (Teilen): Liste halbieren
    mitte = len(liste) // 2
    linke_liste = liste[:mitte]
    rechte_liste = liste[mitte:]

    # 2. REKURSION (Sortieren der Unterlisten):
    # Die Funktion ruft sich selbst auf, um die Hälften immer weiter zu zerlegen und dann sortiert zusammenzuführen.
    linke_sortiert = merge_sort(linke_liste)
    rechte_sortiert = merge_sort(rechte_liste)

    # 3. CONQUER (Zusammenführen):
    # Die sortierten Hälften werden zusammengeführt (Merge).
    return listen_zusammenfuehren(linke_sortiert, rechte_sortiert)


# --------------------------------------------------------------------------------------------------
# DEMONSTRATION UND BONUS 1
# --------------------------------------------------------------------------------------------------

# --- Demonstration ---
unsortierte_liste = [38, 27, 43, 3, 9, 82, 10]
sortierte_liste = merge_sort(unsortierte_liste)

print("## Merge-Sort Demonstration")
print(f"Unsortiert: {unsortierte_liste}")
print(f"Sortiert:   {sortierte_liste}")


# --- Bonus 1: Laufzeitmessung ---

print("\n## Bonus 1: Laufzeitmessung (n = 2^k)")

# Definiere die k-Werte für die Messung (k=10, 11, 12, 13, 14, 15)
k_werte = list(range(10, 16))

print("| n (Größe) | k | Laufzeit (Sek.) | Verhältnis (Laufzeit / n) |")
print("|-----------|---|-----------------|---------------------------|")

# Funktion zur Durchführung der Messung


def messen_und_printen(k):
    n = 2 ** k

    # Erstelle eine zufällige Liste der Länge n
    test_liste = [random.randint(0, 1000000) for _ in range(n)]

    start_zeit = time.time()
    merge_sort(test_liste)
    end_zeit = time.time()

    laufzeit = end_zeit - start_zeit
    # Berechne das Verhältnis Laufzeit / n (für den Vergleich)
    verhaeltnis = laufzeit / n

    # Ausgabe der Ergebnisse
    print(f"| {n:<9} | {k:<1} | {laufzeit:.6f}        | {verhaeltnis:.9f} |")


# Führe die Messungen durch
for k in k_werte:
    messen_und_printen(k)

print("\n**Zusammenfassung zum Verhältnis von Laufzeit und n:**")
print("Die theoretische Laufzeitkomplexität des Merge-Sort-Algorithmus ist O(n log n).")
print("Das Verhältnis von Laufzeit zu n (Laufzeit / n) sollte daher proportional zu log n sein.")
print("In der Tabelle sehen wir, dass dieses Verhältnis mit steigendem n langsam zunimmt.")
print("Dies liegt daran, dass der zusätzliche Faktor (log n) die Anzahl der Rekursionsebenen widerspiegelt, die bei größeren Listen erhöht wird.")
