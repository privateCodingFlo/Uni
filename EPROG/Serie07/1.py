# Aufgabe 1: Die Recamán-Folge (Rekursiv und Iterativ)

# Die Recamán-Folge ist definiert durch:
# 1. a₀ = 0
# 2. aₙ = aₙ₋₁ - n, wenn (aₙ₋₁ - n) > 0 UND (aₙ₋₁ - n) noch nicht in der Folge vorkommt
# 3. aₙ = aₙ₋₁ + n, sonst

# --------------------------------------------------------------------------------------------------
# 1. Nicht-rekursive (Iterative) Funktion: Die effizientere Lösung
# --------------------------------------------------------------------------------------------------

def recaman_iterativ(n):
    """
    Berechnet das n-te Element der Recamán-Folge iterativ (Schritt-für-Schritt).
    Diese Methode ist die effizientere und stabilere Wahl für große n.

    :param n: Der Index des gesuchten Elements (a_n), n >= 0.
    :return: Das n-te Element a_n.
    """
    if n == 0:
        return 0

    # 'folge_elemente' (Set): Speichert alle bisher gesehenen Zahlen.
    # Sets erlauben eine extrem schnelle Prüfung, ob eine Zahl bereits in der Folge ist.
    folge_elemente = {0}

    # 'folge' (Liste): Speichert die Folge in der richtigen Reihenfolge (a_0, a_1, a_2, ...)
    folge = [0]

    # Durchlaufe alle Schritte von i=1 bis i=n.
    for i in range(1, n + 1):
        # Hole das vorherige Element (a_{i-1})
        a_vorher = folge[-1]

        # Versuche den Rückwärts-Sprung: a_{i-1} - i
        subtraktion = a_vorher - i

        # Prüfe die Bedingungen für den Rückwärts-Sprung:
        # 1. Ergebnis muss größer als 0 sein (subtraktion > 0) UND
        # 2. Ergebnis darf noch nicht in der Folge sein (subtraktion not in folge_elemente)
        if subtraktion > 0 and subtraktion not in folge_elemente:
            a_aktuell = subtraktion
        else:
            # Wenn der Rückwärts-Sprung verboten ist, führe den Vorwärts-Sprung durch: a_{i-1} + i
            a_aktuell = a_vorher + i

        # Füge das neue Element zur Liste und zum Set hinzu.
        folge.append(a_aktuell)
        folge_elemente.add(a_aktuell)

    # Das Ergebnis ist das n-te Element in der Liste.
    return folge[n]


# --------------------------------------------------------------------------------------------------
# 2. Rekursive Funktion: Mit Hilfsfunktion zur Zustandsverwaltung
# --------------------------------------------------------------------------------------------------

def _recaman_rekursiv_helfer(n, folge, folge_elemente):
    """
    Hilfsfunktion: Berechnet die Folge rekursiv, indem sie den Zustand (Folge und Set) 
    in jedem Aufruf mitschleppt.
    """
    # ABBRUCHBEDINGUNG: Wenn die Liste die Länge n+1 hat, haben wir a_n erreicht.
    if n == len(folge) - 1:
        return folge[-1]

    a_vorher = folge[-1]
    i = len(folge)  # Der aktuelle Sprung-Wert

    subtraktion = a_vorher - i

    # Regelprüfung wie oben (Rückwärts-Sprung erlaubt?)
    if subtraktion > 0 and subtraktion not in folge_elemente:
        a_aktuell = subtraktion
    else:
        a_aktuell = a_vorher + i

    # Zustand aktualisieren
    folge.append(a_aktuell)
    folge_elemente.add(a_aktuell)

    # REKURSIVER AUFRUF: Rufe die Funktion für den nächsten Schritt (nächsten Index) auf
    return _recaman_rekursiv_helfer(n, folge, folge_elemente)


def recaman_rekursiv(n):
    """
    Startet die rekursive Berechnung für das n-te Element (a_n).
    """
    if n == 0:
        return 0

    # Starte die Hilfsfunktion mit dem Anfangszustand: Folge=[0], Set={0}.
    return _recaman_rekursiv_helfer(n, [0], {0})


# --------------------------------------------------------------------------------------------------
# 3. Test und Ausgabe
# --------------------------------------------------------------------------------------------------

N = 10  # Index für den Test

print(f"--- Berechnung des {N}. Elements (a_{N-1}, da n bei 0 startet) ---")
print(f"Iterativ (a_{N-1}): {recaman_iterativ(N-1)}")
print(f"Rekursiv (a_{N-1}): {recaman_rekursiv(N-1)}")
print("---")


# --------------------------------------------------------------------------------------------------
# 4. Beantwortung der Frage
# --------------------------------------------------------------------------------------------------

# Welche der beiden Implementierungen kann größere Werte von n berechnen ohne einen Fehler zu erzeugen?
# Begründen Sie Ihre Antwort.

# Die nicht-rekursive (iterative) Implementierung kann größere Werte von n berechnen, ohne einen Fehler zu erzeugen.

# Begründung:
# Rekursive Funktion: Bei jedem Aufruf legt die Funktion einen Eintrag auf dem sogenannten Anrufstapel (Call Stack) des Systems ab. Python hat standardmäßig eine maximale Rekursionstiefe von 1000, um einen Stack Overflow zu verhindern. Für n-Werte über dieser Grenze (ca. n > 998) bricht die rekursive Funktion mit einem `RecursionError` ab.
# Iterative Funktion: Diese Funktion verwendet eine Schleife, die keine Einträge auf dem Call Stack hinterlässt. Sie speichert alle Zwischenergebnisse im normalen Arbeitsspeicher (Heap). Der einzige begrenzende Faktor ist hier der verfügbare Speicher (RAM), der erst bei extrem großen n-Werten (weit über 1000) relevant wird.
