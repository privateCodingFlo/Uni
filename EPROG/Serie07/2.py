def listen_zusammenfuehren(liste1, liste2):
    """
    Vereinigt zwei bereits aufsteigend sortierte Listen zu einer einzigen
    aufsteigend sortierten Ergebnisliste.

    Es werden keine eingebauten Sortierfunktionen verwendet.

    :param liste1: Die erste aufsteigend sortierte Liste.
    :param liste2: Die zweite aufsteigend sortierte Liste.
    :return: Die resultierende, sortierte Liste.
    """

    # Die resultierende Liste, in der das Ergebnis gespeichert wird.
    ergebnis_liste = []

    # 1. Die "Pointer" (Zeiger):
    # Zeiger i zeigt auf das aktuelle Element in liste1
    i = 0
    # Zeiger j zeigt auf das aktuelle Element in liste2
    j = 0

    # Längen der Listen zur Vereinfachung
    len1 = len(liste1)
    len2 = len(liste2)

    # 2. Hauptschleife: Solange noch Elemente in BEIDEN Listen sind
    while i < len1 and j < len2:
        # Vergleiche die Elemente, auf die die Pointer zeigen:
        if liste1[i] <= liste2[j]:
            # Das Element aus liste1 ist kleiner (oder gleich), also gehört es als Nächstes
            # in die Ergebnisliste.
            ergebnis_liste.append(liste1[i])
            # Bewege den Zeiger i in liste1 zum nächsten Element.
            i += 1
        else:
            # Das Element aus liste2 ist kleiner, also gehört es als Nächstes
            # in die Ergebnisliste.
            ergebnis_liste.append(liste2[j])
            # Bewege den Zeiger j in liste2 zum nächsten Element.
            j += 1

    # 3. Restliche Elemente hinzufügen:
    # Wenn die erste Schleife beendet ist, bedeutet das, dass mindestens eine Liste
    # komplett abgearbeitet wurde. Die verbleibenden Elemente der ANDEREN Liste
    # sind bereits größer als alle Elemente in ergebnis_liste und müssen
    # daher einfach nur noch hinten angefügt werden.

    # Füge alle verbleibenden Elemente aus liste1 hinzu (falls vorhanden)
    ergebnis_liste.extend(liste1[i:])

    # Füge alle verbleibenden Elemente aus liste2 hinzu (falls vorhanden)
    ergebnis_liste.extend(liste2[j:])

    return ergebnis_liste

# --------------------------------------------------------------------------------------
# Beispiel zur Demonstration
# --------------------------------------------------------------------------------------


liste_a = [1, 5, 8, 12, 20]
liste_b = [2, 3, 5, 7, 10, 15]

ergebnis = listen_zusammenfuehren(liste_a, liste_b)

print("--- Demonstration ---")
print(f"Liste 1: {liste_a}")
print(f"Liste 2: {liste_b}")
print(f"Zusammengeführte Liste: {ergebnis}")

# Beispiel mit unterschiedlicher Länge (Liste C ist leer)
liste_c = []
liste_d = [100, 200, 300]
print("\nBeispiel mit leerer Liste:")
print(f"Ergebnis: {listen_zusammenfuehren(liste_c, liste_d)}")
